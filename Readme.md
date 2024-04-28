Restaurant Review System

This repository contains a simple implementation of a restaurant review system using Python classes. The system includes three main classes: Customer, Restaurant, and Review.
Classes
Customer

The Customer class represents a customer who can write reviews for restaurants. It has the following properties:

    first_name: A string representing the customer's first name.
    last_name: A string representing the customer's last name.

The Customer class has the following methods:

    reviews(): Returns a list of all reviews written by the customer.
    restaurants(): Returns a list of all restaurants reviewed by the customer.
    num_negative_reviews(): Returns the total number of negative reviews (with a rating of 1 or 2) written by the customer.
    has_reviewed_restaurant(restaurant): Returns a boolean indicating whether the customer has written a review for the given restaurant.

Restaurant

The Restaurant class represents a restaurant that can be reviewed by customers. It has the following properties:

    name: A string representing the name of the restaurant.

The Restaurant class has the following methods:

    reviews(): Returns a list of all reviews for the restaurant.
    customers(): Returns a list of all customers who have reviewed the restaurant.
    average_star_rating(): Returns the average star rating for the restaurant based on its reviews.
    top_two_restaurants(): Returns a list of the top two restaurants with the highest average star ratings.

Review

The Review class represents a review written by a customer for a restaurant. It has the following properties:

    customer: A Customer instance representing the customer who wrote the review.
    restaurant: A Restaurant instance representing the restaurant reviewed.
    rating: An integer representing the rating of the review (1-5).

Usage

To use the restaurant review system, simply create instances of the Customer, Restaurant, and Review classes and call their methods as needed.

Here's an example:

python

# Create a new customer

customer1 = Customer("John", "Doe")


# Create a new restaurant

restaurant1 = Restaurant("Best Restaurant")


# Create a new review

review1 = Review(customer1, restaurant1, 5)


# Access the customer property of a Review object

print(review1.customer)  # Output: <__main__.Customer object at 0x...>


# Access the restaurant property of a Review object

print(review1.restaurant)  # Output: <__main__.Restaurant object at 0x...>


# Access the reviews method of a Restaurant object

print(restaurant1.reviews())  # Output: [<__main__.Review object at 0x...>]


# Access the customers method of a Restaurant object

print(restaurant1.customers())  # Output: [<__main__.Customer object at 0x...>]


# Access the average_star_rating method of a Restaurant object

print(restaurant1.average_star_rating())  # Output: 0.0


# Access the top_two_restaurants class method

print(Restaurant.top_two_restaurants())  # Output: None


# Access the num_negative_reviews method

print(customer1.num_negative_reviews())  # Output: 0


# Access the has_reviewed_restaurant method

print(customer1.has_reviewed_restaurant(restaurant1))  # Output: True

Testing

To test the restaurant review system, simply run the provided test.py file. It contains unit tests for all methods in the Customer, Restaurant, and Review classes.

bash

python test.py

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
License

This project is licensed under the MIT License - see the LICENSE file for details.