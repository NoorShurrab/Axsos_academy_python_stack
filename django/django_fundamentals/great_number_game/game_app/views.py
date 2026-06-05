from django.shortcuts import render, redirect
import random

# Renders the main game page and initializes the session
def index(request):
    if 'secret_num' not in request.session:
        request.session['secret_num'] = random.randint(1, 100)
        print(f"Secret number generated: {request.session['secret_num']}")  
        request.session['status'] = None  
        request.session['user_guess'] = None
        request.session['attempts'] = 0
        
    return render(request, 'index.html')

# Processes the player's guess and updates the game status
def guess(request):
    if request.method == 'POST':
        user_guess = int(request.POST.get('guess', 0))
        secret_num = request.session.get('secret_num')
        
        request.session['user_guess'] = user_guess
        request.session['attempts'] += 1
        
        if user_guess < secret_num:
            request.session['status'] = 'low'
        elif user_guess > secret_num:
            request.session['status'] = 'high'
        else:
            request.session['status'] = 'correct'

        if request.session['attempts'] >= 5 and request.session['status'] != 'correct':
            request.session['status'] = 'lose'

    return redirect('/')

# Clears the session and restarts the game
def play_again(request):
    keys_to_clear = ['secret_num', 'status', 'user_guess', 'attempts']
    for key in keys_to_clear:
        if key in request.session:
            del request.session[key]
    return redirect("/")

