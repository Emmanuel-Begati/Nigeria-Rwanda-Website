from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path ('', views.home, name='website-home')
, path ('about', views.about, name='website-about'),
 path ('resources', views.resources, name='website-resources')
]
