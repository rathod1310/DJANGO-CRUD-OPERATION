from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200,null=False)
    author = models.CharField(max_length=200,null=False)
    price = models.IntegerField(null=False)
    publication_date = models.DateField(auto_now=False,null=False)

    def __str__(self):
        return self.name
