import re
from django import forms 
from .models import Movie

class MovieForm(forms.ModelForm):   
    
    class Meta: 
        model = Movie       
        fields = ('name', 
                  'image', 
                  'genres', 
                  'number_Of_Films'
        )
        exclude = ('characters', 'deceased', 'actor')
        
    def clean_name(self):
        name = self.cleaned_data['name']
        #print("Before cleaning:", name)
        name = name.strip() # To remove spaces from the beginning and end of the name
        name = re.sub(r'[^\w\s]', '', name) # To remove special characters from the name 
        name = name.lower().title() # To capitalize the first letter of each word
        #print("After cleaning:", name)
        return name
    
    def clean_genres(self):
        genres = self.cleaned_data['genres']
        genres= genres.strip() # To remove spaces from the beginning and end of the name
        genres = re.sub(r'[^\w\s]', '', genres) # To remove special characters from the name 
        genres = genres.lower().title() # To capitalize the first letter of each word
        return genres
    
# Commented out as code starts to break    
#class DirectorForm(forms.ModelForm):
#    class Meta:
#        model = Director
#        fields = ("name",)