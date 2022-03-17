from django.shortcuts import render
from signups.models import Signups
# Create your views here.
def signup_view(request):
    context = {
        'title':'vilastory | signup',
    }
    return render(request, "signup.html",context)

def signup_meth(request):
    if request.method == 'POST':
        useremails = request.POST['useremail']
        phonenumber = request.POST['phonenumber']
        uservillage = request.POST['userimages']
        userpassword = request.POST['userpassword']
        useremails = request.POST['useremail']