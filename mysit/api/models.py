from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish_date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title


