from fastapi.testclient import TestClient

from main import app

print(app.user_middleware)

client = TestClient(app)

def test_stream_chat():

    payload = {
        "session_id": "stream_test",
        "prompt": "Explain JWT",
        "mode": "backend"
    }

    response = client.post(
        "/ai/chat/stream",
        json=payload
    )

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

def test_normal_chat():

    payload = {
        "session_id": "stream_test",
        "prompt": "What is FastAPI?",
        "mode": "backend"
    }

    response = client.post(
        "/ai/chat",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert body["session_id"] == "stream_test"

    assert len(body["response"]) > 0

def test_get_conversation():

    response = client.get(
        "/ai/conversation/stream_test"
    )

    assert response.status_code == 200

    body = response.json()

    assert body["session_id"] == "stream_test"

    assert len(body["messages"]) > 0

def test_list_conversations():

    response = client.get(
        "/ai/conversations"
    )

    assert response.status_code == 200

    assert isinstance(response.json(), list)

def test_delete_conversation():

    response = client.delete(
        "/ai/conversation/stream_test"
    )

    assert response.status_code == 200

def test_verify_delete():

    response = client.get(
        "/ai/conversation/stream_test"
    )

    body = response.json()

    assert body["messages"] == []