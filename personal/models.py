from django.db import models

# Create your models here.
class Contact(models.Model):
	your_name = models.CharField(max_length=100) 
	your_email = models.EmailField()
	your_subject = models.CharField(max_length=100)
	your_comment = models.TextField(max_length=200)
	posted_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.your_name

	
	#posted_on = models.DateTimeField(default=timezone.now)