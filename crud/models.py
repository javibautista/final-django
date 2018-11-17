from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    dni = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname 
        #+ " " + self.dni + " " + self.fecha_nacimiento
"""from django.db import models
        from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        """
