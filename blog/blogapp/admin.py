from django.contrib import admin
from .models import post, category, Profile,Comment

# Register your models here.
admin.site.register(post)
admin.site.register(category)
admin.site.register(Profile)
admin.site.register(Comment)
