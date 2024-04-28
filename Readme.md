Restaurant Review System

This project contains classes to model a simple restaurant review system using Object-Oriented Programming in Python. The classes included are:

    Customer
    Restaurant
    Review

Each class has specific properties and methods to manage relationships and aggregate/association methods.
Classes
Customer

A Customer object is initialized with a first name and a last name. It has methods to manage reviews and relationships with restaurants.
Properties

    first_name
    last_name

Methods

    reviews()
    customers()
    num_negative_reviews()
    has_reviewed_restaurant(restaurant)

Restaurant

A Restaurant object is initialized with a name. It has methods to manage reviews and relationships with customers.
Properties

    name

Methods

    reviews()
    customers()
    average_star_rating()
    top_two_restaurants() (class method)

Review

A Review object is initialized with a Customer, a Restaurant, and a rating. It manages relationships between customers and restaurants.
Properties

    customer
    restaurant
    rating

Usage

Create instances of the classes and use their methods to manage relationships and aggregate/association data.

Example:

python

customer1 = Customer('John', 'Doe')

customer2 = Customer('Jane', 'Doe')


restaurant1 = Restaurant('Restaurant A')

restaurant2 = Restaurant('Restaurant B')


review1 = Review(customer1, restaurant1, 3)

review2 = Review(customer2, restaurant1, 1)

review3 = Review(customer1, restaurant2, 5)

Now you can use the methods to manage relationships and aggregate/association data.

python

print(customer1.num_negative_reviews())  # Output: 1

