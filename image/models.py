from django.db import models

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Employee(models.Model):
    POSITION_CHOICE = [ 
        ('internship', 'Internship'),
        ('employee', 'Employee'),
    ]

    name = models.TextField(max_length=50)
    position = models.CharField(choices=POSITION_CHOICE, default='employee', max_length=100)
    photo = models.ImageField(upload_to='employee')

    def __str__(self):
        return self.name
