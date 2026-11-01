from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_hello_default_and_param():
    assert client.get("/api/hello").json() == {"message": "hello, world"}
    assert client.get("/api/hello", params={"name": "vunet"}).json() == {"message": "hello, vunet"}


def test_hello_truncates_long_input():
    assert len(client.get("/api/hello", params={"name": "a" * 500}).json()["message"]) == len("hello, ") + 64


def test_security_headers_present():
    r = client.get("/health")
    assert r.headers["x-content-type-options"] == "nosniff"
    assert r.headers["x-frame-options"] == "DENY"
    assert "default-src 'none'" in r.headers["content-security-policy"]


def test_api_docs_disabled():
    assert client.get("/docs").status_code == 404
    assert client.get("/openapi.json").status_code == 404
