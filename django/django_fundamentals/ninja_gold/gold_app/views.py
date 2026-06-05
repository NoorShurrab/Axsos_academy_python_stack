from django.shortcuts import render, redirect
import random
from datetime import datetime

# Renders the main page and initializes session variables
def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    return render(request, 'index.html')

# Calculates gold earned/lost based on chosen location
def process_money(request):
    if request.method == 'POST':
        building = request.POST.get('building')
        gold_earned = 0
        current_time = datetime.now().strftime("%B %dth %Y %I:%M %p")
        
        if building == 'farm':
            gold_earned = random.randint(10, 20)
        elif building == 'cave':
            gold_earned = random.randint(10, 20)  
        elif building == 'house':
            gold_earned = random.randint(10, 20) 
        elif building == 'quest':

            gold_earned = random.randint(-50, 50)

        request.session['total_gold'] += gold_earned
        
        if gold_earned >= 0:
            activity_text = f"You entered a {building} and earned {gold_earned} gold. ({current_time})"
            color = "green"
        else:
            activity_text = f"You failed a quest and lost {abs(gold_earned)} gold. Ouch. ({current_time})"
            color = "red"
            
        new_activity = {
            'text': activity_text,
            'color': color
        }
        
        activities_list = request.session['activities']
        activities_list.insert(0, new_activity) 
        request.session['activities'] = activities_list
        
    return redirect('/')

# Flushes the session and restarts the game
def reset(request):
    request.session.flush()
    return redirect('/')