from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User



class Res(models.Model):
    title = models.CharField(max_length=222)
    img = models.ImageField(upload_to='Recources')
    url = models.URLField(default=None, blank=True, null=True)
    note = RichTextField()


    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'RESOURCES'

class ResImg(models.Model):
    # title = models.CharField(max_length=345)
    img = models.ImageField(upload_to='PANDEMIC/Recources', blank=True)
    img1 = models.ImageField(upload_to='PANDEMIC/Recources', blank=True)
    img2 = models.ImageField(upload_to='PANDEMIC/Recources', blank=True)
    img3 = models.ImageField(upload_to='PANDEMIC/Recources', blank=True)
    res = models.ForeignKey(Res, on_delete=models.CASCADE)


    def __str__(self):
        return f"Onaga"

    class Meta:
        verbose_name_plural = 'RESOURCES IMAGES'



class Testimony(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=66)
    img = models.ImageField(upload_to='Testimony/img', blank=True)
    text = models.TextField()

    def __str__(self):
        return self.name


class FaQ(models.Model):
    question = models.CharField(max_length=222)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField()
    designation = models.CharField(max_length=250)
    twitter = models.URLField(null=True)
    facebook = models.URLField(null=True)
    instagram = models.URLField(null=True)
    linkedin = models.URLField(null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Email_Sub(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Mailer(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'CATEGORY'

    def __str__(self):
        return self.title
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.FileField(default='img/sm/1.png', upload_to='profile')
    status_info = models.CharField(default='Enter Bio', max_length=1000)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post_text = models.CharField(max_length=2000)
    post_pic = models.FileField(default='img/sm/2.jpeg', upload_to='post')

    def __str__(self):
        return self.user.username


class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    following_user = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.following_user.username

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    follower_user = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.follower_user.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment_text = models.CharField(default='', max_length=2000)




# class Blog(models.Model):
#     img = models.ImageField(upload_to='Blog/Pics')
#     cat = models.ForeignKey(Category, on_delete=models.CASCADE)
#     title = models.CharField(max_length=450)
#     name = models.CharField(max_length=222)
#     sub_text = models.TextField(blank=True)
#     date = models.DateField(auto_now_add=False)
#     content = models.TextField()
# 
#     def __str__(self):
#         return self.title

