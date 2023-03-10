import os
import csv
import pandas as pd

DATA_DIR = "../data/Kaggle/target_tables"

dir_list = ["1_population", "2_relevant_factors","3_patient_descriptions","4_models_and_open_questions",
            "5_materials","6_diagnostics","7_therapeutics_interventions_and_clinical_studies","8_risk_factors",
            "unsorted_tables/key_scientific_questions","unsorted_tables/risk_factors"]

dict_name_theme = []

i=0
for d in dir_list:
    current_file_list = os.listdir(f"{DATA_DIR}/{d}")
    for f in current_file_list:
        i+=1
        print(i)
        with open(f"{DATA_DIR}/{d}/{f}","r",encoding="utf8") as f_in:
            reader = csv.DictReader(f_in)
            for row in reader:
                study = row["Study"]
                theme = d[2:].split("/")[-1]
                study_type = row["Study Type"] if "Study Type" in row else None
                if len(dict_name_theme) > 0 and dict_name_theme[-1]["Study"] != study:
                    dict_name_theme.append({ 'Study': study,'Theme': theme,'Subtheme':  f.rstrip("csv"),"StudyType": study_type})
                elif len(dict_name_theme) == 0:
                    dict_name_theme.append({ 'Study': study, 'Theme': theme,'Subtheme':  f.rstrip("csv"),"StudyType": study_type})

print(len(dict_name_theme))

with open("test.csv", 'w', encoding="utf8",newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Study", "Theme", "Subtheme","StudyType"], delimiter=";")
    writer.writeheader()
    writer.writerows(dict_name_theme)