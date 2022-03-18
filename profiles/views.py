from django.shortcuts import render, redirect
from signups.models import Signups
from .models import Profiles,Posts
# Create your views here.
def profile_view(request):
    try:
        user = request.COOKIES['logedin']
    except:
        return redirect("/")
    users = Signups.objects.filter(useremail = user).first()

    context = {
        'title':'vilastory | profiles',
        'users':users
    }
    return render(request, "profiles.html",context)

def savebio_view(request):
    if request.method == 'POST':
        userimages = request.FILES['userimage']
        biotext = request.POST['userimage']

        user = request.COOKIES['logedin']
        get_user = Signups.objects.get(useremail= user)
        exist_page = Profiles.objects.filter(users = get_user).exists()
        if exist_page:
             about_me = Profiles.objects.get(users = get_user)
             about_me.userimages = userimages
             about_me.aboutme = biotext
             about_me.save()
        else:
            about_me = Profiles(users=get_user,userimage = userimages, aboutme=biotext)
            about_me.save()

    return redirect('/')


def logout_view(request):
    try:
        user = request.COOKIES['logedin']
        respose = redirect("/")
        respose.delete_cookie("logedin")
    except:
        return redirect("/")
    return redirect('/')