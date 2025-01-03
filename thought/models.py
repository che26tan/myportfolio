from django.db import models
from users.models import User
from django.utils.timezone import now

class likedislike(models.IntegerChoices):
    NONE = 0, 'None'
    LIKE = 1, 'Like'
    Dislike = 2, 'Dislike'

class Thought(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=now) 
    thought = models.CharField(max_length=500)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author_name}: {self.thought[:30]}"
    
class ThoughtStat(models.Model):
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now) 
    comments = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)