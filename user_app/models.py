from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from user_app.user_manager import UserManager
from django.utils import timezone
import os
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

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

def user_profile_picture_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"profile_picture.{ext}"  # optional rename
    return os.path.join("profile_pictures", str(instance.user.pk), filename)
class UserDetials(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_detials")
    name = models.CharField(max_length=200,null=True,blank=True)
    mobile_number = models.CharField(max_length=10,null=True,blank=True)
    profile_picture = models.ImageField(upload_to=user_profile_picture_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name