from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta, date
import time

class BaseModel(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Company(BaseModel):
    city = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    zip = models.IntegerField(max_length=5, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=6000, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    website = models.URLField(max_length=120, null=True, blank=True)
    employees = models.IntegerField(null=True, blank=True)
    contact_name = models.CharField(max_length=120, null=True, blank=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=120, blank=True)
    profile_pic = models.ImageField(upload_to='uploads/', null=True, blank=True)
    profile_background = models.ImageField(upload_to='uploads/', null=True, blank=True)

# class Language(models.Model):
#     language = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.language
#
#
# class CompanyProject(models.Model):
#     project_name = models.CharField(max_length=1000)
#     created = models.DateField(auto_now=True)
#     company = models.ForeignKey(Company, related_name='company_projects')
#     language = models.ForeignKey(Language, blank=True, null=True)
#     completed = models.BooleanField()
#     project_screenshot = models.ImageField(upload_to="images/developer_screenshots", blank=True, null=True)
#     description = models.TextField(max_length=6000, blank=True, null=True)
#     accepted_project = models.OneToOneField('developer_app.DeveloperProject', related_name="company_pick", blank=True, null=True)
#     deadline = models.DateField(blank=True, null=True)
#
#     def __unicode__(self):
#         return self.project_name

class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    state = models.CharField(max_length=120, blank=True)
    zip = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=120, blank=True)
    company = models.ForeignKey(Company, related_name="home_company", null=True, blank=True)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)


class Project(BaseModel):
    date = models.DateField(default=(date.today() + timedelta(days=14)))
    start_time = models.TimeField(default="10:00")
    bounty = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=10000)
    contact_name = models.CharField(max_length=120)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=120, null=True, blank=True)
    sample_screenshot = models.FileField(upload_to='uploads/', null=True, blank=True)
    finished_screenshot = models.FileField(upload_to='uploads/', null=True, blank=True)
    website = models.URLField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return "{} - {}".format(self.date, self.name)


class Developer(BaseModel):
    birthdate = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=120, blank=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=6000, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='uploads', null=True, blank=True)
    profile_background = models.ImageField(upload_to='uploads', null=True, blank=True)
    github = models.URLField(max_length=1000, blank=True, null=True)
    portfolio_site = models.URLField(max_length=1000, blank=True, null=True)

    user = models.OneToOneField(User, null=True, blank=True)

    def current_age(self):
        birthday = time.strptime(self.birthdate)
        return datetime.now() - datetime(birthday)

    def calculate_age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

    age = property(calculate_age)


# class DeveloperProject(models.Model):
#     project_name = models.CharField(max_length=1000)
#     created = models.DateField(auto_created=True, auto_now=False)
#     developer = models.ForeignKey(Developer, related_name="projects")
#     company_project = models.ForeignKey(CompanyProject, related_name="developer_projects")
#     project_screenshot = models.ImageField(upload_to="images/developer_screenshots", blank=True, null=True)
#     description = models.TextField(max_length=6000, blank=True, null=True)
#     completed = models.BooleanField()
#
#     def __unicode__(self):
#         return self.project_name



