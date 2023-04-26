from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path ('', views.home, name='website-home')
, path ('about', views.about, name='website-about'),
path ('contact-us', views.contact, name='website-contact'),
path('login/', views.login, name='website-login'),
path ('sign_up', views.sign_up, name='website-sign_up')
]
