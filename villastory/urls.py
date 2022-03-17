from django.contrib import admin
from django.urls import path
from signups.views import signup_view,signup_meth
from logins.views import login_view,login_meth
from profiles.views import profile_view,logout_view
from posts.views import post_view
from django.contrib.staticfiles.urls import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name="login"),
    path('signin',login_meth, name="signin"),
    path('signup/',signup_view, name="signup"),
    path('create_account/',signup_meth, name="create_account"),
    path('home/',post_view, name="homepage"),
    path('profile/',profile_view, name="profile"),
    path('logout/',logout_view, name="logout"),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
