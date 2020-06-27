from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser.
        """
        user = self.create_user(
            email,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """ Custome User Model """

    email = models.EmailField(max_length=255, primary_key=True, verbose_name='email address', unique=True, default=None)
    Business_Name = models.CharField(max_length=255, default=None, blank=False, null=False, verbose_name = 'Bussiness Name' )
    Business_Website = models.CharField(max_length=255, blank=True, default=None, verbose_name = 'Bussiness Website')
    First_Name = models.CharField(max_length=255, default=None, blank=False, null=False, verbose_name = 'First Name')
    Last_Name = models.CharField(max_length=255, blank=True, default=None, verbose_name = 'Last Name')
    Phone_Number = PhoneNumberField(blank=True, default=None, verbose_name = 'Phone Number')
    gridCheck = models.BooleanField(default=False,blank=False, null=False)
    is_Influencer = models.BooleanField(default=False, blank=False, null=False)
    is_Brand = models.BooleanField(default=False, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['Business_Name','First_Name', 'gridCheck']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    