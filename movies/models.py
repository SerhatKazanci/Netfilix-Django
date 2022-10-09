from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Kategori(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Sub_category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Kategori2(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Movie(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    sub_category = models.ManyToManyField('Sub_category')
    onetoone = models.OneToOneField(Kategori2, on_delete=models.CASCADE, null=True)
    isim = models.CharField(max_length=100)
    resim = models.FileField(upload_to='movies', null=True, blank=True, verbose_name='Film Resmi')

    def __str__(self):
        return self.isim
class Izlenenler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    izlenen = models.ManyToManyField('Movie')
    
    def __str__(self):
        return self.user.username