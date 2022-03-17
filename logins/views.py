from django.shortcuts import render

# Create your views here.
def login_view(request):
    errors = ''
    if request.method == 'POST':
        useremails = request.POST['useremail']
        userpassword = request.POST['userpassword']
        try:
            users = Signups.objects.get(useremail=useremails)
            if users.passwords == userpassword:
                response = redirect("/home/")
                response.create_cookie("logedin", useremails)
                return response
            else:
                errors = 'Wrong password please try again'
                return redirect("/")
        except:
            errors = "user dont exist, please try gain"
    context = {
        'title':'vilastory | login',
        'errors':errors
    }
    return render(request, "login.html",context)

def login_meth(request):
   pass