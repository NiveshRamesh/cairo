from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_and_get_note():
    r = client.post("/api/notes", json={"text": "hello"})
    assert r.status_code == 201
    note_id = r.json()["id"]
    assert client.get(f"/api/notes/{note_id}").json() == {"id": note_id, "text": "hello"}


def test_missing_note_is_404():
    assert client.get("/api/notes/9999").status_code == 404


def test_empty_note_is_rejected():
    assert client.post("/api/notes", json={"text": ""}).status_code == 422
