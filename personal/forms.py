#from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ('your_name', 'your_email', 'your_subject', 'your_comment')
		widgets = {
			'your_name' : TextInput(attrs={'placeholder': 'Name *', 'class': 'form-control'}),
			'your_email' : EmailInput(attrs={'placeholder': 'Email *', 'class': 'form-control'}),
			'your_subject' : TextInput(attrs={'placeholder': 'Subject *', 'class': 'form-control'}),
			'your_comment' : Textarea(attrs={'placeholder': 'Comment *', 'class': 'form-control'}),
		}
