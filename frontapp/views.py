#request handler
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from .models import *
from django import forms

# Create your views here. - Request Handlers
#--------------------------------------------------------------------------
#Home Page
#--------------------------------------------------------------------------
def index(request):
    name = ''
    if request.user.is_authenticated:
        name = request.user.get_short_name()
        return render(request, 'index.html', {'name': name}) #variables to templated page
    else:
        return render(request, 'index.html')

#--------------------------------------------------------------------------
#login 
#--------------------------------------------------------------------------
def login_request(request):
    if request.user.is_authenticated:
        logout_request(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username, password= password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Logged in as: {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid ID or password combination")
        else:
            messages.error(request, "Invalid ID or password combination")
    
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

#--------------------------------------------------------------------------
#logout handler
#--------------------------------------------------------------------------
def logout_request(request):
    logout(request)
    messages.info(request, "Log-out Successful ")
    return redirect('/#')

#--------------------------------------------------------------------------
#register
#--------------------------------------------------------------------------
def register_request(request):
    if request.user.is_authenticated:
        msg = "Already logged in!"
        return render(request, "register.html", context={"msg":msg})
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.save()
                login(request, user)
                return redirect('/account')
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])

        form = CreateUserForm()
        return render(request, "register.html", context={"form":form})


#--------------------------------------------------------------------------
# Account type (customer, promoter, venue)
#--------------------------------------------------------------------------
@login_required
def accType_request(request):

    if request.method == "POST":
        #Create a form instance from data in POST
        form = AccounTypeForm(request.POST)
        if form.is_valid():
            # Save a new acctype object from the form's data.
            at = AccountType.objects.get(user = request.user)
            at.accType = form.cleaned_data.get('accType')
            at.save()
            
            return redirect('/')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = AccounTypeForm()
    return render(request, "account.html", context={"form":form})

#--------------------------------------------------------------------------
# Venue Information request handler
#--------------------------------------------------------------------------
@login_required
def venue_req(request):
   
    at = AccountType.objects.get(user= request.user)
    if VenueOwner.objects.filter(user = at).exists():
        ven_instance = VenueOwner.objects.get(user = at)
    if at.accType == "Venue":

        if request.method == "POST":
            form = VenueForm(request.POST)
            if form.is_valid():
                ven = VenueOwner.objects.get_or_create(user = at)
                ven = form.save(commit=False)
                ven.user = at
                ven.save()

                return redirect('/')
                
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])
        
        if VenueOwner.objects.filter(user = at).exists():
            form = VenueForm(instance=ven_instance)
        else:
            form = VenueForm()
        return render(request, "venue.html", context={"form":form})
    else:
        msg = "Not a venue account"
        return render(request, "venue.html", context={"msg":msg})
    

#--------------------------------------------------------------------------
# Promoter Page
#--------------------------------------------------------------------------
@login_required
def pro_req(request):
    
    at = AccountType.objects.get(user= request.user)
    if Promoter.objects.filter(user = at).exists():
        promoter_instance = Promoter.objects.get(user = at)
    if at.accType == "Promoter":

        if request.method == "POST":
            form = PromoterForm(request.POST)
            if form.is_valid():
                promoter = Promoter.objects.get_or_create(user = at)
                promoter = form.save(commit=False)
                promoter.user = at
                promoter.save()

                return redirect('/')
                
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])
        
        if Promoter.objects.filter(user = at).exists():
            form = PromoterForm(instance=promoter_instance)
        else:
            form = PromoterForm()
        return render(request, "promoter.html", context={"form":form})
    else:
        msg = "Not a promoter account"
        return render(request, "promoter.html", context={"msg":msg})

#--------------------------------------------------------------------------    
#create concert/events page
#--------------------------------------------------------------------------
@login_required
def concert_req(request):
   
    accountType = AccountType.objects.get(user= request.user)
    if accountType.accType == "Venue":

        if request.method == "POST":
            form = ConcertForm(request.POST)
            if form.is_valid():
                concert = form.save(commit=False)
                
                vo = VenueOwner.objects.get(user=accountType)
                concert.venueName = vo
                concert.seats_avail1 = vo.seats_capacity1 #initial setup of concert sets available
                concert.seats_avail2 = vo.seats_capacity2
                concert.seats_avail3 = vo.seats_capacity3
                concert.seats_avail4 = vo.seats_capacity4

                concert.save()

                return redirect('/')
                
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])
        
        if VenueOwner.objects.filter(user= accountType).exists():

            form = ConcertForm()
            return render(request, "concert.html", context={"form":form})
        else:
            msg = "Please setup your venue information first"
            return render(request, "concert.html", context={"msg":msg})
    else:
        msg = "Not a venue account"
        return render(request, "concert.html", context={"msg":msg})

#--------------------------------------------------------------------------    
# Browse Concerts
#--------------------------------------------------------------------------

def getData():
    '''Populates return value: "Cards" with Concerts from the DB'''
    concertObj = Concert.objects.all()
    cards = concertObj.values()
#fixed missing venue name in values dictionary
    for card, concert,  in zip(cards, concertObj):
        card.update({'image': "https://t3.ftcdn.net/jpg/04/69/33/98/240_F_469339833_6lmBJ2UqV1UQjZRQETVgMQL5UwWNDGoU.jpg"})
        card.update({'venueName': concert.venueName.__str__() })
    return cards

