from django.db import models


class CourseManager(models.Manager):
    def create_validator(self, post_data):
        errors = {}

        if len(post_data['name']) <= 5:
            errors['name'] = "Course name must be more than 5 characters long."
            
        
        if len(post_data['description']) <= 15:
            errors['description'] = "Description must be more than 15 characters long."
            
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CourseManager()

class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="course_description")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


