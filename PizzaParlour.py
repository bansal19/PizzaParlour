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

# Store all the orders
all_orders = []


# Helper Functions:
def helper_add_to_order(order, json_data):
    # Get all the Drinks from the POST request and add them to the order

    try:
        if len(json_data["Drinks"]) > 0:
            for drink in json_data["Drinks"]:
                order_drink = Drink(drink)
                order.add_order_item(order_drink)
    except KeyError:
        pass

    try:
        # Get all the Pizzas from the POST request and add them to the order
        if len(json_data["Pizzas"]) > 0:
            for pizza in json_data["Pizzas"]:
                pizza_name = pizza
                pizza_size = json_data["Pizzas"][pizza_name]["size"]
                pizza_toppings = json_data["Pizzas"][pizza_name]["toppings"]
                order_pizza = Pizza(pizza_name, pizza_size, pizza_toppings)
                order.add_order_item(order_pizza)
    except KeyError:
        pass


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
        helper_add_to_order(new_customer_order, request.get_json())

        all_orders.append(new_customer_order)
        return "Order was filled in successfully. Your orderID is: " + str(new_customer_order.order_number)

    else:
        return "Sorry, have to use POST request to fill in pizza order"


@app.route("/get_order_info/<order_id>", methods=['GET'])
def get_order_info(order_id):

    if request.method == 'GET':
        for order in all_orders:
            if order.order_number == int(order_id):
                return json.dumps(order.to_dict())

        return "Sorry, the order with the order number " + order_id + " was not found."


@app.route("/order_distribution/<order_id>/<pickup_or_deliver>", methods=['PATCH'])
def set_order_distribution(order_id, pickup_or_deliver):
    """ Provide information for if the order is for either pickup or delivery
    possible values for pick_or_deliver: ["pickup", "in-house", 'uber', "foodora"] """

    if request.method == 'PATCH':
        for order in all_orders:
            if order.order_number == int(order_id):
                if pickup_or_deliver == "pickup":
                    order.set_order_distribution(pickup_or_deliver)
                else:
                    json_data = request.get_json()
                    order.set_order_distribution(list(json_data.keys())[0], json_data[list(json_data.keys())[0]])
                return json.dumps(order.to_dict())

        return "Sorry, the order with the order number " + order_id + " was not found."


@app.route("/add_to_order/<order_id>", methods=['PATCH'])
def add_to_order(order_id):
    """Given a particular orderID, add to this specific order"""

    if request.method == 'PATCH':
        for order in all_orders:
            if order.order_number == int(order_id):
                json_data = request.get_json()
                helper_add_to_order(order, json_data)
                return json.dumps(order.to_dict())

        return "Sorry, the order with the order number " + order_id + " was not found."


@app.route("/remove_from_order/<order_id>", methods=['PATCH'])
def remove_from_order(order_id):
    """ Given particular orderID, remove specific items from the order"""

    if request.method == 'PATCH':
        for order in all_orders:
            if order.order_number == int(order_id):
                json_data = request.get_json()

                try:
                    if len(json_data["Drinks"]) > 0:
                        for drink in json_data["Drinks"]:
                            drink_to_remove = Drink(drink)
                            order.remove_order_item(drink_to_remove)
                except KeyError:
                    pass

                try:
                    if len(json_data["Pizzas"]) > 0:
                        for pizza in json_data["Pizzas"]:
                            pizza_to_remove = Pizza(pizza)
                            order.remove_order_item(pizza_to_remove)
                except KeyError:
                    pass

                return json.dumps(order.to_dict())

        return "Sorry, the order with the order number " + order_id + " was not found."


@app.route("/cancel_order/<order_id>", methods=['DELETE'])
def cancel_order(order_id):
    """Cancel the order with this orderID"""

    if request.method == 'DELETE':
        for order in all_orders:
            if order.order_number == int(order_id):
                order.cancel_order()
                all_orders.remove(order)


@app.route("/deliver_order/<order_id>", methods=['PATCH'])
def deliver_order(order_id):

    if request.method == 'PATCH':
        for order in all_orders:
            if order.order_number == int(order_id):
                if order.distribution == "pickup":
                    order.order_ready_for_pickup()
                    return "Order " + order_id + " ready for pickup"

                elif order.distribution == "in-house":
                    order.order_out_for_delivery()
                    return "Order " + order_id + " is out for our in-house delivery to " + order.order_address

                elif order.distribution == "uber":
                    order.order_out_for_delivery()
                    return json.dumps(order.to_dict())

                elif order.distribution == "foodora":
                    order.order_out_for_delivery()
                    return json.dumps(order.to_dict())

@app.route("/")

if __name__ == "__main__":
    app.run()