def browse_req(request):
    
    return render(request, "browse.html", context={"cards": getData()})

#--------------------------------------------------------------------------
# Ticket orders
#--------------------------------------------------------------------------

@login_required
def ticket_req(request, id_):
    #id_ is the concert object id in database
    myAmount = Balance.objects.get(user= request.user).balance
    at = AccountType.objects.get(user= request.user)  
    if at.accType == 'Customer' or at.accType == 'Promoter':
        
        concert = Concert.objects.get(id=id_)
               
        seats = [concert.venueName.seats1]
        seats.append(concert.venueName.seats2)#appends none if doesnt exist for checking later
        seats.append(concert.venueName.seats3)#appends none if doesnt exist for checking later
        seats.append(concert.venueName.seats4)#appends none if doesnt exist for checking later

        price = [concert.venueName.price1]
        if concert.venueName.price2 != 0:
            price.append(concert.venueName.price2)
        if concert.venueName.price3 != 0:
            price.append(concert.venueName.price3)
        if concert.venueName.price4 != 0:
            price.append(concert.venueName.price4)

        seatsAvail = [concert.seats_avail1]
        if concert.venueName.seats2 != None:
            seatsAvail.append(concert.seats_avail2)
        if concert.venueName.seats3 != None:
            seatsAvail.append(concert.seats_avail3)
        if concert.venueName.seats4 != None:
            seatsAvail.append(concert.seats_avail4)


        if request.method == "POST":
            form = TicketOrderForm(request.POST)
            
            if form.is_valid():                
                
                ticket = form.save(commit=False)
                ticket.user = request.user
                ticket.concertName = concert

                if ticket.seat_type == "option1":
                    ticket.seat_type = seats[0]
                    ticket.price = ticket.quantity * price[0]
                elif ticket.seat_type == "option2" and concert.venueName.seats2 != None:
                    ticket.seat_type = seats[1]
                    ticket.price = ticket.quantity * price[1]
                elif ticket.seat_type == "option3" and concert.venueName.seats3 != None:
                    ticket.seat_type = seats[2]
                    ticket.price = ticket.quantity * price[2]
                elif ticket.seat_type == "option4" and concert.venueName.seats4 != None:
                    ticket.seat_type = seats[3]
                    ticket.price = ticket.quantity * price[3]

                #checkout
                bal = Balance.objects.get(user= request.user)

                if (bal.balance - ticket.price >= 0):
                    bal.balance -= ticket.price
                    
                    #update seats left in concert
                    if ticket.seat_type == seats[0]:
                        if (concert.seats_avail1 - ticket.quantity) >= 0:
                            concert.seats_avail1 -= ticket.quantity
                        else:
                            msg = "Unable to complete Transaction: Not enough seats"
                            return render(request, "TicketOrder.html", context={"msg":msg})
                        
                    elif ticket.seat_type == seats[1] and concert.venueName.seats2 != None:
                        if (concert.seats_avail2 - ticket.quantity) >= 0:
                            concert.seats_avail2 -= ticket.quantity
                        else:
                            msg = "Unable to complete Transaction: Not enough seats"
                            return render(request, "TicketOrder.html", context={"msg":msg})
                    
                    elif ticket.seat_type == seats[2] and concert.venueName.seats3 != None:
                        if (concert.seats_avail3 - ticket.quantity) >= 0:
                            concert.seats_avail3 -= ticket.quantity
                        else:
                            msg = "Unable to complete Transaction: Not enough seats"
                            return render(request, "TicketOrder.html", context={"msg":msg})

                    elif ticket.seat_type == seats[3] and concert.venueName.seats4 != None:
                        if (concert.seats_avail4 - ticket.quantity) >= 0:
                            concert.seats_avail4 -= ticket.quantity
                        else:
                            msg = "Unable to complete Transaction: Not enough seats"
                            return render(request, "TicketOrder.html", context={"msg":msg})
                        

                    
                    concert.save()
                    
                    bal.save()
                    ticket.save()
                    return redirect('/mytickets/')
                
                else:
                    msg = "Unable to complete Transaction: User Balance is too low"
                    return render(request, "TicketOrder.html", context={"msg":msg})
    
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])
        

        form = TicketOrderForm()
        return render(request, "TicketOrder.html", context={"form":form, "seats": seats, 'prices': price, 'seatsAvail': seatsAvail, 'bal': myAmount })
    else:
        msg = "Can't buy tickets using a Venue Account"
        return render(request, "TicketOrder.html", context={"msg":msg})

@login_required
def myTicket_req(request):
    #concertObj = Concert.objects.all()
    tickets = TicketOrder.objects.filter(user = request.user)
    concertObj = tickets
    tickets = tickets.values()
    for ticket, concert in zip(tickets, concertObj):
        ticket.update({'concertName': concert.concertName.__str__() })

    return render(request, "mytickets.html", context={"cards":tickets})

@login_required
def my_balance(request):
    
    if request.user.is_authenticated:
        bal = Balance.objects.get(user= request.user).balance
        return render(request, 'balance.html', {'bal': bal}) #variables to templated page
    else:
        return render(request, '/')