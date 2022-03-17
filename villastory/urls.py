from django.contrib import admin
from django.urls import path
from signups.views import signup_view
from logins.views import login_view
from profiles.views import profile_view,logout_view
from posts.views import post_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name="login"),
    path('signup/',signup_view, name="signup"),
    path('home/',post_view, name="homepage"),
    path('profile/',profile_view, name="profile"),
    path('logout/',logout_view, name="logout"),
   
]
