# %%
from members.models import Member
import csv
import pandas as pd

df=pd.read_excel("Member.xlsx")
# print(df)

# %%
for index, row in df.iterrows():
    print(row['name'])
    object = Member.objects.get(id=row['id'])
    object.position = row['position']
    object.office = row['office']
    object.lab = row['lab']
    object.lab_location = row['lab_location']
    object.expertise = row['expertise']
    object.graduate = row['graduate']
    object.experience = row['experience']
    object.patent = row['patent']
    object.awarded = row['awarded']
    object.published_accepted_papers = row['published_accepted_papers']
    object.published_refered_papers = row['published_refered_papers']
    object.published_conference_foreign = row['published_conference_foreign']
    object.published_conference_domestic = row['published_conference_domestic']
    object.project_tech = row['project_tech']
    object.project_gen = row['project_gen']
    object.students_doc = row['students_doc']
    object.students_master = row['students_master']
    object.students_honor = row['students_honor']
    object.students_conference = row['students_conference']
    object.save()
# %%
