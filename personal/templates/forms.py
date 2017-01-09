from django import forms

class ContactForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100, 
		widgets=forms.TextInput(attrs={'placeholder': 'Name *'}))
	your_email = forms.EmailField(request.post or None, 
		widgets=forms.TextInput(attrs={'placeholder': 'Email *'}))
	your_subject = forms.CharField(label='Your subject', max_length=100,  
		widgets=forms.TextInput(attrs={'placeholder': 'Subject '}))
	your_comment = forms.CharField(label='Your comment', max_lenght=200, 
		widgets=forms.TextArea(attrs={'placeholder': 'Comments *'}))

#required=False,