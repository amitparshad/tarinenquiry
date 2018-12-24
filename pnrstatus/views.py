from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
#from . forms import Namepnr


def pnrstatus(request):


    url = "https://api.railwayapi.com/v2/pnr-status/pnr/{}/apikey/4bv5ozzira/"
    #pnrno = '2516775996'
    #pnrno = request.POST['pnrno']
    pnrno = request.POST.get('abc')
    r = requests.get(url.format(pnrno)).json()

    #if(r['train']['name'] == 'null'):
     #   raise Http404
     #   return render_to_response('pnrstatus.html')


    pnr_status = {
        'pnr' : r['pnr'],
        'train_name': r['train']['name'],
        'train_number': r['train']['number'],
        'chart_prepared' : r['chart_prepared'],
        'from_station' : r['from_station']['name'],
        'f_code' : r['from_station']['code'],
        'to_station' : r['to_station']['name'],
        't_code' : r['to_station']['code'],
        'res_upto' : r['reservation_upto']['name'],
        'journney_class': r['journey_class']['code'],
        'booking_status': r['passengers'][0]['booking_status'],
        'current_status' : r['passengers'][0]['current_status'],
        'total_passengers' : r['total_passengers'],
        'doj' : r['doj'],
        'boarding_point':r['boarding_point']['name'],
     }


    print(pnr_status)
    context = {'pnr_status' : pnr_status}
    return render(request, "pnrstatus.html", context)
# Create your views here.
