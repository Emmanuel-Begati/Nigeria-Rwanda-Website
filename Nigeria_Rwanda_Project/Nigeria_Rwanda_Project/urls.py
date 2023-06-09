"""
URL configuration for Nigeria_Rwanda_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from users import views as users_views
from django.contrib.auth import views as auth_views
from contact_form.views import contact_view 
from newsletter.views import subscribe as newsletter_views
from newsletter.views import check_email 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', users_views.sign_up, name='website-sign_up'),
     path('profile/', users_views.profile, name='website-profile'),
    path('', include('website.urls' )),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='website-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='website-logout'),
    path('contact-us/', contact_view, name='website-contact'),
    path('subscribe/', newsletter_views, name='newsletter_signup'),
    path('check_email/', check_email, name='check_email')

]
