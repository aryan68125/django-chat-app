from django.contrib import admin

from user_app.models import User,UserDetials
# Register your models here.
@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    class Meta:
        model = User
    list_display = [field.name for field in User._meta.get_fields() if not field.many_to_many and not field.one_to_many]


@admin.register(UserDetials)
class UserDetialsAdmin(admin.ModelAdmin):
    class Meta:
        model = UserDetials
    list_display = [field.name for field in UserDetials._meta.get_fields() if not field.many_to_many and not field.one_to_many]