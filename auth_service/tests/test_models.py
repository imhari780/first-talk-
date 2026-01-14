from django.test import TestCase
from auth_service.models import User


class UserModelTest(TestCase):

    def test_user_creation(self):
        user = User.objects.create(
            username="hari", password="test123", role="participant"
        )

        self.assertEqual(user.username, "hari")
        self.assertEqual(user.role, "participant")
