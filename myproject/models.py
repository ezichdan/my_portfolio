from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category

    
class Project(models.Model):
    tittle = models.CharField(max_length=60)
    description = models.TextField()
    proj_img1 = models.ImageField(upload_to='projects/proj_img1', blank=True, null=True)
    proj_img2 = models.ImageField(upload_to='projects/proj_img2', blank=True, null=True)
    proj_img3 = models.ImageField(upload_to='projects/proj_img3', blank=True, null=True)
    client = models.CharField(max_length=100, default='')  # Provide a default value here
    project_url = models.URLField(max_length=200, default='')  # Provide a default value here
    time_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_created = models.DateField(auto_now_add=True, blank=True)
    

    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.tittle


class Resume(models.Model):
    tittle = models.CharField(max_length=60)
    file = models.FileField(upload_to='resume', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.tittle
    
    
