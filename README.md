# A2: Pizza Parlour API


## How to run

Run the main Flask module by running `python3 PizzaParlour.py`

Added pylint to vscode

Run unit tests with coverage by running `pytest --cov-report term --cov=. tests/unit_tests.py`

## Roadmap
![A2_Roadmap](a2_Roadmap.jpeg)

## Design
High cohesion: instead of including the delivery information as seperate variables in the order object, it will be a sepearte order_delivery object that is an element of the order object. This means that each class has a single responsibility. 
