from django.db import models
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)


# Lamda func -> when userprof is used, check if they exist & create if not
User.userprofile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])
