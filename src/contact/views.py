from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


from .forms import contactForm

# Create your views here.
def contact(request):
	title = 'Contact'
	form = contactForm(request.POST or None)
	context = {'title':title, 'form':form,}

	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = 'Message from MYSITE.com'
		message = '%s %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		fail_silently=True
		send_mail = (subject, message, emailFrom, emailTo, fail_silently)

	template = 'contact.html'
	return render(request,template,context)