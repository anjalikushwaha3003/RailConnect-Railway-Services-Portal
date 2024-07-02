from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
import json
import requests

from django.conf import settings
def confirm(request):
    return render(request,'user/confirm.html')
def login_acc(request):
    return render(request,'user/login_acc.html')
def tickets(request):
     
    tickets = Booking.objects.all()
    return render(request,"user/tickets.html",{'tickets': tickets})
    


def payment_view(request):
    context = {
        'settings': settings
    }
    return render(request, 'user/payment.html', context)
def index(request):
    return render(request, 'user/home.html')
def privacy(request):
    return render(request,'user/privacy.html')

def book(request):
    selected_option = None

    if request.method == 'POST':
        selected_option = request.POST.get('option', None)

    return render(request, 'user/trains.html', {'selected_option': selected_option})
def trainbwst(request):
    if request.method == 'POST':
        from_station=request.POST.get('from')
        to_station=request.POST.get('to')
        date_of_journey = request.POST.get('date')
        

        url = "https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations"

        querystring = {"fromStationCode":from_station,"toStationCode":to_station,"dateOfJourney":date_of_journey}

        headers = {
	"X-RapidAPI-Key": "5dfdaa8a4dmsh3ded44899cc7367p10c40djsn9fd956bd7e08",
	"X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            api_data = response.json()
            train_data = api_data.get('data', [])
            

            return render(request, 'user/trains.html', {'train_data': train_data})

    return render(request, 'user/trains.html')

def myprofile(request):
    
    return render(request,'user/myprofile.html')
def viewprofile(request):
    user = request.session.get('email')
    rdata = ""
    if request.method == 'POST':
        name = request.POST.get("name")
        mobile = request.POST.get("mob")
        password = request.POST.get("password")
        

        add = request.POST.get("address")
        register(name=name, email=user, mobile=mobile, address=add,
                 password=password).save()
        return HttpResponse("<script>location.href='/user/myprofile'</scrip t>")
    if user:
        rdata = register.objects.filter(email=user)
    md = {
        "rdata": rdata
    }
    return render(request, 'user/viewprofile.html', md)


def terms(request):
    return render(request,'user/terms.html')

def livestatus(request):
    if request.method == 'POST':
        train_number = request.POST.get('trainNumber')
        day = request.POST.get('day')

        
        url = "https://irctc1.p.rapidapi.com/api/v1/liveTrainStatus"
        querystring = {"trainNo": train_number, "startDay": day}

        
        headers = {
            "X-RapidAPI-Key": "5dfdaa8a4dmsh3ded44899cc7367p10c40djsn9fd956bd7e08",
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }

        try:
            
            response = requests.get(url, headers=headers, params=querystring)

            
            if response.status_code == 200:
                
                train_status_data = response.json()

                
                if train_status_data.get('status', False) and train_status_data.get('data'):
                    train_data = train_status_data['data']
                    context = {
                        'train_name': train_data.get('train_name'),
                        'source_station': train_data.get('source'),
                        'destination_station': train_data.get('destination'),
                        'run_days': train_data.get('run_days'),
                        'delay': train_data.get('delay'),
                        'std': train_data.get('std'),
                        'new_message': train_data.get('new_message'),
                        'current_station_name': train_data.get('current_station_name'),
                        'eta': train_data.get('eta'),
                        'etd': train_data.get('etd'),
                        'status_as_of':train_data.get('status_as_of')
                    }

                    
                    return render(request, 'user/livestatus.html', context)
                else:
                    
                    pass
            else:
                
                pass

        except requests.exceptions.RequestException as e:
  
            pass

    
    return render(request, 'user/livestatus.html')
    
def pnr(request):
    if request.method == 'POST':
        pnr_number = request.POST.get('pnr_number')
        
        
        url = f"https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/{pnr_number}"
        headers = {
            "X-RapidAPI-Key": "b5ed445cbcmshed00c1321045a3ap145388jsn9b9846331793",
            "X-RapidAPI-Host": "pnr-status-indian-railway.p.rapidapi.com"
        }

        
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            
            return render(request, 'user/pnr.html', {'pnr_data': data})
        else:
            
            return render(request, 'user/pnr.html', {'error': 'Failed to fetch PNR data'})

    
    return render(request, 'user/pnr.html')

def ticketbooking(request):
    return render(request,"user/ticketbooking.html")

def aboutus(request):
    return render(request,"user/aboutus.html")

def seatavailability(request):
    if request.method == 'POST':
        from_station = request.POST.get('from_station')
        to_station = request.POST.get('to_station')
        date = request.POST.get('date')
        train_number = request.POST.get('train_number')
        trainClass = request.POST.get('trainClass')
        
        rapidapi_key = "5dfdaa8a4dmsh3ded44899cc7367p10c40djsn9fd956bd7e08"
        
        
        # API request parameters
        url = "https://irctc1.p.rapidapi.com/api/v1/checkSeatAvailability"
        headers = {
            'X-RapidAPI-Key': rapidapi_key,
            'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
        }
            
            
        
        querystring = {
            "classType": trainClass ,
            "fromStationCode": from_station,
            "quota": "GN",
            "toStationCode": to_station,
            "trainNo": train_number,
            "date": date
        }

        # Make API request
        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            availability_data = response.json()
        else:
            availability_data = None

        return render(request, 'user/seatavailability.html', {"availability_data": availability_data})
    

    return render(request, 'user/seatavailability.html')


def home2(request):
    return(request,"user/home2.html")

    
    
def feedback_user(request):
    if request.method == 'POST':
    
        rating = request.POST.get('rating')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        
        # Check if required fields are not empty
        if rating is not None and name and email and mobile and message:
            
                # Convert 'rating' to integer-
            
                
            # Create a new Feedback instance and save it
            feedback_instance = feedback(
                    Rating=rating,
                    Name=name,
                    Email=email,
                    Mobile=mobile,
                    Message=message
                ).save()
        
            

    return render(request, 'user/feedback.html')  
    
    

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')  
        password = request.POST.get('password')
        x = register.objects.filter(email=email, password=password)
        if x.count() == 1:

            request.session['user'] = email
            request.session['userpic'] = str(x[0].profile)
            request.session['username'] = str(x[0].name)
            user=request.session.get('user')
            
            
            return HttpResponse("<script>location.href='/user/login/'</script>")
        else:
            return HttpResponse("<script>location.href='/user/login/'</script>")

    return render(request,'user/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        profile = request.FILES['profile']
        add = request.POST.get("address")
        x = register.objects.all().filter(email=email).count()
        if x == 1:
            return HttpResponse("<script>location.href='/user/registered'</script>")
        else:
            register(name=name, mobile=mobile, email=email,
                     password=password, address=add, profile=profile).save()
            return HttpResponse("<script> location.href='/user/successreg'</script>")
    return render(request, 'user/signup.html')


def successreg(request):

    return render(request, 'user/successreg.html')


def already(request):

    return render(request, 'user/already.html')

def signout(request):
    if request.session.get('user'):
        del request.session['user']
        del request.session['userpic']
        return HttpResponse("<script>location.href='/user/login'</script>")
    return render(request, 'user/login.html')


def thank(request):
    return render(request, 'user/thankcon.html')

 
def ft(request):
    return render(request,'user/ft_livestation.html')

def contact(request):
    if (request.method == "POST"):
        a1 = request.POST.get('query')
        a2 = request.POST.get('name')
        a3 = request.POST.get('email')
        a4 = request.POST.get('mobile')
        a5 = request.POST.get('message')
        X = contactus(Query=a1, Name=a2, Email=a3,
                      Mobile=a4, Message=a5).save()
        return (HttpResponse("<script> location.href='/user/thank'</script>"))

    return render(request, 'user/contactus.html')
def stationcodes(request):
    
    return render(request, 'user/stationcodes.html')


def booking_success(request):
    return render(request,'user/Booked.html')

def book_ticket(request):
    
    if request.method == 'POST':
    
        train_number = request.POST.get('train_number')
        class_type=request.POST.get('class_type')
        station_from=request.POST.get('station_from')
        station_to=request.POST.get('station_to')
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        date=request.POST.get('date')
        print(train_number,class_type,station_from,station_to,name,gender,age)
        Booking(train_number=train_number,class_type=class_type,station_from=station_from,station_to=station_to,name=name,age=age, gender=gender,date=date).save()
        return redirect('https://rzp.io/l/G9ALoJXcO')

def delete_ticket(request, pnr):
    ticket = Booking.objects.get(pnr=pnr)
    ticket.delete()
    return render(request,'user/cancelled.html')
    
   