from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class movie_details(models.Model):
    name = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    popularity = models.DecimalField(max_digits = 3, decimal_places=1)
    imdb_score =   models.DecimalField(max_digits = 3, decimal_places=1)
    
	
    def __str__(self):
	return "{'name':'" + self.name + "', 'director':'" + self.director + "'}"

class auth(models.Model):
	user = models.ForeignKey(User,unique=True)
	token = models.CharField(max_length=200)
	session_key =  models.CharField(max_length=200)	    
	
 	
