# Counter
A Flask web application that counts the number of times the root route ('/') has been visited. The count is stored in the session so it persists across page refreshes.

## How to Run
1. Activate the environment:
    - flask_env\Scripts\activate

2. Install Flask:
    - pip install flask

3. Run the server:
    - python server.py

4. Access the route

## Routes
`[/]`                  Displays the counter value

`[/destroy_session]`   Clears the session and redirects to /

`[/add_two]`           Increments the counter by 2 and renders the index page

`[/reset]`             Resets the counter to 0 and renders the index page


