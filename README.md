# A2: Pizza Parlour API


## How to run

Run the main Flask module by running `python3 PizzaParlour.py`

Added pylint to vscode

Run unit tests with coverage by running `pytest --cov-report term --cov=. tests/unit_tests.py`

## Roadmap
![A2_Roadmap](a2_roadmap.jpg)

## 1. Design
> _choose design patterns to use and define data objects_

Object Oriented (Gives High cohesion): instead of including the delivery information as seperate variables in the order object, it will be a sepearte order_delivery object that is an element of the order object. This means that each class has a single responsibility. 

Factory: There are mutliple types of delivery (uber, foodora, in-house, etc.). Each of these delivery types will be a class that implements the OrderDistribution interface. A factory class will create the OrderDistribution object, filling in the constructor with the proper parameters based off the type (uber: JSON, foodora: CSV, in-house). 

Serialization: For each class we have defined, there is a toString method to serialize the data to JSON. 

Reference: [Uber Menu Integration API](https://developer.uber.com/docs/eats/guides/menu_integration)

#### Data Class Diagram
![Design Patterns](a2_design_patterns.jpg)

#### Criticisms and Limitations of Design Patterns

## 2. Write
> pair program features and document as we go

#### Pair Programming
1. Creating Order class
    - **Driver**: Ryan 
    - **Navigator**: Shardul
    - We didn't know how to define static variables in Python, how to modify static variables in classes
    - How to have the static variables in the init functions.

    - We though that creating a class would be shorter, but there was a little bit of a learning curve as we remembered how to do things in Python. The Navigator, Shardul, helped by looking up references on his computer
    - We also made the collaborative decision to swtich from VSCode to Pycharm so we could use the built-in functionality of linting and other language specific features to help us create clean code. 
    - From here on, we are going to adjust our expectations of what we can get done in a hour of pair programming. The next hour we will spend on creating the MenuItem class and its subclasses of Drink and Pizza. 

2. Creating MenuItem class and Children Drink and Pizza
    - **Driver**: Shardul
    - **Navigator**: Ryan 
    - Should the pizza type be an ENUM? Unfortunately we couldn't have that because the Pizza Parlour should be able to add pizza types. The same can be said about the toppings, so we created a dictionary and list for each of those respectively. The dictionary's key is the pizza type and the value is the price of that particular pizza type. 
    - We externalised our data so that it can be changed globally. All the information is stored in Menu.json now regarding the goods provided by Pizza Parlour.
    - We took advantage of inheritance and the child-parent relationship while creating our classes in this session of pair-programming!

## 3. Test
> finalize unit tests and ensure code coverage and cleanliness

## Pair Programming
1. Creating Classes for each file

2. 
