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
    bios = ''
    try:
        bios = Profiles.objects.get(users = users)
    except:
        bios = "nobios"
    context = {
        'title':'vilastory | profiles',
        'users':users,
        'bios':bios
    }
    return render(request, "profiles.html",context)

def savebio_view(request):
    if request.method == 'POST':
        userimages = request.FILES['userimage']
        biotext = request.POST['biotext']

        user = request.COOKIES['logedin']
        get_user = Signups.objects.get(useremail= user)
        exist_page = Profiles.objects.filter(users = get_user).exists()
        if exist_page:
             about_me = Profiles.objects.get(users = get_user)
             about_me.userimages = userimages
             about_me.aboutme = biotext
             about_me.save()
        else:
            about_me = Profiles(users=get_user,userimages = userimages, aboutme=biotext)
            about_me.save()

    return redirect('/profile/')


def addpost_view(request):
        if request.method == 'POST':
            poststext = request.POST['poststext']
            user = request.COOKIES['logedin']
            get_user = Signups.objects.get(useremail= user)
            new_posts = Posts(postby=get_user, post_text=poststext,post_village=get_user.village)
            new_posts.save()
            return redirect("/home/")

def addpostimages_view(request):
        if request.method == 'POST':
            postsimages = request.FILES['postsimages']
            captionposts = request.POST['captionposts']
            user = request.COOKIES['logedin']
            get_user = Signups.objects.get(useremail= user)
            new_posts = Posts(postby=get_user,post_image = postsimages, post_text=captionposts, post_village=get_user.village)
            new_posts.save()
            return redirect("/home/")

def logout_view(request):
        user = request.COOKIES['logedin']
        response = redirect("/")
        response.delete_cookie("logedin")
        return response