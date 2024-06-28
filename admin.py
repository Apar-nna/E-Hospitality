from django.contrib import admin
from .models import CustomUser, UserProfile, LoginTable  # Ensure LoginTable matches the model name exactly

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(LoginTable)
