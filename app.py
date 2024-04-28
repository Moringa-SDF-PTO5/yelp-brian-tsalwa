class Customer:
    _customer_objects = []

    def __init__(self, first_name, last_name):
        if not isinstance(first_name, str) or (len(first_name) < 1 or len(first_name) > 25):
            raise ValueError("First name must be a string between 1 and 25 characters.")
        if not isinstance(last_name, str) or (len(last_name) < 1 or len(last_name) > 25):
            raise ValueError("Last name must be a string between 1 and 25 characters.")

        self.first_name = first_name
        self.last_name = last_name
        self._customer_objects.append(self)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def reviews(self):
        reviews = [review for review in Review._review_objects if review.customer == self]
        return reviews

    @property
    def restaurants(self):
        restaurants = [review.restaurant for review in self.reviews]
        return restaurants

    def num_negative_reviews(self):
        return sum(1 for review in self.reviews if review.rating <= 2)

    def has_reviewed_restaurant(self, restaurant):
        return any(review.restaurant == restaurant for review in self.reviews)


class Restaurant:
    _restaurant_objects = []
    _review_objects = []    
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 1:
            raise ValueError("Restaurant name must be a non-empty string.")

        self.name = name
        self._restaurant_objects.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def reviews(self):
        return [review for review in Review._review_objects if review.restaurant == self]

    @property
    def customers(self):
        customers = [review.customer for review in self.reviews]
        return list(set(customers))

    def average_star_rating(self):
        if not self.reviews:
            return 0.0
        return round(sum(review.rating for review in self.reviews) / len(self.reviews), 1)

    @classmethod
    def top_two_restaurants(cls):
        if not any(restaurant.reviews for restaurant in cls._restaurant_objects):
            return None
        avg_ratings = [(restaurant.name, restaurant.average_star_rating()) for restaurant in cls._restaurant_objects]
        avg_ratings.sort(key=lambda x: x[1], reverse=True)
        return [Restaurant(name) for name, _ in avg_ratings[:2]]


class Review:
    _review_objects = []  # To store all review objects

    def __init__(self, customer, restaurant, rating):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be a Customer instance.")
        if not isinstance(restaurant, Restaurant):
            raise ValueError("Restaurant must be a Restaurant instance.")
        if not isinstance(rating, int) or (rating < 1 or rating > 5):
            raise ValueError("Rating must be an integer between 1 and 5.")

        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self._review_objects.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        self._customer = value

    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, value):
        self._restaurant = value

    @classmethod
    def top_negative_reviewer(cls):
        if not any(review.rating < 3 for review in cls._review_objects):
            return None
        negative_reviews = [review for review in cls._review_objects if review.rating < 3]
        negative_reviews.sort(key=lambda x: x.customer.name)
        negative_reviews.sort(key=lambda x: x.rating, reverse=True)
        return negative_reviews[0].customer
    
customer1 = Customer("Brian", "Tsalwa")

restaurant1 = Restaurant("SushiSo")

review1 = Review(customer1, restaurant1, 5)

print(review1.rating)