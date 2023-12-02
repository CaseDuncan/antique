from django.contrib import admin
from .models import VerificationCode , Evaluation , CustomUser
# Register your models here.

admin.site.register(VerificationCode)
admin.site.register(Evaluation)
admin.site.register(CustomUser)
