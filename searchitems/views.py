from django.shortcuts import render
from posts.models import ImportantInfo
from signups.models import Signups
# Create your views here.
def searchitems_view(request):
    try:
        user = request.COOKIES['logedin']
    except:
        return redirect("/")
    users = Signups.objects.filter(useremail = user).first()
    if request.method == 'POST':
        # details = ''
        # allsearch = ''
        searchitem = request.POST['searchitems']
        try:
            details = ImportantInfo.objects.filter(market= searchitem)
        except:
            details = 'nodetails'
        try:
            allsearch = ImportantInfo.objects.filter(village = users.village)
        except:
            allsearch = 'nodata'

        context = {
            'title': 'search for' + searchitem,
            'searchitem':searchitem,
            'details':details,
            'allsearch':allsearch
        }
        return render(request, "businesse.html", context)
