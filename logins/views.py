from django.shortcuts import render

# Create your views here.
def login_view(request):
    context = {
        'title':'vilastory | login',
    }
    return render(request, "login.html",context)