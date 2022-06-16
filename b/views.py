from django.shortcuts import render, redirect

from .models import *  
from .forms import *    





def one(request):
	tms = Team.objects.all()
	testi = Testimony.objects.all()
	ques = FaQ.objects.all()

	context = {
		'tms': tms,
		'testi':testi,
		'ques': ques,

		'navbar':'home'
	}
	return render(request, 'b/index.html', context)


def Contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successful')
			return redirect('b:cont')

	else:
		form = ContactForm()

	context = {
		'form': form,
		'navbar':'cont'
	}
	
	return render(request, 'b/contact.html', context)


def two(request):
	return render(request, 'b/about.html', {'navbar':'about'})


def RESEARCH(request):
	proj = Res.objects.all()
	context = {
	'proj':proj,
	'navbar': 'res'
	}
	return render(request, 'b/abt.html', context)

def Proj(request, pk):
	pros = Res.objects.get(id=pk)
	res = ResImg.objects.get(pk=pk)
	context = {
		'pros': pros,
		'res':res,
		'navbar': 'res'
	}
	return render(request, 'b/pand-detail.html', context)



# def EmailSub(request):
# 	if request.method == 'POST':
# 		form = ESubForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('b:sub')
# 	else:
# 		form = ESubForm()
# 	context = {
# 		'form': form,
# 	}
# 	return render(request, 'base.html', context)



def mail_letter(request):

	emails = Email_Sub.objects.all()
	df = read_frame(emails, fieldnames = ['email'])
	mail_list = df['email'].values.tolist()
	if request.method == 'POST':
		form = MailForm(request.POST)
		if form.is_valid():
			form.save()
			title = form.cleaned_data.get('title')
			message = form.cleaned_data.get('message')

			send_mail(
				title,
				message,
				'',
				mail_list,
				fail_silently=False
			)
			messages.success(request, 'MESSAGE SUCCESSFULLY SENT TO THE MAIL LIST')
			return redirect('b:mail')

	else:
		form = MailForm()
	context = {
		'form': form
	}
	return render(request, 'b/mail.html', context)



# def blog(request):
# 	bo = Blog.objects.all()
# 	cat = Category.objects.all()
# 	context = {
# 		'bo': bo,
# 		'cat': cat,
#
# 		'navbar': 'blog'
# 	}
# 	return render(request, 'b/blog.html', context)


# def bgDetail(request):
# 	return render (request, 'b/blog-single.html')

# def contact(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.Post)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, 'Successful')
# 			return redirect('b:contact')
#
# 	else:
# 		form = ContactForm()
#
# 	context = {
# 		'form': form,
# 	}
# 	return render(request,'b/contact.html', context)



# def logout1(request):
# 	logout(request)
# 	return redirect("signup")
#
# def search(request):
# 	return render(request, 'b/search.html')
#
# def login1(request):
# 	if request.method == "POST":
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			return redirect("profile")
#
# def signup(request):
# 	if request.method == "POST":
# 		email = request.POST['email']
# 		username = request.POST['username']
# 		fname = request.POST['fname']
# 		lname = request.POST['lname']
# 		password = request.POST['password']
#
# 		a = User.objects.create_user(username, email, password)
# 		a.first_name = fname
# 		a.last_name = lname
# 		a.save()
#
# 		if a:
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				return redirect("login")
# 	return render(request, 'b/signup.html')
#
# def follow_user(request):
# 	return redirect("search")
#
# # UPLOADING POST
#
#
# def uploadpost(request):
# 	return render(request, 'b/c.html')

