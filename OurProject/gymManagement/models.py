from django.db import models

# Create your models here.
class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Plan(models.Model):
    PLAN_VALIDITY_CHOICES = [
        (0.25, 'Weekly (7 Days)'),
        (1, 'Monthly'),
        (6, '6 Months'),
    ]

    plan_name = models.CharField(max_length=100, unique=True)
    validity = models.FloatField(choices=PLAN_VALIDITY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['validity']
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    def __str__(self):
        return f"{self.plan_name} ({self.get_validity_display()}) - Nu.{self.amount}"






class Member(models.Model):
    PLAN_CHOICES = [
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('six_months', '6 Months'),
]
    
    PAYMENT_STATUS_CHOICES = [
    ('Paid', 'Paid'),
    ('Pending', 'Pending'),
]
    

    # Unique identifier for the member
    member_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)  # optional
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.member_id}) - {self.payment_status}"


class Equipment(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    # Fields
    name = models.CharField(max_length=255)
    total_no = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    # Optional: Auto timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # String representation
    def __str__(self):
        return f"{self.name} ({self.total_no})"
    

class GymMember(models.Model):
    PLAN_CHOICES = [
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('biannually', 'Biannually'),
    ]

    member_id = models.CharField(max_length=20, unique=True)  # Example: GM-1001
    name = models.CharField(max_length=100)
    date_join = models.DateField()
    plan = models.CharField(max_length=12, choices=PLAN_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.member_id})"

    class Meta:
        db_table = 'gymManagement_gymmember'  # Ensures table matches your view