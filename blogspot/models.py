from django.db import models, migrations
from django.urls import reverse


# Create your models here.
class PostForm(models.Model):
    title = models.CharField(max_length=200)
    # author = models.ForeignKey(
    #     'auth.User',
    #     on_delete=models.CASCADE,
    # )
    body = models.TextField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('post_detail', args=[str(self.id)])
