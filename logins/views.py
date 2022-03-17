from django.shortcuts import render

# Create your views here.
def login_view(request):
    context = {
        'title':'vilastory | login',
    }
    return render(request, "login.html",context)

def login_meth(request):
   if request.method == 'POST':
        useremails = request.POST['useremail']
        phonenumber = request.POST['phonenumber']
        users = Signups.objects.get(useremail=useremails)