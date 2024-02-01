from allauth.socialaccount.models import SocialAccount
from django.db import models


# Create your views here.
class ProfileModel(models.Model):
    social_account = models.OneToOneField(SocialAccount, on_delete=models.CASCADE)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    picture = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'Waqt_profilemodel'

    def __str__(self):
        return str(self.email)


class SendMessageModel(models.Model):
    city = [('Toshkent', 'Toshkent'),
            ('Andijon', 'Andijon'),
            ('Buxoro', 'Buxoro'),
            ('Denov', 'Denov'),
            ('Guliston', 'Guliston'),
            ('Jizzax', 'Jizzax'),
            ('Margilon', "Marg'ilon"),
            ('Namangan', 'Namangan'),
            ('Navoiy', 'Navoiy'),
            ('Nukus', 'Nukus'),
            ('Olmaliq', 'Olmaliq'),
            ('Qarshi', 'Qarshi'),
            ('Qoqan', "Qo'qon"),
            ('Samarqand', 'Samarqand'),
            ('Olmaliq', 'Olmaliq'),
            ('Termiz', 'Termiz'),
            ("Xiva", 'Xiva')]
    email = models.EmailField()
    city = models.CharField(max_length=20, choices=city)
    recurrent = models.CharField(max_length=10, choices=[('1', '1 kun'),('2', '2 kun'),('3', '3 kun'),('5', '5 kun')])
    route = models.CharField(max_length=10, choices=[('gmail', 'Gmail orqali'), ('telegram', 'Telegram orqali'), ('juftlik', 'Ikkalasidan ham')])
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
