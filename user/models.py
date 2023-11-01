from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext as _
from django.db import models


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    class ROLES:
        EXECUTOR = 'executor'
        AUDITOR = 'auditor'
        SUPER_ADMIN = 'super_admin'

        ROLES_CHOICES = (
            (SUPER_ADMIN, 'Супер әкімші'),
            (EXECUTOR, 'Орындаушы'), (AUDITOR, 'Аудитор'),
        )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)  # Optional field
    group = models.CharField(max_length=100, null=True, blank=True)  # Optional field
    specialty = models.CharField(max_length=100, null=True, blank=True)  # Non-required field

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES.ROLES_CHOICES,
                            default=ROLES.EXECUTOR)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'first_name', 'last_name', 'birthday', 'group', 'specialty']

    objects = UserManager()

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name} Email: {self.email}; Role: {self.role}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_super_admin(self):
        return self.role == User.ROLES.SUPER_ADMIN

    @property
    def is_executor(self):
        return self.role == User.ROLES.EXECUTOR

    @property
    def is_auditor(self):
        return self.role == User.ROLES.AUDITOR

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
