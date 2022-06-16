from django.urls import path
from . import views


app_name = 'b'

urlpatterns = [
    path('', views.one, name='home'),
    path('about-me/', views.two, name='about'),
    # path('register/', views.registerUser, name='register'),
    # path('Wole/', views.index, name='login'),
    # path('My-Home/', views.dash, name='dashboard'),
    path('Contact', views.Contact, name='cont'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='b/logout.html'), name='logout'),
    # path('post', views.feed, name='feed'),
    # path('mowapelu/<username>/', views.telemi, name='follow'),
    # path('miowapelu/<username>/', views.matelemi, name='unfollow'),
    # path('profile/<username>/', views.profile,name='profile'),
    # path('post/<username>/', views.post,name='post'),
    # path('comment/<username>/<post_id>/', views.comment,name = 'comment'),
    # path('welcome/',views.welcome,name='welcome'),
    # path('search/', views.search, name='search'),
    path('pandemic', views.RESEARCH, name='res'),
    path('pandemic/<int:pk>/', views.Proj, name='pandemic'),
    # path('profile/', views.profile, name='profile'),
    # path('YOU-HAVE-SUBSCRIBE', views.EmailSub, name='sub'),
    path('SEND-MAIL', views.mail_letter, name='mail'),
    # path('profile-upload', views.profile_upload, name='profile-upload'),
    # path('search-me', views.search, name='search'),

    
]