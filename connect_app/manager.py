from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class StudentManager(BaseUserManager):
    # Email acts as unique identifier for auth

    # Creates and saves Student with email and password
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email must be provided'))
        email = self.normalize_email(email)
        user, created = self.get_or_create(username=username, email=email, **extra_fields)
        user.set_password(password)
        return user

    # Create a superuser with email and password
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # Check extra fields
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have "is_staff"=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have "is_superuser"=True'))

        # Call create_user to create the super user
        return self.create_user(username, email, password, **extra_fields)
