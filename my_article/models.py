from django.db import models

# Create your models here.


from django.db import models

class Article(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    author = models.TextField(max_length=100)
    date = models.TextField(max_length=50)

    