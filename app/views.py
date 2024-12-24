from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.models import pcards
from app.models import productViewer as productViewer1
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout,authenticate
from django.contrib.auth import login as auth_login
from.forms import CreateUserForm,LoginForm
from .models import Profile,Cart,CartItem,Address
from django.contrib.auth.models import auth   
from .forms import Profileform
from django.shortcuts import get_object_or_404
from sbm.utils import get_location_details
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib import messages
from sbm.utils import generate_otp
import requests
from django.core.cache import cache
from django.contrib import messages


def home(request):
    pcardsdata=pcards.objects.all()
    cartitems = None  # Initialize cartitems at the beginning
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            cart=get_object_or_404(Cart,user=request.user)
            cartitems = CartItem.objects.filter(cart=cart)
        except Profile.DoesNotExist:
           profile = None 
        except Cart.DoesNotExist:
            cart = None
            cartitems=None
    else :
        profile=None
        
    
    return render(request,'index.html',{"pcardsdata":pcardsdata,"u":profile,'cartitems':cartitems})
def productViewer(request,id):
    productViewerdata=productViewer1.objects.get(product_id=id)
    pcardsdata=pcards.objects.get(product_id=id)
    data={
        'productViewerdata':productViewerdata,
        'pcardsdata':pcardsdata
    }
    return render(request,'productViewer.html',data)


def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        profile_form = Profileform(request.POST)

        if form.is_valid() and profile_form.is_valid():
            # Save form data temporarily
            user = form.save(commit=False)  # Create user instance without saving
            user.set_password(form.cleaned_data['password1'])  # Set the password
            request.session['signup_form'] = form.cleaned_data
            
            email = form.cleaned_data.get('email')
            otp_code = generate_otp()
            request.session['otp'] = otp_code
            request.session['email'] = email
            
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp_code}',
                'your_email@gmail.com',  # From email
                [email],  # To email
                fail_silently=False,
            )
            messages.success(request, f"OTP has been sent to {email}")
            
            # Save the profile data temporarily
            request.session['profile_form'] = profile_form.cleaned_data
            
            return redirect('otp_verify')
    else:
        form = CreateUserForm()
        profile_form = Profileform()
        
    
        
    return render(request, "registration/signup.html", {"registerform": form, "profile_form": profile_form})


# views.py
def otp_verify(request):
    if request.method == "POST":
        input_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')
        form_data = request.session.get('signup_form')
        email = request.session.get('email')
        profile_data = request.session.get('profile_form')
        
        if input_otp == session_otp:
            # OTP is correct, create user and log in
            if form_data:
                form_data['email'] = email 
                form = CreateUserForm(form_data)
                
                if form.is_valid():
                    user = form.save()
                    username = user.username
                    
                    # Create Profile
                    profile_form = Profileform(profile_data)
                    if profile_form.is_valid():
                        profile = profile_form.save(commit=False)
                        profile.user = user
                        profile.username=username
                        profile.save()
                        
                    auth_login(request, user)  # Use Django's login function
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    messages.success(request, "Registration successful!")
                    
                    return redirect('home')
                else:
                    messages.error(request, "Error in form")
            else:
                messages.error(request, "No form data found in session")
        else:
            messages.error(request, "Invalid OTP")
    
    return render(request, "registration/otp_verify.html")

def login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            

            username=request.POST.get('username')
            password=request.POST.get('password')
            user= authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            
    context={'loginform':form}        
    return render(request,"registration/login.html",context=context)

def logout_view(request):
    
    logout(request)

    return redirect('home')

@login_required
def addtocart(request,product_id):
    product=get_object_or_404(pcards,product_id=product_id)
    cart,created=Cart.objects.get_or_create(user=request.user)
    cartitem,created=CartItem.objects.get_or_create(cart=cart,product=product)

    if not created:
        cartitem.quantity+=1
    
    else:
        cartitem.quantity=1
    cartitem.save()
    return redirect('home')
@login_required  
def viewcart(request):
    bill=0
    if request.user.is_authenticated:
        cart=get_object_or_404(Cart,user=request.user)
        cartitems = CartItem.objects.filter(cart=cart)
        for item in cartitems:
            bill += int(item.product.pcardcost) * item.quantity
    else:
        cart=None
        cartitems=None
    return render(request, 'viewcart.html', {'cart': cart, 'cart_items': cartitems,'bill':bill})

def delete_from_cart(request,id):
    cart=get_object_or_404(Cart,user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=id)
    cart_item.delete()
    messages.success(request, "Item successfully removed from the cart.")
    
   
    
    return redirect('viewcart')

def AddressView(request):
    addresses=None
    if request.user.is_authenticated:
        addresses=Address.objects.filter(user=request.user)
    if request.user.is_authenticated:
        if request.method == 'POST':
            name_add = request.POST.get('name')
            phone_add = request.POST.get('a_mobile')
            pincode = request.POST.get('pincode')
            city = request.POST.get('city')
            state = request.POST.get('state')
            house_no = request.POST.get('house_no')
            area = request.POST.get('area')
            landmark = request.POST.get('landmark')

        
            address = Address(
                user=request.user, 
                name=name_add,
                a_mobile=phone_add,
                pincode=pincode,
                city=city,
                state=state,
                house_no=house_no,  
                area=area,
                landmark=landmark
            )
            address.save()
            return redirect('home')
        
    return render(request, 'checkoutpage.html',{"addresses":addresses})
# views.py'''



def get_city_state(request):
    pincode = request.GET.get('pincode')
    
    if pincode and len(pincode) == 6:  # Ensure valid pincode length
        # Replace with your desired external API
        api_url = f"http://www.postalpincode.in/api/pincode/{pincode}"
        response = requests.get(api_url)
        data = response.json()
        
        if data['Status'] == 'Success':
            city = data['PostOffice'][0]['District']
            state = data['PostOffice'][0]['State']
            return JsonResponse({'city': city, 'state': state})
        else:
            return JsonResponse({'error': 'Invalid pincode'}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
