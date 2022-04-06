from django.test import TestCase

# my imports below
from .models import Post
from django.urls import reverse

# Create your tests here.
class PostTests(TestCase):
    @classmethod
    # this is a built-in method that creates initial data
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="Testing... Testing 1 2 3")

    # only functions that begin with the word 'test' will be run
    def test_model_content(self):
        # uses assertEqual to check that the content of the 'text' field matches what we expect
        self.assertEqual(self.post.text, "Testing... Testing 1 2 3")

    # test url exists at correct location
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # test that url is available by name
    # def test_url_available_by_name(self):
        # response = self.client.get(reverse("home"))
        # self.assertEqual(response.status_code, 200)

    # test if template name is correct
    # def test_template_name_correct(self):
        # response = self.client.get(reverse("home"))
        # self.assertTemplateUsed(response, "home.html")

    # test the template has the correct content
    # def test_template_content(self):
        # response = self.client.get(reverse("home"))
        # self.assertContains(response, "Testing... Testing 1 2 3")

    # combine the above into one single unit test
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Testing... Testing 1 2 3")
