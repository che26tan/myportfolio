from django.db import models
from users.models import User
from django.utils.timezone import now

# class RatingStar(models.IntegerChoices):
#     NORATE = 0, 'No Rating'
#     VERYBAD = 1, 'Very Bad'
#     BAD = 2, 'Bad'
#     GOOD = 3, 'Good'
#     VERYGOOD = 4, 'Very Good'
#     EXCELLENT = 5, 'Excellent' 

class Category(models.IntegerChoices):
    OTHER = 0, 'Other'
    TECH=1, 'Technology'
    HW = 2, 'Health & Wellness'
    LS = 3, 'Lifestyle'
    BF = 4, 'Business & Finance'
    ENTERTAINMENT = 5, 'Entertainment'   

class likedislike(models.IntegerChoices):
    NONE = 0, 'None'
    LIKE = 1, 'Like'
    Dislike = 2, 'Dislike'


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=now) 
    blog_title = models.CharField(max_length=200, unique=True)
    blog_des = models.TextField(max_length=1000)
    blog_category = models.IntegerField(choices=Category.choices, default=Category.OTHER)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blog_title} ({self.blog_category})"

class BlogStat(models.Model):
    blog_title = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now) 
    # blog_rating = models.IntegerField(choices=RatingStar.choices, default=RatingStar.NORATE)
    comments = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)