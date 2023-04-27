from django.db import models 

# Commented out as code starts to break
#class Director(models.Model):
#    name = models.CharField(max_length=255)
#    
#    def __str__(self):
#       return self.name

class Movie(models.Model):    
    name = models.CharField(max_length=255)    
    image = models.CharField(max_length=255)    
    genres = models.TextField() 
    number_Of_Films = models.IntegerField()    
    characters = models.CharField(max_length=255) 
    actor = models.CharField(max_length=255)   
    deceased = models.BooleanField(default=False)
    #director = models.OneToOneField(Director, on_delete=models.CASCADE, related_name='movie') # Commented out as code starts to break
        
    def __str__(self):
        return self.name[:50]