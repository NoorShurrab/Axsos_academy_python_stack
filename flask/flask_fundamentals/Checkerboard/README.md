# Checkerboard
This Flask-based web application dynamically generates a checkerboard grid. It showcases proficiency in server-side routing and the Jinja templating engine.

## Features
Supports three distinct URL patterns:
  - `/`: Default 8x8 checkerboard.
  - `/<x>`: Variable rows with 8 columns.
  - `/<x>/<y>`: Custom rows (x) and columns (y).

  
## Technical Implementation 
The core logic for alternating colors is implemented in the `index.html` template:
- **Parity Comparison:** The grid is built by comparing the parity (even/odd) of both row and column indices.
- **Color Selection:** The first color is applied only if both indices are either even or both are odd. This ensures a perfect checkerboard pattern regardless of grid size.

## How to work
1. Activate the environment:
    - flask_env\Scripts\activate

2. Install dependencies:
    - pip install flask

3. Run the application:
    - python check.py

4. Access the routes