from django.shortcuts import render, redirect
from signups.models import Signups
# Create your views here.
def profile_view(request):
    try:
        user = request.COOKIES['logedin']
    except:
        return redirect("/")
    users = Signups.objects.filter(useremail = user).first()
    print("###########################")
    print(users.id)
    print("###########################")
    context = {
        'title':'vilastory | profiles',
        'users':users
    }
    return render(request, "profiles.html",context)


def logout_view(request):
    return redirect('/')