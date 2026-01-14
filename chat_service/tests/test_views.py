# from django.test import TestCase
# from django.urls import reverse


# class ChatViewTest(TestCase):

#     def test_dummy_view_test(self):
#         """
#         This test only checks that Django test runner works
#         and does not break due to URL issues.
#         """
#         response = self.client.get("/")

#         # Root URL irundhaal 200, illatti 404
#         self.assertIn(response.status_code, [200, 404])


# import pytest
# from django.urls import reverse
# from rest_framework.test import APIClient
# from chat_service.models import Message


# @pytest.mark.django_db
# def test_send_message_api():
#     client = APIClient()

#     payload = {
#         "room_id": "room_test",
#         "sender_id": "user_test",
#         "content": "Hello machan",
#     }

#     response = client.post(
#         "/api/messages/send/",
#         payload,
#         format="json",
#     )

#     assert response.status_code == 201
#     assert Message.objects.count() == 1

#     message = Message.objects.first()
#     assert message.room_id == "room_test"
#     assert message.sender_id == "user_test"
#     assert message.content == "Hello machan"
import pytest
from rest_framework.test import APIClient
from chat_service.models import Message


@pytest.mark.integration
@pytest.mark.django_db
def test_send_message_api():
    client = APIClient()

    payload = {
        "room_id": "room_test",
        "sender_id": "user_test",
        "content": "Hello machan",
    }

    response = client.post(
        "/api/messages/send/",
        payload,
        format="json",
    )

    # Check if API response is 201 Created
    assert response.status_code == 201

    # Check if message is saved in DB
    assert Message.objects.count() == 1

    message = Message.objects.first()

    # Validate DB fields
    assert message.room_id == "room_test"
    assert message.sender_id == "user_test"
    assert message.content == "Hello machan"


@pytest.mark.integration
@pytest.mark.django_db
def test_send_message_api_invalid_data():
    client = APIClient()

    # Payload missing 'content' field (required)
    payload = {
        "room_id": "room_test",
        "sender_id": "user_test",
        # content missing
    }

    response = client.post(
        "/api/messages/send/",
        payload,
        format="json",
    )

    assert response.status_code == 400
    assert "content" in response.data  # Error message should mention missing content


@pytest.mark.integration
@pytest.mark.django_db
def test_delete_message_api():
    client = APIClient()

    # Create message to delete
    message = Message.objects.create(
        room_id="room_test",
        sender_id="user_test",
        content="Message to delete",
    )

    response = client.delete(f"/api/messages/{message.room_id}/{message.message_id}/")

    assert response.status_code == 204

    # Reload from DB to check soft delete fields
    message.refresh_from_db()
    assert message.visibility_state == "deleted"
    assert message.deleted_at is not None
