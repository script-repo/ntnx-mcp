"""Tests for Prism Central client."""

import pytest
from ntnx_mcp.client import PrismCentralClient
from ntnx_mcp.config import Settings


@pytest.fixture
def settings():
    """Create test settings."""
    return Settings(
        host="192.168.1.100",
        username="admin",
        password="password",
    )


@pytest.fixture
def client(settings):
    """Create test client."""
    return PrismCentralClient(settings)


def test_build_url(client):
    """Test URL building."""
    url = client._build_url("vmm", "ahv/config/vms")
    assert url == "/vmm/v4.0/ahv/config/vms"


def test_build_url_custom_version(client):
    """Test URL building with custom version."""
    url = client._build_url("vmm", "ahv/config/vms", version="v4.0.a1")
    assert url == "/vmm/v4.0.a1/ahv/config/vms"


def test_build_query_params_empty(client):
    """Test query params with no filters."""
    params = client._build_query_params()
    assert params == {}


def test_build_query_params_filter(client):
    """Test query params with filter."""
    params = client._build_query_params(filter="name eq 'test'")
    assert params == {"$filter": "name eq 'test'"}


def test_build_query_params_all(client):
    """Test query params with all options."""
    params = client._build_query_params(
        filter="name eq 'test'",
        orderby="name asc",
        top=10,
        skip=20,
        select="name,id",
        expand="cluster",
    )
    assert params == {
        "$filter": "name eq 'test'",
        "$orderby": "name asc",
        "$top": "10",
        "$skip": "20",
        "$select": "name,id",
        "$expand": "cluster",
    }


def test_build_query_params_top_zero(client):
    """Test that top=0 is included in params."""
    params = client._build_query_params(top=0)
    assert params == {"$top": "0"}
