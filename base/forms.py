from django.forms import ModelForm 
from .models import Room, Message, Profile



class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']

class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        fields = ['avatar','job_title','location','bio']