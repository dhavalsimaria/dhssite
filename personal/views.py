from django.shortcuts import render
from .forms import ContactForm
import os
from django.http import JsonResponse
from django.http import HttpResponse


firstName = 'DHAVAL' 
lastName = 'SIMARIA'
address = 'PUNE, INDIA'
dob = '3 OCT, 1992'
phone = '+91-968-604-1077'
email = 'DHAVALSIMARIA@YMAIL.COM'
website = 'WWW.IAMCODER.COM'
motto = 'The More I WORKHARD, the More my LUCK FAVORS me.'
form_class = ContactForm()

args = {'firstName_key' : firstName, 'lastName_key' : lastName, 
		'address_key' : address, 'phone_key' : phone, 'email_key' : email, 
		'dob_key' : dob, 'website_key' : website, 'motto_key' : motto, 'form' : form_class}

def index(request):
	template = 'personal/Index-Static-Image-BG.html'
	return render(request, template, args)

def add(request):
		if request.method=='POST' and request.is_ajax():
			form=ContactForm(request.POST)
			if form.is_valid():
				try:
					form.save()

				except Exception as e:
					print ('%s' % str(e))
					msg = 'That\'s embarrassing. Will you please Say Hello again?'
					status = "Error"
					name = ''

				else:
					msg = 'Connected'
					status = "Success"
					name = form.cleaned_data['your_name'];

			print('status %s' % status)
			return JsonResponse({'message':msg, 'status':status, 'welcome_name': name})

def download(request):
	file_path = 'C:/Users/pnlmm075/dhssite/personal/static/personal/cv/DHAVAL_SIMARIA_CV.pdf'
	if os.path.exists(file_path):
		with open(file_path, 'rb') as cv:
			response = HttpResponse(cv.read(), content_type='application/pdf')
			response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
			return response	
	else:
		raise Http404
	