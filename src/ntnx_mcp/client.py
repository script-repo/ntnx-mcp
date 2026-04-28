"""Prism Central API client."""

import uuid as _uuid
from typing import Any, Optional

import httpx

from ntnx_mcp.config import Settings


class PrismCentralError(Exception):
    """Base exception for Prism Central API errors."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        details: Optional[str] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.details = details
        super().__init__(message)


class AuthenticationError(PrismCentralError):
    """Authentication failed."""
    pass


class NotFoundError(PrismCentralError):
    """Resource not found."""
    pass


class RateLimitError(PrismCentralError):
    """Rate limit exceeded."""
    pass


class ValidationError(PrismCentralError):
    """Request validation failed."""
    pass


class PrismCentralClient:
    """HTTP client for Prism Central v4 API."""

    API_VERSION = "v4.0"

    def __init__(self, settings: Settings):
        self.settings = settings
        self._client: Optional[httpx.AsyncClient] = None

    async def v3_list(
        self,
        resource: str,
        kind: str,
        filter: Optional[str] = None,
        length: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """List entities using v3 API (POST with body filter).
        
        The v3 API uses POST /api/nutanix/v3/{resource}/list with filter in body.
        """
        client = await self._get_client()
        url = f"/nutanix/v3/{resource}/list"
        
        body: dict[str, Any] = {
            "kind": kind,
            "length": length,
            "offset": offset,
        }
        if filter:
            body["filter"] = filter
        
        try:
            response = await client.request(
                method="POST",
                url=url,
                json=body,
            )
        except httpx.ConnectError as e:
            raise PrismCentralError(
                f"Connection failed to {self.settings.host}:{self.settings.port}. "
                "Verify the host is accessible and the port is correct.",
                details=str(e),
            )
        except httpx.TimeoutException as e:
            raise PrismCentralError(
                f"Request timed out after {self.settings.timeout} seconds.",
                details=str(e),
            )

        if response.status_code >= 400:
            self._handle_error(response)

        return response.json()

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create the HTTP client."""
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url=self.settings.base_url,
                headers={
                    **self.settings.get_auth_header(),
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                verify=self.settings.verify_ssl,
                timeout=httpx.Timeout(self.settings.timeout),
            )
        return self._client

    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client and not self._client.is_closed:
            await self._client.aclose()
            self._client = None

    def _build_url(
        self,
        namespace: str,
        path: str,
        version: Optional[str] = None,
    ) -> str:
        """Build the API URL for a request."""
        api_version = version or self.API_VERSION
        return f"/{namespace}/{api_version}/{path}"

    def _build_query_params(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        select: Optional[str] = None,
        expand: Optional[str] = None,
    ) -> dict[str, str]:
        """Build OData query parameters."""
        params: dict[str, str] = {}
        if filter:
            params["$filter"] = filter
        if orderby:
            params["$orderby"] = orderby
        if top is not None:
            params["$top"] = str(top)
        if skip is not None:
            params["$skip"] = str(skip)
        if select:
            params["$select"] = select
        if expand:
            params["$expand"] = expand
        return params

    def _handle_error(self, response: httpx.Response) -> None:
        """Handle API error responses."""
        status = response.status_code
        try:
            error_data = response.json()
            message = error_data.get("message", response.text)
            details = error_data.get("details", None)
        except Exception:
            message = response.text
            details = None

        if status == 401:
            raise AuthenticationError(
                "Authentication failed. Check your credentials.",
                status_code=status,
                details=details,
            )
        elif status == 403:
            raise AuthenticationError(
                "Permission denied. User lacks required permissions.",
                status_code=status,
                details=details,
            )
        elif status == 404:
            raise NotFoundError(
                f"Resource not found: {message}",
                status_code=status,
                details=details,
            )
        elif status == 429:
            raise RateLimitError(
                "Rate limit exceeded. Slow down requests.",
                status_code=status,
                details=details,
            )
        elif status == 422 or status == 400:
            raise ValidationError(
                f"Validation error: {message}",
                status_code=status,
                details=details,
            )
        else:
            raise PrismCentralError(
                f"API error ({status}): {message}",
                status_code=status,
                details=details,
            )

    async def request(
        self,
        method: str,
        namespace: str,
        path: str,
        body: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, str]] = None,
        version: Optional[str] = None,
        request_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """Make an API request."""
        client = await self._get_client()
        url = self._build_url(namespace, path, version)

        headers = {}
        if request_id:
            headers["Ntnx-Request-Id"] = request_id

        try:
            response = await client.request(
                method=method,
                url=url,
                json=body,
                params=params,
                headers=headers if headers else None,
            )
        except httpx.ConnectError as e:
            raise PrismCentralError(
                f"Connection failed to {self.settings.host}:{self.settings.port}. "
                "Verify the host is accessible and the port is correct.",
                details=str(e),
            )
        except httpx.TimeoutException as e:
            raise PrismCentralError(
                f"Request timed out after {self.settings.timeout} seconds.",
                details=str(e),
            )

        if response.status_code >= 400:
            self._handle_error(response)

        if response.status_code == 204:
            return {"status": "success"}

        return response.json()

    async def list(
        self,
        namespace: str,
        path: str,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        select: Optional[str] = None,
        expand: Optional[str] = None,
        version: Optional[str] = None,
    ) -> dict[str, Any]:
        """List entities with OData query support."""
        params = self._build_query_params(
            filter=filter,
            orderby=orderby,
            top=top,
            skip=skip,
            select=select,
            expand=expand,
        )
        return await self.request("GET", namespace, path, params=params, version=version)

    async def get(
        self,
        namespace: str,
        path: str,
        entity_id: str,
        select: Optional[str] = None,
        expand: Optional[str] = None,
        version: Optional[str] = None,
    ) -> dict[str, Any]:
        """Get a single entity by ID."""
        params = self._build_query_params(select=select, expand=expand)
        full_path = f"{path}/{entity_id}"
        return await self.request("GET", namespace, full_path, params=params, version=version)

    async def create(
        self,
        namespace: str,
        path: str,
        body: dict[str, Any],
        request_id: Optional[str] = None,
        version: Optional[str] = None,
    ) -> dict[str, Any]:
        """Create an entity."""
        return await self.request(
            "POST", namespace, path, body=body, request_id=request_id, version=version
        )

    async def update(
        self,
        namespace: str,
        path: str,
        entity_id: str,
        body: dict[str, Any],
        request_id: Optional[str] = None,
        version: Optional[str] = None,
    ) -> dict[str, Any]:
        """Update an entity."""
        full_path = f"{path}/{entity_id}"
        return await self.request(
            "PUT", namespace, full_path, body=body, request_id=request_id, version=version
        )

    async def delete(
        self,
        namespace: str,
        path: str,
        entity_id: str,
        request_id: Optional[str] = None,
        version: Optional[str] = None,
    ) -> dict[str, Any]:
        """Delete an entity."""
        full_path = f"{path}/{entity_id}"
        return await self.request(
            "DELETE", namespace, full_path, request_id=request_id, version=version
        )

    async def action(
        self,
        namespace: str,
        path: str,
        entity_id: str,
        action: str,
        body: Optional[dict[str, Any]] = None,
        request_id: Optional[str] = None,
        version: Optional[str] = None,
    ) -> dict[str, Any]:
        """Perform an action on an entity."""
        full_path = f"{path}/{entity_id}/${action}"
        return await self.request(
            "POST", namespace, full_path, body=body, request_id=request_id, version=version
        )

    async def get_with_etag(
        self,
        namespace: str,
        path: str,
        entity_id: str,
        version: Optional[str] = None,
    ) -> tuple[dict[str, Any], str]:
        """GET an entity and return (body, etag) for optimistic concurrency.

        The v4 update workflow requires the ETag from a prior GET to be sent
        back via the ``If-Match`` header on the subsequent PUT.
        """
        client = await self._get_client()
        url = self._build_url(namespace, f"{path}/{entity_id}", version)

        try:
            response = await client.request(method="GET", url=url)
        except httpx.ConnectError as e:
            raise PrismCentralError(
                f"Connection failed to {self.settings.host}:{self.settings.port}. "
                "Verify the host is accessible and the port is correct.",
                details=str(e),
            )
        except httpx.TimeoutException as e:
            raise PrismCentralError(
                f"Request timed out after {self.settings.timeout} seconds.",
                details=str(e),
            )

        if response.status_code >= 400:
            self._handle_error(response)

        etag = response.headers.get("etag", "")
        if not etag:
            raise PrismCentralError(
                "Server did not return an ETag header, cannot perform safe update.",
                status_code=response.status_code,
            )

        return response.json(), etag

    async def update_with_etag(
        self,
        namespace: str,
        path: str,
        entity_id: str,
        body: dict[str, Any],
        etag: str,
        version: Optional[str] = None,
    ) -> dict[str, Any]:
        """PUT an entity with ``If-Match`` (ETag) and ``Ntnx-Request-Id``.

        This is the standard v4 optimistic-concurrency update pattern.
        """
        client = await self._get_client()
        url = self._build_url(namespace, f"{path}/{entity_id}", version)
        request_id = str(_uuid.uuid4())
        headers = {
            "If-Match": etag,
            "Ntnx-Request-Id": request_id,
        }

        try:
            response = await client.request(
                method="PUT", url=url, json=body, headers=headers,
            )
        except httpx.ConnectError as e:
            raise PrismCentralError(
                f"Connection failed to {self.settings.host}:{self.settings.port}. "
                "Verify the host is accessible and the port is correct.",
                details=str(e),
            )
        except httpx.TimeoutException as e:
            raise PrismCentralError(
                f"Request timed out after {self.settings.timeout} seconds.",
                details=str(e),
            )

        if response.status_code >= 400:
            self._handle_error(response)

        if response.status_code == 204:
            return {"status": "success"}

        return response.json()
