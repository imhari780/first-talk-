from django.test import TestCase


class RoomGatewayTest(TestCase):

    def test_room_gateway_basic(self):
        """
        Dummy test to validate room_gateway test execution.
        """
        response = self.client.get("/")

        self.assertIn(response.status_code, [200, 404])
