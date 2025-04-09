from django.contrib import admin

# Register your models here.
from .models import Answer, UserLike

admin.site.register(Answer)
admin.site.register(UserLike)
