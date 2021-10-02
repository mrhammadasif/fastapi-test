from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_file():
  resp = client.get("/files/hammad.txt")
  assert resp.status_code == 200
  assert resp.json()['file_path'] == "hammad.txt"