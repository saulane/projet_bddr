from django.db import models

# Create your models here.

class Theme(models.Model):
    theme = models.CharField(max_length=500, unique=True)

class Subtheme(models.Model):
    theme_id = models.ForeignKey(Theme, on_delete=models.CASCADE,null=True)
    subtheme = models.CharField(max_length=500, unique=True)

class Journal(models.Model):
    journal_name = models.CharField(max_length=200, unique=True)

class Study_type(models.Model):
    type = models.CharField(max_length=100,unique=True)

class Article(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=500)
    type_id = models.ForeignKey(Study_type, on_delete=models.CASCADE,null=True)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)
    subtheme_id = models.ForeignKey(Subtheme, on_delete=models.CASCADE,null=True)
    abstract = models.TextField(null=True)
    doi = models.CharField(max_length=300, unique=True)
    url = models.URLField()

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

class Article_author(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE,null=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)

