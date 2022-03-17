from django.shortcuts import render, redirect

# Create your views here.
def profile_view(request):
    context = {
        'title':'vilastory | profiles',
    }
    return render(request, "posts.html",context)


def logout_view(request):
    return redirect('/')