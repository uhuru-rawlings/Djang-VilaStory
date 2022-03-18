from django.shortcuts import render
from profiles.models import Posts
# Create your views here.
def post_view(request):
    try:
        user = request.COOKIES['logedin']
    except:
        return redirect("/")
    users = Signups.objects.filter(useremail = user).first()
    try:
        get_posts = Posts.objects.filter(village = users.village)
    except:
        get_posts = "noposts"
    context = {
        'title':'vilastory | posts',
        'get_posts':get_posts
    }
    return render(request, "posts.html",context)