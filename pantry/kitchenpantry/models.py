# Create your models here.
# -*- coding: utf-8 -*-
from allauth.socialaccount.models import SocialAccount
import hashlib
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
import hashlib


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())

class Ingredient(models.Model):
    name = models.TextField()
    class Meta:
        db_table = 'ingredient'

class Pantry(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    user = models.ForeignKey(UserProfile)

class Recipe(models.Model):
    name = models.TextField()
    author = models.TextField()
    ingredients = models.TextField()
    recipeyield = models.TextField()
    difficulty = models.TextField()
    totaltime = models.TextField()
    activetime = models.TextField()
    directions = models.TextField()
    class Meta:
        db_table = 'recipe'
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

