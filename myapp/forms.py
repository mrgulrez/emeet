from django import forms

class JoinRoomForm(forms.Form):
    roomID = forms.CharField(label='RoomID', max_length=100)
