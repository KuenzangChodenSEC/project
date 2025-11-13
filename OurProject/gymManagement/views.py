from django.shortcuts import render, redirect
from .models import CalendarEvent, Plan, Member, Equipment, GymMember

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
    events = CalendarEvent.objects.all().order_by('-start_date')
    return render(request, 'admin.html', {'events': events})


# Profile picture / user profile page
def profile_page(request):
    return render(request, 'pfp.html')

# View plan (detailed plan list)
def view_plan(request):
    plans = Plan.objects.all()
    return render(request, 'viewplan.html', {'plans': plans})

# View payment details
def view_payment(request):

    # Fetch all members from the database
    members = Member.objects.all().order_by('name')  # order alphabetically

    # Pass members to the template
    context = {
        'members': members
    }
    return render(request, 'viewpayment.html', context)


# View all members
def view_members(request):
    members = GymMember.objects.all()
    return render(request, "viewmembers.html", {"members": members})

# Inventory management page
def inventory(request):
    """
    Display all equipment in the inventory.
    """
    # Fetch all equipment from the database, order by name ascending
    equipment_list = Equipment.objects.all().order_by('name')

    context = {
        'equipment_list': equipment_list,
    }

    return render(request, 'inventory.html', context)