from django.db import models

# Create your models here.

class Subtheme(models.Model):
    subtheme_name = models.CharField(max_length=300, unique=True)

class Theme(models.Model):
    theme_name = models.CharField(max_length=200, unique=True)

class Journal(models.Model):
    journal_name = models.CharField(max_length=200, unique=True)

class Study_type(models.Model):
    type = models.CharField(max_length=100, unique=True)

class Study(models.Model):
    name = models.CharField(max_length=100)
    study_type_id = models.ForeignKey(Study_type)

class Article(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=300)
    study_id = models.ForeignKey(Study)
    journal_id = models.ForeignKey(Journal)
    theme_id = models.ForeignKey(Theme)
    doi = models.URLField()

class Article_theme(models.Model):
    article_id = models.ForeignKey(Article)
    subtheme_id = models.ForeignKey(Subtheme)

class Labo(models.Model):
    labo_name = models.CharField(max_length=100, unique=True)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    labo_id = models.ForeignKey(Labo)

class Article_author(models.Model):
    article_id = models.ForeignKey(Article)
    author_id = models.ForeignKey(Author)

