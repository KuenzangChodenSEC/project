from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Event Name")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(null=True, blank=True, verbose_name="End Date (Optional)")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    
    # You might want to add fields like 'created_by' (ForeignKey to User) in a real app
    
    class Meta:
        ordering = ['start_date']
        verbose_name = "Calendar Event"
        verbose_name_plural = "Calendar Events"

    def __str__(self):
        # Format: "Event Name (YYYY-MM-DD)"
        return f"{self.title} ({self.start_date.strftime('%Y-%m-%d')})"
    



class Plan(models.Model):
    # Plan Name choices
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    BIANNUALLY = 'biannually'

    PLAN_NAME_CHOICES = [
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (BIANNUALLY, 'Biannually'),
    ]

    plan_name = models.CharField(
        max_length=50,
        choices=PLAN_NAME_CHOICES,
        default=MONTHLY,
        unique=True,
    )
    
    # Validity in months. Use floats for fractions (e.g., 0.25 for 7 days)
    # The JavaScript handles the display logic for these values.
    # 0.25 month = approx 7 days
    # 1.0 month = 1 month
    # 6.0 months = 6 months
    validity_months = models.FloatField(
        default=1.0,
        help_text="Validity period in months (e.g., 0.25 for 7 days, 1.0 for 1 month)."
    )
    
    # Use DecimalField for financial accuracy
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Amount in Nu."
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_plan_name_display()} Plan - Nu.{self.amount}"

    class Meta:
        ordering = ['validity_months']
        verbose_name = "Plan Detail"
        verbose_name_plural = "Plan Details"


class UserPayment(models.Model):
    # Choices for the Plan Field
    PLAN_CHOICES = [
        ('weekly', '1 Week'),
        ('monthly', '1 Month'),
        ('biannually', '6 Months'),
        ('yearly', '1 Year'), # Added 'yearly' for completeness based on dummy data
    ]

    # Choices for the Payment Status Field
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ]

    # Assume a Member/User model exists and is linked by Foreign Key.
    # For this example, we'll use a string for the name/ID, but in a real app,
    # you would use ForeignKey to link to a Member model.

    user_name = models.CharField(max_length=100, verbose_name=_("Member Name"))
    member_id = models.CharField(max_length=50, unique=True, verbose_name=_("Member ID"))

    plan = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES,
        default='monthly',
        verbose_name=_("Plan Duration")
    )

    # Use DecimalField for financial data to prevent floating point errors
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Payment Amount (Nu.)")
    )
    
    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending',
        verbose_name=_("Status")
    )

    # Optional: Track when the payment was made/recorded
    payment_date = models.DateTimeField(auto_now_add=True)
    
    # Optional: Track the plan expiration date
    # expiration_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = _("User Payment")
        verbose_name_plural = _("User Payments")
        ordering = ['-payment_date'] # Show newest payments first

    def __str__(self):
        return f"{self.user_name} - {self.get_plan_display()} - {self.get_payment_status_display()}"
    


class Equipment(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=255)
    total_no = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.name
    
class Member(models.Model):
    name = models.CharField(max_length=255)
    member_id = models.CharField(max_length=50)
    date_join = models.DateField(default=timezone.now)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.member_id})"