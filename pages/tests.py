from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepageTests(SimpleTestCase):
    """Test for home page"""
    def test_url_exists_at_correct_location(self):
        """test URL of homepage"""
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
        
    def test_url_available_by_name(self):
        """ test if URL is available by name"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        
    def test_template_name_correct(self):
        """test if the template is correct template"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
         
class AboutpageTests(SimpleTestCase):
    """Tests for the aboutpage"""
    def test_url_exists_at_correct_location(self):
        """Test URL at correct location"""
        response = self.client.get("/about/")
        self.assertEqual(response.status_code,200)
        
    def test_url_available_by_name(self):
        """ test if URL is available by name"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)
        
    def test_template_name_correct(self): 
        """test if the template is correct template"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")