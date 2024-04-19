from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from FastFoodApp.products.models import Product

UserModel = get_user_model()


class WebViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = UserModel.objects.create_user(username='testuser', password='12345', email='test@example.com')
        self.client.login(username='testuser', password='12345')

        image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')

        for i in range(10):
            Product.objects.create(
                name=f"Product {i}",
                price=10.00 + i,
                description=f"Description {i}",
                image=image
            )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/index.html')
        self.assertEqual(response.context['user'], self.user)

    def test_menu_view_pagination(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/menu.html')
        self.assertEqual(len(response.context['products']), 5)
        self.assertTrue(response.context['page_obj'])
        self.assertEqual(response.context['page_obj'].number, 1)  # First page

        # Test the second page
        response = self.client.get(reverse('menu') + '?page=2')
        self.assertEqual(len(response.context['products']), 5)
        self.assertEqual(response.context['page_obj'].number, 2)
