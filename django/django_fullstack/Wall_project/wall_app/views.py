from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message, Comment
from login_app.models import User
from django.utils import timezone
from datetime import timedelta


def wall_index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        "current_user": User.objects.get(id=request.session['user_id']),
        "all_messages": Message.objects.all().order_by("-created_at") 
    }
    return render(request, 'wall.html', context)


def post_message(request):
    if request.method == "POST":
        if len(request.POST['message']) < 1:
            messages.error(request, "The post cannot be empty!")
        else:
            user = User.objects.get(id=request.session['user_id'])
            Message.objects.create(message=request.POST['message'], user=user)
    return redirect('/wall')

def post_comment(request, message_id):
    if request.method == "POST":
        if len(request.POST['comment']) < 1:
            messages.error(request, "The comment cannot be empty!")
        else:
            user = User.objects.get(id=request.session['user_id'])
            msg = Message.objects.get(id=message_id)
            Comment.objects.create(comment=request.POST['comment'], user=user, message=msg)
    return redirect('/wall')

def delete_message(request, message_id):
    if 'user_id' not in request.session:
        return redirect('/')
        
    message_to_delete = Message.objects.get(id=message_id)
    
    if message_to_delete.user.id == request.session['user_id']:
        now = timezone.now()
        if now - message_to_delete.created_at < timedelta(minutes=30):
            message_to_delete.delete()
        else:
            messages.error(request, "You cannot delete a post that is more than 30 minutes old!")
    return redirect('/wall')
