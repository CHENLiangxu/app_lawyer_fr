from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=30)
    pernom = models.CharField(max_length=30)
    telephone_fix = models.CharField(max_length=16, null=True)
    telephone_protable = models.CharField(max_length=16)
    adress = models.CharField(max_length=200)
    pays = models.CharField(max_length=30)
    ville = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    # civilite : 0 monsieur; 1 madame 2 mademoiselle; 
    civilite = models.IntegerField()
    date_naissance = models.DateField()
    date_rdv = models.DateTimeField(null=True)
    mail = models.CharField(max_length=200)
    mail_invite = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    #client -> client_2
    client_2 = models.OneToOneField("self", on_delete=models.SET_NULL, null=True)

class Lower(models.Model):
    nom = models.CharField(max_length=30)
    pernom = models.CharField(max_length=30)
    telephone_protable = models.CharField(max_length=16)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    #avocat <-> client
    mon_client = models.ManyToManyField(Client)

class Appointment(models.Model):
    target_user = models.ForeignKey("TargetUser")
    lawyer = models.ForeignKey("lower")
    date_rdv = models.DateTimeField(max_length=200)

class TargetUser(models.Model):
    user= models.OneToOneField(User)
    telephone_fix = models.CharField(max_length=16, null=True)
    telephone_protable = models.CharField(max_length=16)
    adress = models.CharField(max_length=200, null=True)
    pays = models.CharField(max_length=30, null=True)
    ville = models.CharField(max_length=50, null=True)
    code_postal = models.CharField(max_length=10, null=True)
    # civilite : 0 monsieur; 1 madame 2 mademoiselle; 
    civilite = models.IntegerField()
    date_naissance = models.DateField()
    date_rdv = models.DateTimeField(null=True)
    mail_invite = models.CharField(max_length=200, null=True)
    #client -> client_2
    client_2 = models.OneToOneField("self", on_delete=models.SET_NULL, null=True)
