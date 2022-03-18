from django.shortcuts import render, redirect
from signups.models import Signups
from profiles.models import Villages
# Create your views here.
def signup_view(request):
    villages = Villages.objects.all()
    context = {
        'title':'vilastory | signup',
        'villages':villages,
    }
    return render(request, "signup.html",context)

def signup_meth(request):
    if request.method == 'POST':
        useremails = request.POST['useremail']
        phonenumber = request.POST['phonenumber']
        uservillage = request.POST['userimages']
        userpassword = request.POST['userpassword']
        try:
            # check if username exists
            users = Signups.objects.get(useremail=useremails)
            errors = 'user with this email already exist, please try login in.'
            return redirect('/signup/')
        except:
            new_user = Signups(useremail = useremails, phone = phonenumber, village = uservillage, passwords = userpassword)
            new_user.save()
            return redirect('/')