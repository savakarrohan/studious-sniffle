from urllib import response
from django.test import SimpleTestCase

# Create your tests here.
class HomepageTests(SimpleTestCase):
    """Test for home page URL being root URL"""
    def test_url_exists_at_correct_location(self):
        """test Url"""
        response1 = self.client.get("/")
        self.assertEqual(response1.status_code,200)
         
class AboutpageTests(SimpleTestCase):
    """Tests for the about page"""
    def test_url_exists_at_correct_location(self):
        """Test URL at correct location"""
        response2 = self.client.get("/about/")
        self.assertEqual(response2.status_code,200)