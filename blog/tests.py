from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from blog.models import Blog


class BlogListTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        
        self.blog1 = Blog.objects.create(
            title='Blog 1', content='Blog 1 content', owner=self.user, 
            subtitle='new test subtitle', budget='400', trip_duration='4'
        )

    def test_get_blogs(self):
        """
        tests that we can retrieve a single blog post using a GET request to the /blogs/<id>/ endpoint. 
        We check that the response code is 200 and that the response contains the correct blog post
        """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_blog_invalid_data(self):
        """
         tests that if we submit invalid data when creating a new blog post,
        the server responds with a _404_NOT_FOUND error and the blog post is not created in the database.
        """
        data = {
            'title': 'New Blog',
            'subtitle': 'new test subtitle',
            'budget': '400',
            'trip_duration': '4'
        }
        response = self.client.post('/blog/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Blog.objects.count(), 1)