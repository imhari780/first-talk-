from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class DialogueFlowTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='hari', password='1234')
        self.client.login(username='hari', password='1234')

    def test_full_dialogue_flow(self):
        # Start session
        res = self.client.post('/dialogue/start')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        session_id = res.data['session_id']

        # Send message
        res = self.client.post(
            f'/dialogue/{session_id}/message',
            {"content": "Hello"}
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("content", res.data)

        # End session
        res = self.client.post(f'/dialogue/{session_id}/end')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_no_second_active_session(self):
        self.client.post('/dialogue/start')
        res = self.client.post('/dialogue/start')
        self.assertEqual(res.status_code, status.HTTP_409_CONFLICT)
