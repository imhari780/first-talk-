from django.test import TestCase


class AuthViewTest(TestCase):

    def test_dummy_auth_view(self):
        """
        Safe test to ensure auth_service test runner works.
        """
        response = self.client.get("/")

        self.assertIn(response.status_code, [200, 404])
