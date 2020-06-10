from django.db import models

# Create your models here.

JOB_TYPE = (
    ('full time', 'full time'),
    ('part time', 'part time'),
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='jobs/')

    def __str__(self):
        return self.title
     
class category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    