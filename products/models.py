from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    url=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    body=models.TextField()
    pub_date=models.DateTimeField()
    votes_total=models.IntegerField(default=1)
    image=models.ImageField(upload_to='product_photos/')
    icon=models.ImageField(upload_to='product_icons/')
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)
    upvoters=models.TextField()
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[0:150]
    
 