from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.

class Evaluation(models.Model):
    comment = models.CharField(max_length=1000 , blank=False)
    contact_method = models.CharField(max_length=1000 , blank=False)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='evaluations')
    antique_img = models.ImageField(upload_to='evaluation_photos/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.comment}'
    
class VerificationCode(models.Model):
    code = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def ___str__(self):
        return str(f"{self.code}")

    #overide the save method
    def save(self, *args, **kwargs):
        codes = [x for x in range(10)]
        code_items = []

        for x in range(5):
            verification_code = random.choice(codes)
            code_items.append(verification_code)

        verify_code = "".join(str(item) for item in code_items)
        self.code = verify_code
        super().save(*args, **kwargs)
