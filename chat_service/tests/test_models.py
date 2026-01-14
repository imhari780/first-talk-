# from django.test import TestCase
# from chat_service.models import Message


# class MessageModelTest(TestCase):

#     def test_message_creation(self):
#         message = Message.objects.create(
#             room_id="room1",
#             sender_id="user1",
#             content="Hello"
#         )

#         # Assert (this is the REAL unit test)
#         self.assertEqual(message.content, "Hello")
#         self.assertEqual(message.room_id, "room1")


import pytest
from chat_service.models import Message


@pytest.mark.integration
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
