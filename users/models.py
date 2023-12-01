from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evaluation(models.Model):
    comment = models.CharField(max_length=1000 , blank=False)
    contact_method = models.CharField(max_length=1000 , blank=False)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='evaluations')
    antique_img = models.ImageField(upload_to='evaluation_photos/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.comment}'
