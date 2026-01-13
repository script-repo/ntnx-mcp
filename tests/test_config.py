"""Tests for configuration module."""

import os
import pytest
from ntnx_mcp.config import Settings


def test_settings_base_url():
    """Test base URL generation."""
    settings = Settings(
        host="192.168.1.100",
        username="admin",
        password="password",
    )
    assert settings.base_url == "https://192.168.1.100:9440/api"


def test_settings_custom_port():
    """Test custom port in base URL."""
    settings = Settings(
        host="192.168.1.100",
        port=8443,
        username="admin",
        password="password",
    )
    assert settings.base_url == "https://192.168.1.100:8443/api"


def test_settings_has_credentials_with_username_password():
    """Test credential detection with username/password."""
    settings = Settings(
        host="192.168.1.100",
        username="admin",
        password="password",
    )
    assert settings.has_credentials is True


def test_settings_has_credentials_with_api_key():
    """Test credential detection with API key."""
    settings = Settings(
        host="192.168.1.100",
        api_key="test-api-key",
    )
    assert settings.has_credentials is True


def test_settings_no_credentials():
    """Test credential detection with no credentials."""
    settings = Settings(
        host="192.168.1.100",
    )
    assert settings.has_credentials is False


def test_auth_header_basic():
    """Test basic auth header generation."""
    settings = Settings(
        host="192.168.1.100",
        username="admin",
        password="password",
    )
    header = settings.get_auth_header()
    assert "Authorization" in header
    assert header["Authorization"].startswith("Basic ")


def test_auth_header_api_key():
    """Test API key header generation."""
    settings = Settings(
        host="192.168.1.100",
        api_key="test-api-key",
    )
    header = settings.get_auth_header()
    assert header == {"X-Ntnx-Api-Key": "test-api-key"}


def test_auth_header_api_key_takes_precedence():
    """Test that API key takes precedence over username/password."""
    settings = Settings(
        host="192.168.1.100",
        username="admin",
        password="password",
        api_key="test-api-key",
    )
    header = settings.get_auth_header()
    assert "X-Ntnx-Api-Key" in header
    assert "Authorization" not in header


def test_settings_defaults():
    """Test default values."""
    settings = Settings(
        host="192.168.1.100",
        username="admin",
        password="password",
    )
    assert settings.port == 9440
    assert settings.verify_ssl is True
    assert settings.timeout == 30
