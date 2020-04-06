from PizzaParlour import app
import json


def test_pizza():
	response = app.test_client().get('/pizza')

	assert response.status_code == 200
	assert response.data == b'Welcome to Pizza Planet!'


def test_get_menu():
	response = app.test_client().get('/print_menu')

	assert response.status_code == 200

	with open("Classes/Menu.json", "r") as f:
		data = json.load(f)

	menu = data

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


def test_add_pizza_type():

	response = app.test_client().post('/add_pizza/Shardul/6.99')

	assert response.status_code == 200
	assert response.data == b'Shardul: 6.99'



if __name__ == "__main__":
	test_pizza()
