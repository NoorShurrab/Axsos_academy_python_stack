from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    # Validates show data before create/update.
    # current_show_id is used to exclude the show being edited from the duplicate title check.
    def create_validator(self, data, current_show_id=None):
        errors = {}

        if len(data['title']) < 2:  # Title must be at least 2 characters
            errors['title'] = "Show title should be at least 2 characters."
            
        if len(data['network']) < 3: # Network must be at least 3 characters
            errors['network'] = "Network should be at least 3 characters."
            
        if len(data['description']) > 0 and len(data['description']) < 10: # Description, if provided, must be at least 10 characters
            errors['description'] = "Description should be at least 10 characters if provided."
            
        if data['release_date']:   # Release date must be in the past
            input_date = datetime.strptime(data['release_date'], '%Y-%m-%d').date()
            if input_date >= datetime.today().date():
                errors['release_date'] = "Release date must be in the past."
                
        # Check for duplicate title, excluding the current show (if editing)
        title_exists = Show.objects.filter(title=data['title'])
        if current_show_id:
            title_exists = title_exists.exclude(id=current_show_id)
            
        if title_exists.exists():
            errors['unique_title'] = "A TV Show with this title already exists."
            
        return errors

# Defines the Show model and its database fields
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Use the custom manager (ShowManager) for this model, enabling Show.objects.create_validator(...)
    objects = ShowManager()