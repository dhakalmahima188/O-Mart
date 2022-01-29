from django.db import models

# Create your models here.
class desitnation(models.Model):
    # id: int
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True)
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    is_featured=models.BooleanField(default=False)
