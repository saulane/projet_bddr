import csv
import os
import json
from collections import defaultdict

from datetime import datetime

from articles.models import *
from django.db import IntegrityError
from tqdm import tqdm

cord_uid_to_text = defaultdict(list)

DATA_DIR = "../../data/"

dict_study = {}

with open("test.csv", "r", encoding="utf8") as f_in:
    reader = csv.DictReader(f_in, delimiter=";")
    for row in reader:
        dict_study[row["Study"]] = [row["Theme"], row["Subtheme"], row["StudyType"]]

# open the file
with open(f"{DATA_DIR}metadata.csv", "r", encoding="utf8") as f_in:
    reader = csv.DictReader(f_in)
    i = 0
    for i,row in tqdm(enumerate(reader)):
        # if i == 5:
        #     break
        # access some metadata
        cord_uid = row['cord_uid']
        title = row['title']
        abstract = row['abstract']
        # authors = row['authors'].split('; ')
        doi = row['doi']
        journal = row['journal']
        try:
            article_date = datetime.strptime(row["publish_time"], "%Y-%m-%d")
        except:
            continue
        url = row["url"]
        authors_full = []

        # # access the full text (if available) for Intro
        introduction = []
        if row['pdf_json_files']:
            for json_path in row['pdf_json_files'].split('; '):
                with open(f"{DATA_DIR}{json_path}") as f_json:
                    full_text_dict = json.load(f_json)

                    authors_full = full_text_dict["metadata"]["authors"]

        article_study_type = None


        journal_obj = Journal(journal_name=journal)
        try:
            journal_obj.save()
        except IntegrityError:
            journal_obj = Journal.objects.get(journal_name=journal)   


        article = Article(date=article_date,
                          title=title,
                          abstract=abstract,
                          journal_id=journal_obj,
                          doi=doi,
                          url=url)
        try:
            article.save()
        except IntegrityError:
            article = Article.objects.get(doi=doi)

        authors_object = []
        for author in authors_full:

            

            new_author = Author(first_name=author["first"],
                                last_name=author["last"],
                                email=author["email"])
            if "laboratory" in author["affiliation"] and author["affiliation"]["laboratory"]:
                new_labo = Laboratory(labo_name = author["affiliation"]["laboratory"])
                try:
                    new_labo.save()
                except IntegrityError:
                    new_labo = Laboratory.objects.get(labo_name=author["affiliation"]["laboratory"])
                
                new_author.labo_id = new_labo

            if "institution" in author["affiliation"] and  author["affiliation"]["institution"]:
                new_insti = Institution(institution = author["affiliation"]["institution"])
                try:
                    new_insti.save()
                except IntegrityError:
                    new_insti = Institution.objects.get(institution=author["affiliation"]["institution"])
                new_author.institution_id = new_insti

            try:
                check_author = Author.objects.get(first_name=author["first"],
                                   last_name=author["last"],
                                   institution_id=new_insti,
                                   labo_id = new_labo)
                new_author = check_author
            except:
                new_author.save()

            try:
                Article_author.objects.get(article_id=article,author_id=new_author)
            except:
                article_author = Article_author(article_id=article,author_id=new_author)
                article_author.save()
            

                                



        if title in dict_study:
            i+=1

            theme = dict_study[title][0]
            subtheme = dict_study[title][1]
            studytype = dict_study[title][2]

            theme_obj = Theme(theme=theme)
            try:
                theme_obj.save()
            except IntegrityError:
                theme_obj = Theme.objects.get(theme=theme)            

            subtheme_obj = Subtheme(subtheme=subtheme,theme_id=theme_obj)
            try:
                subtheme_obj.save()
            except IntegrityError:
                subtheme_obj = Subtheme.objects.get(subtheme=subtheme)        

            article_study_type = Study_type(type=studytype)
            
            try:
                article_study_type.save()
            except IntegrityError:
                article_study_type = Study_type.objects.get(type=studytype)
            
            article.type_id = article_study_type
            article.subtheme_id = subtheme_obj
            article.save()
