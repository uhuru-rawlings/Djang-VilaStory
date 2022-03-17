from django.shortcuts import render

# Create your views here.
def post_view(request):
    context = {
        'title':'vilastory | posts',
    }
    return render(request, "posts.html",context)