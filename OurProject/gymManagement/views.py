from django.shortcuts import render, redirect
from .models import Event, Plan, UserPayment, Member
from django.utils import timezone
from django.contrib.auth.decorators import login_required # Recommended for admin views
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


class CustomPlanJSONEncoder(DjangoJSONEncoder):
    """
    Custom encoder to ensure Decimal and Float values are correctly formatted
    for JSON serialization, which is crucial when passing data to JavaScript.
    """
    def default(self, obj):
        if isinstance(obj, float):
            return obj
        return super().default(obj)



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
    """
    Fetches all plans and passes them as a JSON string to the template.
    """
    # Retrieve all plan data as dictionaries, ordered by validity
    plans_queryset = Plan.objects.all().values(
        'plan_name', 
        'validity_months', 
        'amount'
    )

    # Convert the queryset to a JSON string using the custom encoder
    # The 'plans|safe' filter in the template requires a JSON string here.
    plans_json = json.dumps(list(plans_queryset), cls=CustomPlanJSONEncoder)
    
    context = {
        'plans': plans_json, # JSON string
        # Add other context variables needed for the template's URLs (e.g., user details)
        'plans_data_list': list(plans_queryset), # List of dictionaries for the initial table rendering if needed, 
                                                 # though your JS handles the full render now.
    }
    
    return render(request, 'viewplan.html', context)
# View payment details

def view_payment(request):
    # This retrieves ALL payments. You might want to paginate this in a real app.
    # The {% for member in members %} block in your HTML will use this queryset.
    members = UserPayment.objects.all() 
    return render(request, 'viewpayment.html', {'members': members})

# A new view for the AJAX/fetch request to update payment status
@require_http_methods(["POST"])
def update_payment_status(request):
    # In a real application, you should handle CSRF protection (middleware handles this)
    # and perform authentication/authorization checks here.
    
    try:
        # Assuming you pass data via JSON body
        # For simplicity with client-side, we'll assume POST data if no JSON is parsed
        import json
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            # Fallback if request.body isn't a valid JSON, assuming form-like data
            data = request.POST 

        member_id = data.get('member_id')
        new_status = data.get('new_status') # Should be 'paid' or 'pending'

        if not member_id or new_status not in ['paid', 'pending']:
            return JsonResponse({'success': False, 'message': 'Invalid data provided.'}, status=400)

        payment = UserPayment.objects.get(member_id=member_id)
        payment.payment_status = new_status
        payment.save()
        
        return JsonResponse({'success': True, 'message': f'Payment status updated to {new_status}.'})
    
    except UserPayment.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Member not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'An error occurred: {str(e)}'}, status=500)


# View all members
def view_members(request):
    members = Member.objects.all().order_by('-date_join')
    return render(request, 'viewmembers.html', {'members': members})
# Inventory management page
# gymManagement/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Equipment
from .forms import EquipmentForm

# View for listing all equipment
def inventory(request):
    equipment_list = Equipment.objects.all()
    return render(request, 'inventory.html', {'equipment_list': equipment_list})



