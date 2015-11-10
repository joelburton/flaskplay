import unittest

from flaskplay import create_app

app = create_app('flaskplay.config.TestConfig')


class TreatsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_rediret(self):
        """Test homepage."""

        r = self.client.get("/")
        self.assertEqual(r.status_code, 302)

    def test_homepage(self):
        """Test homepage."""

        r = self.client.get("/treats/")
        self.assertEqual(r.status_code, 200)

    def test_other(self):
        """Test crash page."""

        self.assertRaises(Exception, self.client.get, "/treats/other?crash=yes")

    def test_other_ok(self):
        """Test crash page."""

        r = self.client.get("/treats/other")
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()