from django import forms
from .models import Email_Sub, Mailer, Team, Contact, Profile, Post, Comment
from django.contrib.auth.models import User






class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=256, help_text='Required Field')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=256, help_text='Required Field')

    class Meta:
        model = User
        fields = ['email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['status_info', 'profile_pic']


class CreatePost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_text', 'post_pic']

class CreateComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_text']


class ESubForm(forms.ModelForm):
    class Meta:
        model = Email_Sub
        fields = ['email',]


class MailForm(forms.ModelForm):
    class Meta:
        model = Mailer
        fields = '__all__'
        
        
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email',  'message']


    name = forms.CharField(widget=forms.Textarea(attrs={
        'rows':'1',
        'class':'form-group',
        'id':'name',
        'placeholder':'Your Name',

    }))
    email = forms.CharField(widget=forms.Textarea(attrs={
        'rows':'1',
        'class':'form-group',
        'id':'email',
        'placeholder':'Your Email'
    }))
    # subject = forms.CharField(widget=forms.Textarea(attrs={
    #     'rows':'1',
    #     'class':'form-group',
    #     'id':'subject',
    #     'placeholder':'Topic'
    # }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows':'7',
        'class':'form-group',
        'id':'message',
        'placeholder':'Your Message'
    }))


    labels = {

        'name': '',
        'email': '',
        # 'subject': '',
        'message': ''
    }







