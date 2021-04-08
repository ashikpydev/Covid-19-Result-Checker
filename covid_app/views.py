from django.shortcuts import render,render
import json
import requests

url = "https://covid-193.p.rapidapi.com/statistics"


headers = {
    'x-rapidapi-key': "d9cbda2f6dmshc2bba4bd0e71c1ap1ab42fjsnc01c43dd2e87",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()



# Create your views here.
def home(request):
    noofresults = int(response['results'])
    mylist= []
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method == 'POST':
        selectedcountry = request.POST["selectedcountry"]
        noofresults = int(response['results'])
        for x in range(0,noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total)- int(active) - int(recovered)

        context = {'selectedcountry':selectedcountry, 'mylist':mylist, 'new':new, 'active':active, 'critical':critical, 'recovered':recovered, 'total':total, 'deaths':deaths}
        return render(request, 'covid.html', context)
                

    noofresults = int(response['results'])
    mylist= []
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    context = {'mylist':mylist}
    
    return render(request, 'covid.html', context)