from django import forms

class MessageForm(forms.Form):
        user = forms.CharField(max_length=50, required=True)
        subject = forms.CharField(max_length=100, required=True)
      
      
 