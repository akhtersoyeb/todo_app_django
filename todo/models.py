from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    startdate = models.DateTimeField('released on')
    enddate = models.DateTimeField('ending on')

    def __str__(self):
        return self.title
