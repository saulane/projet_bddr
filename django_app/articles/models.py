from django.db import models

# Create your models here.

class Theme(models.Model):
    theme = models.CharField(max_length=400, unique=True)

class Subtheme(models.Model):
    theme_id = models.ForeignKey(Theme, on_delete=models.CASCADE,null=True)
    subtheme = models.CharField(max_length=500, unique=True)

class Journal(models.Model):
    journal_name = models.CharField(max_length=500, unique=True)

class Study_type(models.Model):
    type = models.CharField(max_length=500,unique=True)

class Laboratory(models.Model):
    labo_name = models.TextField(unique=True)

class Institution(models.Model):
    institution = models.TextField(unique=True)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    institution_id = models.ForeignKey(Institution, on_delete=models.CASCADE,null=True)
    labo_id = models.ForeignKey(Laboratory, on_delete=models.CASCADE,null=True)

class Article(models.Model):
    date = models.DateField()
    title = models.TextField()
    type_id = models.ForeignKey(Study_type, on_delete=models.CASCADE,null=True)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)
    subthemes = models.ManyToManyField(Subtheme)
    abstract = models.TextField(null=True)
    doi = models.CharField(max_length=500, unique=True)
    authors = models.ManyToManyField(Author)
    url = models.URLField(max_length=500)
