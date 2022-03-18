from django.shortcuts import render
from profiles.models import Posts
from signups.models import Signups

# Create your views here.
def post_view(request):
    try:
        user = request.COOKIES['logedin']
    except:
        return redirect("/")
    users = Signups.objects.filter(useremail = user).first()
    try:
        get_posts = Posts.objects.filter(post_village = users.village)
    except:
        get_posts = "noposts"
    context = {
        'title':'vilastory | posts',
        'get_posts':get_posts,
    }
    return render(request, "posts.html",context)

def addinfo_view(request):
    if request.method == 'POST':
        try:
            user = request.COOKIES['logedin']
        except:
            return redirect("/")
        users = Signups.objects.filter(useremail = user).first()
        nearhosp = request.POST['nearhosp']
        nearpolice = request.POST['nearpolice']
        shopingcent = request.POST['shopingcent']
        try:
            pass
        except:
            pass
    return redirect("/home/")