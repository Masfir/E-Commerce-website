from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages

# Create your views here.
    
def signup(request):
    if request.method == "POST":
        get_name = request.POST.get("name")
        get_email = request.POST.get("email")
        get_password = request.POST.get("password")
        get_confirm_password = request.POST.get("confirm_password")       
        get_name = get_name.title()
        
        if get_password != get_confirm_password:
            messages.warning(request, "Password is not matching.Please enter the correct password.")
            return render(request, "signup.html")
        
        try:
            if User.objects.get(email = get_email):
                messages.warning(request, f"{get_email} email is taken")
                return render(request, "signup.html")
                
        
        except Exception as identifier:
            pass    
          
        myuser = User.objects.create_user(get_name, get_email, get_password)
        myuser.save()
        messages.success(request, "Created your account")
        return redirect("/authapp/authlogin")
                           
    return render(request,'signup.html')
    

def authlogin(request):
    if request.method == "POST":
        get_name = request.POST.get("name")
        get_email = request.POST.get("email")
        get_password = request.POST.get("password")
        myuser = authenticate(username = get_name, email = get_email, password = get_password)
        
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.warning(request, "Invalid")
    return render(request,'login.html')

def authlogout(request):
    logout(request)
    messages.success(request, "Logout successful")
    return render(request, 'login.html')
