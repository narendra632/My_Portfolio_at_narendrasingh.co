from django.db import models


class About(models.Model):
    name = models.CharField(max_length=100)
    about1 = models.TextField()
    about2 = models.TextField()
    i_am = models.CharField(max_length=100, default='')
    one_liner = models.CharField(max_length=200)
    career = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    freelance = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio')
    bgimage = models.ImageField(upload_to='portfolio')
    location = models.CharField(max_length=100)
    quote = models.CharField(max_length=200)
    favicon = models.ImageField(upload_to='portfolio', default='')
    apple_icon = models.ImageField(upload_to='portfolio', default='')
    meta_desc = models.TextField(default="")
    meta_keywords = models.CharField(max_length=300,default="")
    meta_href = models.URLField(max_length=200, default="")

    def __str__(self):
        return self.name


class Social(models.Model):
    linkedin = models.URLField(max_length=200)
    whatsapp = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)

    def __str__(self):
        return 'Social Media Links'


class Skill(models.Model):
    name = models.CharField(max_length=100)
    skill_img = models.FileField(upload_to='portfolio', blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

    def __str__(self):
        return self.course


class Experience(models.Model):
    role = models.CharField(max_length=100)
    year = models.CharField(max_length=100, blank=True)
    place = models.CharField(max_length=100, blank=True)
    clink = models.URLField(max_length=200, blank=True, default="")
    cname = models.CharField(max_length=50, blank=True)
    description1 = models.CharField(max_length=200, blank=True)
    description2 = models.CharField(max_length=200, blank=True)
    description3 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.role


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    filter = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    logo_image = models.ImageField(upload_to='portfolio', blank=True)
    image1 = models.ImageField(upload_to='portfolio', blank=True)
    image2 = models.ImageField(upload_to='portfolio', blank=True)
    image3 = models.ImageField(upload_to='portfolio', blank=True)
    project_date = models.CharField(max_length=100, default="")
    project_URL = models.CharField(max_length=200,default="")
    description = models.TextField(default="")

    def __str__(self):
        return self.description


class Service(models.Model):
    service_name = models.CharField(max_length=30)
    service_img = models.ImageField(upload_to='portfolio')
    service_icon = models.CharField(max_length=25)
    service_desc = models.TextField()

    def __str__(self):
        return self.service_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=70, default="")
    message = models.TextField(max_length=700,default="")

    def __str__(self):
        return self.name
