from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,ContactForm
from .models import UMessage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout



# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"You have successfully registered...")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Username or Password Incorrect")
            return render(request,"login.html",context)

        messages.success(request,"You have successfully logged in.")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

    
def logoutUser(request):
    logout(request)
    messages.success(request,"You have successfully logged out.")
    return redirect("index")

def contact(request):

    form = ContactForm(request.POST or None)
    if request.method == "POST":
        Name = request.POST.get("Name")
        Email = request.POST.get("Email")
        Message = request.POST.get("Message")

        newMessage = UMessage(Name = Name, Email = Email, Message = Message)
        newMessage.save()

        messages.info(request,"Your message send successfully...")

        return redirect("user:contact")
    context = {
            "form" : form
        }
    return render(request,"contact.html",context)


'''def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template =
                get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })'''
    