from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    c_post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    c_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="c_author")
    comment = models.TextField()
    timestamp = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.c_post.title} - {self.c_author}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})