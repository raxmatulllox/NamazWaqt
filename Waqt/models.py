from allauth.socialaccount.models import SocialAccount
from django.db import models


# Create your views here.
class ProfileModel(models.Model):
        social_account = models.OneToOneField(SocialAccount, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        email = models.EmailField()
        name = models.CharField(max_length=255)
        picture = models.URLField(null=True, blank=True)

        class Meta:
            db_table = 'profilemodel'

        def __str__(self):
            return str(self.created_at)
