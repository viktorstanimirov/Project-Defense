from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .forms import ProductCreateForm, ProductUpdateForm, ProductDeleteForm
from .models import Product

UserModel = get_user_model()


class ProductViewTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='12345', email='test@example.com')
        self.client.login(username='testuser', password='12345')

        image = SimpleUploadedFile(name='test_image.jpg', content=b'some image data', content_type='image/jpeg')

        self.product = Product.objects.create(
            name="Sample Product",
            price=10.00,
            description="Sample Description",
            image=image
        )

    def test_product_create_view_get(self):
        response = self.client.get(reverse('create-food'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/create-food.html')
        self.assertIsInstance(response.context['form'], ProductCreateForm)

    def test_product_detail_view_get(self):
        response = self.client.get(reverse('details-food', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/details-food.html')
        self.assertEqual(response.context['product'], self.product)

    def test_product_update_view_get(self):
        response = self.client.get(reverse('update-food', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/update-food.html')
        self.assertIsInstance(response.context['form'], ProductUpdateForm)
        self.assertEqual(response.context['form'].instance, self.product)

    def test_product_delete_view_get(self):
        response = self.client.get(reverse('delete-food', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/delete-food.html')
        self.assertIsInstance(response.context['form'], ProductDeleteForm)

    def test_product_delete(self):
        response = self.client.post(reverse('delete-food', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('menu'))
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())



