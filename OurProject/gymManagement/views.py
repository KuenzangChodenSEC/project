from django.shortcuts import render, redirect
from .models import Event
from django.utils import timezone


# Homepage
def index(request):
    return render(request, 'index.html')

# Membership plan page
def plan(request):
    return render(request, 'plan.html')

# Why Join Us page
def why_join_us(request):
    return render(request, 'whyjoinus.html')

# Login page
def login_view(request):
    return render(request, 'login.html')

# Signup page
def signup(request):
    return render(request, 'signup.html')

# Forgot password page
def forgot_password(request):
    return render(request, 'forgot-password.html')

# Admin dashboard page
def admin_page(request):
    # Fetch events that start today or in the future
    upcoming_events = Event.objects.filter(start_date__gte=timezone.now().date()).order_by('start_date')
    
    # Pass the events to the template context
    context = {
        'events': upcoming_events
    }
    return render(request, 'admin.html', context)


# Profile picture / user profile page
def profile_page(request):
    return render(request, 'pfp.html')

# View plan (detailed plan list)
def view_plan(request):
    return render(request, 'viewplan.html')

# View payment details
def view_payment(request):

    return render(request, 'viewpayment.html')


# View all members
def view_members(request):
   
    return render(request, "viewmembers.html")

# Inventory management page
def inventory(request):

    return render(request, 'inventory.html')