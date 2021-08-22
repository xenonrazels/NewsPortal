from django.db import models

# Create your models here.
class News(models.Model):
    ''''News model with it's attribute'''
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    featured_image=models.ImageField(upload_to='news/')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name= "News"
        verbose_name_plural="News"
    