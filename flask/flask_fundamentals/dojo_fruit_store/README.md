# dojo_fruit_store
A small Flask web application that allows students to order fruits from the Dojo store. The app accepts a form submission and displays a checkout confirmation page with the order details.

## How to Run
1. Clone the repository:
    - git clone https://github.com/mchoidojo/dojo_fruit_store.git

2. Navigate to the project folder:
    - cd dojo_fruit_store

3. Activate the environment:
    - flask_env\Scripts\activate

4. Install Flask:
    - pip install flask

5. Run the server
    - python server.py

6. Access the routes

## Pages
1. Home (/)
    - Displays the fruit order form with quantities, name, and student ID

2. Fruits (/fruits)
    - Displays images of all available fruits

3. Checkout (/checkout) 
    - Displays the order confirmation with total items and timestamp

## Observation: 
***Refresh on Checkout Page*** 👉

When hitting the refresh button on the /checkout page, the browser tries to resend the same POST request again. This means the order gets processed twice and the print statement fires again in the terminal.

