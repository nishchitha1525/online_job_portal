from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import Job, Application
from django.contrib.auth import logout

def home(request):
    return render(request, "home.html")


# ---------------- LOGIN ----------------
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login Successful!")
            return redirect("/jobs/")
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")


# ---------------- REGISTER ----------------
def register(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=fullname).exists():
            messages.error(request, "Username already exists!")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, "register.html")

        User.objects.create_user(
            username=fullname,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful! Please Login.")
        return redirect("/login/")

    return render(request, "register.html")


# ---------------- JOBS ----------------
# ---------------- JOBS ----------------
def jobs(request):
    title = request.GET.get("title")
    location = request.GET.get("location")

    jobs = Job.objects.all()

    if title:
        jobs = jobs.filter(title__icontains=title)

    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, "jobs.html", {
        "jobs": jobs
    })


# ---------------- APPLY JOB ----------------
def apply(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        qualification = request.POST.get("qualification")
        resume = request.FILES.get("resume")

        Application.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            qualification=qualification,
            resume=resume
        )

        messages.success(request, "Application Submitted Successfully!")
        return render(request, "success.html")

    return render(request, "apply.html")


# ---------------- ABOUT ----------------
def about(request):
    return render(request, "about.html")


# ---------------- CONTACT ----------------
def contact(request):
    return render(request, "contact.html")


# ---------------- PROFILE ----------------
def profile(request):
    return render(request, "profile.html")


# ---------------- DASHBOARD ----------------
def dashboard(request):
    return render(request, "dashboard.html")


# ---------------- LOGOUT ----------------


def logout_user(request):
    logout(request)
    return redirect('home')


# ---------------- MY APPLICATIONS ----------------
def my_applications(request):
    applications = Application.objects.all()

    return render(request, "my_applications.html", {
        "applications": applications
    })


# ---------------- CHANGE PASSWORD ----------------
def change_password(request):
    if request.method == "POST":
        messages.success(request, "Password Changed Successfully!")

    return render(request, "change_password.html")


# ---------------- FORGOT PASSWORD ----------------
def forgot_password(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "forgot_password.html")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email not found!")
            return render(request, "forgot_password.html")

        user.set_password(password)
        user.save()

        messages.success(request, "Password Reset Successfully! Please Login.")
        return redirect("/login/")

    return render(request, "forgot_password.html")

    
