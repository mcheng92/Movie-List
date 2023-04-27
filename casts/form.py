import re
from django import forms
from .models import Casts

class CastForm(forms.ModelForm):
    
    class Meta:
        model = Casts
        fields = ("character", "image", "actor", "actor_image","actor_age", "deceased", "movie")
        
        
    def clean_character(self):
        character = self.cleaned_data['character']
        #print("Before cleaning:", name)
        character = character.strip() # To remove spaces from the beginning and end of the name
        character = re.sub(r'[^\w\s]', '', character) # To remove special characters from the name
        character = character.lower().title() # To capitalize the first letter of each word
        #print("After cleaning:", name)
        return character
    
    def clean_actor(self):
        actor = self.cleaned_data['actor']
        actor = actor.strip() # To remove spaces from the beginning and end of the name
        actor = re.sub(r'[^\w\s]', '', actor) # To remove special characters from the name
        actor = actor.lower().title() # To capitalize the first letter of each word
        return actor
