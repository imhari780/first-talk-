import pytest
from chat_service.models import Message


@pytest.mark.django_db
def test_message_model_create():
    message = Message.objects.create(
        room_id="room_test",
        sender_id="user_test",  # ✅ correct field
        content="Hello machan",
    )

    assert message.room_id == "room_test"
    assert message.sender_id == "user_test"
    assert message.content == "Hello machan"
    assert message.deleted_at is None
