from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path ('', views.home, name='website-home')
, path ('about', views.home, name='website-about'),
path ('contact-us', views.home, name='website-contact'),
path ('login', views.home, name='website-login'),
path ('sign-up', views.home, name='website-sign-up')
]
