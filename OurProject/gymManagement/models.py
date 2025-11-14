from django.db import models

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
