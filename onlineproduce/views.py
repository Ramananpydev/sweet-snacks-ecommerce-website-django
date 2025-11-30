from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from onlineproduce.forms import contact,SignupForm, SigninForm
from onlineproduce.models import customer,Login
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
import os



# Create your views here.

def name(request):
    return HttpResponse('Ramanan')

def main(request):
    return render(request,"home.html")

def menu(request):
    return render(request,"product.html")

def address(request):
    return render(request,"contact.html")

def  info(request):
    return render(request,"about.html")

def signin(request):
    return render(request,"signin.html")

def signup(request):
    return render(request,"signup.html")

def payment(request):
    return render(request,"order.html")
    

def complete(request):
    return render(request,"order-success.html")

def new(request):
    return render(request,"home1.html")






def enquiry_form(request):
    if request.method == "POST":
        form = contact(request.POST) 
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            recipient_email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
        
            subject = "THANK YOU FOR ENQUIRY"
            body = f"""
Hi {name},

Thank you for reaching out to us.
Please find attached our brochure with pricing and product details.

Best regards,
The Sweet & Savory Sales Team
"""

            # Create and send email
            email_message = EmailMessage(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
            )

            # Attach brochure if exists
            brochure = os.path.join(settings.BASE_DIR, "static", "menu_card.pdf")
            if os.path.exists(brochure):
                email_message.attach_file(brochure)

            email_message.send(fail_silently=False)

            return render(request, "contact.html", {'f': name, 'success': True})
        else:
            return render(request, "contact.html", {"gmail": form})

    else:
        form = contact()
        return render(request, "contact.html", {"gmail": form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password( form.cleaned_data["password"])
            user.save()
            return redirect("onlineproduce:signin")   
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})


def signin(request):
    msg = ""
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = Login.objects.get(email=email)
                if check_password (password,user.password):
                    request.session["user_id"] = user.id
                    request.session["user_name"] = user.username
                    return redirect("onlineproduce:home1")  
                else:
                    msg = "Invalid Password"
            except Login.DoesNotExist:
                msg = "User does not exist"
    else:
        form = SigninForm()

    return render(request, "signin.html", {"form": form, "msg": msg})




def profile(request):
    if "user_id" not in request.session:
        return redirect("onlineproduce:signin")

    user = Login.objects.get(id=request.session["user_id"])
    return render(request, "profile.html", {"user": user})




def logout_view(request):
    request.session.flush()
    return redirect(request.META.get('HTTP_REFERER'))


