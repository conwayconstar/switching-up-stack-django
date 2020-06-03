from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):
    """
    Set the user Model.
    """
    User = get_user_model()

    def test_create_user(self):
        """
        Tests creating a standard user.
        Test that the user is created with the set variables.
        Test if there is a type error if no params are passed in.
        Test if there is a type error if no password is passed in.
        Test if there is a value error if email is blank.
        Test if there is a value error trying
        to create a superuser with normal user method.
        """
        email = 'conway@trichome.tech'
        password = 'smokedope420'
        first_name = 'Conway'
        last_name = 'Kush'
        occupation = 'Software engineer'
        company = 'Trichome Tech'
        profile_title = 'We out here building cool shit.'

        user = self.User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            occupation=occupation,
            company=company,
            profile_title=profile_title,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.occupation, occupation)
        self.assertEqual(user.company, company)
        self.assertEqual(user.profile_title, profile_title)
        with self.assertRaises(TypeError):
            self.User.objects.create_user()
        with self.assertRaises(TypeError):
            self.User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            self.User.objects.create_user(
                email='',
                password=password
            )
        with self.assertRaises(ValueError):
            self.User.objects.create_user(
                email='failuser@fail.com',
                password=password,
                is_superuser=True
            )

    def test_create_superuser(self):
        """
        Tests creating a superuser.
        Test that the superuser is created with the set variables.
        Test if there is a value error trying
        to create a normal user with superuser method.
        """
        email = 'k@kidcurrent.tv'
        password = 'weouthere420'
        first_name = 'Kid'
        last_name = 'Current'
        occupation = 'Product Designer'
        company = 'KidCurrent TV'

        user = self.User.objects.create_superuser(
            email=email,
            first_name=first_name,
            last_name=last_name,
            occupation=occupation,
            company=company,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.occupation, occupation)
        self.assertEqual(user.company, company)
        self.assertTrue(user.is_superuser)

        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                email='superfail@fail.com',
                password='foo',
                is_superuser=False
            )

    def test_get_by_id(self):
        """
        Tests user get by id.
        Tests if method has value
        Tests if user exists
        """
        email = 'k@kidcurrent.tv'
        password = 'weouthere420'
        first_name = 'Kid'
        last_name = 'Current'
        occupation = 'Product Designer'
        company = 'KidCurrent TV'

        user = self.User.objects.create_superuser(
            email=email,
            first_name=first_name,
            last_name=last_name,
            occupation=occupation,
            company=company,
            password=password
        )

        user = self.User.objects.get_by_id(user.id)

        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.occupation, occupation)
        self.assertEqual(user.company, company)
        self.assertTrue(user.is_superuser)

        with self.assertRaises(ValueError):
            self.User.objects.get_by_id()

        with self.assertRaises(self.User.DoesNotExist):
            self.User.objects.get_by_id(99)
