from flask import Flask, request
from Classes.Menu import Menu
from Classes.Order import Order
from Classes.MenuItem import MenuItem
from Classes.Drink import Drink
from Classes.Pizza import Pizza
import json

menu_path = "Classes/Menu.json"

app = Flask("Assignment 2")

menu = Menu(menu_path)


""" Menu APIs: """
@app.route('/pizza')
def welcome_pizza():
    return 'Welcome to Pizza Planet!'


@app.route('/print_menu')
def print_menu():
    return str(menu.get_menu())


@app.route("/get_item/<menu_item>", methods=['GET'])
def get_item(menu_item):
    return str(menu_item) + ": " + str(menu.get_item_price(menu_item))


""" Order APIs: """


@app.route("/new_order", methods=['POST'])
def new_order():
    """
    Input a new order into Pizza Parlour. It's a POST request with the body being a JSON
    """
    if request.method == 'POST':
        new_customer_order = Order()
        json_data = request.get_json()

        # Get all the Drinks from the POST request and add them to the order
        if len(json_data["Drinks"]) > 0:
            for drink in json_data["Drinks"]:
                order_drink = Drink(drink)
                new_customer_order.add_order_item(order_drink)

        # Get all the Pizzas from the POST request and add them to the order
        if len(json_data["Pizzas"]) > 0:
            for pizza in json_data["Pizzas"]:
                pizza_name = pizza
                pizza_size = json_data["Pizzas"][pizza_name]["size"]
                pizza_toppings = json_data["Pizzas"][pizza_name]["toppings"]
                order_pizza = Pizza(pizza_name, pizza_size, pizza_toppings)
                new_customer_order.add_order_item(order_pizza)

        return "Order was filled in successfully. Your orderID is: " + str(new_customer_order.order_number)

    else:
        return "Sorry, have to use POST request to fill in pizza order"


@app.route("/get_order_info/<orderID>", methods=['GET'])
def get_order_info(orderID):

    if request.method == 'GET':
        

@app.route("/order_distribution/<orderID>/<pickOrDeliver>")
def order_distribution(orderID, pickOrDeliver):
    """ Get an order in for either pickup or delivery"""
    pass


@app.route("/add_to_order/<orderID>/")
def add_to_order(orderID):
    """Given a particular orderID, add to this specific order"""
    pass


@app.route("/remove_from_order/<orderID>/")
def remove_from_order(orderID):
    """ Given particular orderID, remove specific items from the order"""
    pass


@app.route("/cancel_order/<orderID>")
def cancel_order(orderID):
    """Cancel the order with this orderID"""
    pass


if __name__ == "__main__":
    app.run()
