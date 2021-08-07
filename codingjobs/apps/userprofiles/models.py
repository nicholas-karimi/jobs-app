from django.db import models
from django.contrib.auth.models import User 

from apps.jobs.models import Application

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)


# Lamda func -> when userprof is used, check if they exist & create if not
User.userprofile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])


class ConversationMessage(models.Model):
    application = models.ForeignKey(Application, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmaessages', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']