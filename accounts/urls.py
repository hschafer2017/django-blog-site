# ACCOUNTS FOLDER
from django.conf.urls import url
from accounts.views import do_login, register, do_logout, profile  

    
urlpatterns = [
    url(r'^login', do_login, name='login'),    
    url(r'^register$', register, name='register'), 
    url(r'^logout$', do_logout, name='logout'),
    url(r'^profile$', profile, name='profile') 
    ]