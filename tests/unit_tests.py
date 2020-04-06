from PizzaParlour import app
import json


def test_pizza():
	response = app.test_client().get('/pizza')

	assert response.status_code == 200
	assert response.data == b'Welcome to Pizza Planet!'


def test_get_menu():
	response = app.test_client().get('/print_menu')

	assert response.status_code == 200
	menu = {
		"all_pizza_types": {
			"Pepperoni": 8.99,
			"Margherita": 7.5,
			"Vegetarian": 7.59,
			"Neapolitan": 11.99
		},
		"all_drinks": {
			"Coke": 1.59,
			"Diet Coke": 1.69,
			"Coke Zero": 1.69,
			"Diet Pepsi": 1.29,
			"Dr Pepper": 1.29,
			"Water": 0.99,
			"Pepsi": 1.39,
			"Juice": 1.99
		},
		"all_pizza_sizes": {
			"small": -2.0,
			"medium": 0.0,
			"large": 2.0,
			"family size": 5.0
		},
		"all_pizza_toppings": {
			"onions": 0.1,
			"tomatoes": 0.1,
			"anchovies": 0.1,
			"extra cheese": 0.5,
			"garlic": 0.2,
			"salt": 0.0,
			"ham": 0.5
		}
	}

	assert json.loads(response.data) == menu


def test_get_item():
	response = app.test_client().get('/get_item/Coke')

	assert response.status_code == 200
	assert response.data == b'Coke: 1.59'


def test_new_order():

	response_body = {
		"Pizzas": {
			"Margherita": {
				"size": "large",
				"toppings": ["onions", "tomatoes"]
			}
		},
		"Drinks": ["Coke"]
	}

	response = app.test_client().post('/new_order', json=response_body)

	assert response.status_code == 200
	assert response.data == b'Order was filled in successfully. Your orderID is: 0'


def test_get_order_info():

	response = app.test_client().get('/get_order_info/0')

	desired_response = b'{"orderID": 0, "order status": "OrderStatus.STARTED", "order items": [{"Coke": 1.59}, {"Margherita": {"size": "large", "toppings": ["onions", "tomatoes"], "price": 9.7}}], "order distribution": null, "order price": 11.29, "order address": null}'

	assert response.status_code == 200
	assert response.data == desired_response


def test_set_order_distribution():

	response_body = {"uber": "4 David Copperfield St"}

	response = app.test_client().patch('/order_distribution/0/deliver', json=response_body)

	assert response.status_code == 200
	assert response.data == b'{"orderID": 0, "order status": "OrderStatus.STARTED", "order items": [{"Coke": 1.59}, {"Margherita": {"size": "large", "toppings": ["onions", "tomatoes"], "price": 9.7}}], "order distribution": "uber", "order price": 11.29, "order address": "4 David Copperfield St"}'


def test_add_to_order():
	# Testing add to order


if __name__ == "__main__":
	test_pizza()
