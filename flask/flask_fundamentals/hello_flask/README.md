# Flask Routing
This project demonstrates the core concepts of URL Routing, including static routes, dynamic routes with variable rules.

### Description
1. @app.route('/') 
    - It handles requests to the main page (localhost:5000/).
2. @app.route('/Champion')
    - It triggers when the user visits localhost:5000/Champion.
3. @app.route('/say/<name>')
    - Dynamic route (Variable Rules) it takes a string 'name' from the URL and returns a personalized greeting.
4. @app.route('/repeat/<int:num>/<word>')
    - Iterative route accepts an integer 'num' and a string 'word'. 
    - It repeats the word 'num' times as HTML paragraphs.