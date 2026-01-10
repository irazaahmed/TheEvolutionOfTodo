"""
Simple test to verify the application starts and basic functionality works
"""
import asyncio
from app.main import app
from fastapi.testclient import TestClient


def test_app_starts():
    """Test that the application starts without errors"""
    assert app is not None
    print("✓ Application object created successfully")


def test_root_endpoint():
    """Test the root endpoint"""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo Backend API - Phase II Part 1"}
    print("✓ Root endpoint works correctly")


def test_api_docs_available():
    """Test that API documentation is available"""
    client = TestClient(app)

    # Test that docs are available
    response = client.get("/docs")
    assert response.status_code == 200
    print("✓ API documentation available")

    # Test that OpenAPI schema is available
    response = client.get("/openapi.json")
    assert response.status_code == 200
    openapi_schema = response.json()
    assert "Todo API" in openapi_schema["info"]["title"]
    print("✓ OpenAPI schema available")


if __name__ == "__main__":
    test_app_starts()
    test_root_endpoint()
    test_api_docs_available()
    print("\n✓ All basic functionality tests passed!")