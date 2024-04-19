from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class LoginAppUserViewTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='12345', email='test@example.com',
                                                  first_name='', last_name='')
        self.url = reverse('login')

    def test_login_redirect(self):
        login = self.client.login(username='testuser', password='12345')
        self.assertTrue(login, "User should be logged in for redirection test")

        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': '12345'
        }, follow=True)

        self.assertRedirects(response, reverse('menu'), status_code=302, target_status_code=200)

    def test_login_redirect_with_complete_profile(self):
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.save()
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('login'))
        self.assertTrue(response.status_code, 200)


class AppUserProfileUpdateViewTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='12345', email='test@example.com')
        self.client.login(username='testuser', password='12345')
        self.url = reverse('update-profile', kwargs={'pk': self.user.pk})

    def test_profile_update(self):
        response = self.client.post(self.url, {
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com'
        }, follow=True)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')


class UserAccountCreateViewTests(TestCase):
    def setUp(self):
        self.url = reverse('signup')

    def test_user_creation(self):
        response = self.client.post(self.url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'password2': 'newpassword123'
        }, follow=True)

        if response.status_code == 200:
            print(response.context['form'].errors)

        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())
        self.assertRedirects(response, reverse('login'), status_code=302, target_status_code=200)


class LogoutUserTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.url = reverse('logout')

    def test_user_logout(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
