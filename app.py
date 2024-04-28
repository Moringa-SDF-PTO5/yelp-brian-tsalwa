class Customer():
    all_customers = []
    def __init__(self, first_name, last_name, restaurant=None):
        if not (isinstance(first_name, str) and isinstance(last_name, str)):
            raise ValueError("Names must be of type str")
        if not (1 <= len(first_name) <= 25 and 1 <= len(last_name) <= 25):
            raise ValueError("Names must be between 1 and 25 characters, inclusive")
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.all_customers.append(self)
        self.restaurants = []
        if restaurant is not None:
            self.restaurants.append(restaurant)
            restaurant.customers.append(self)
        self.reviews = []

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if not (isinstance(value, str)):
            raise ValueError("first_name must be a string")
        if not (1 <= len(value) <= 25):
            raise ValueError("first_name must be between 1 and 25 characters, inclusive")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if not (isinstance(value, str)):
            raise ValueError("last_name must be a string")
        if not (1 <= len(value) <= 25):
            raise ValueError("last_name must be between 1 and 25 characters, inclusive")
        self._last_name = value

    @property
    def restaurants(self):
        return self._restaurants
    @restaurants.setter
    def restaurants(self, value):
        if not (isinstance(value, list) and all(isinstance(x, Restaurant) for x in value)):
            raise ValueError("restaurants must be a list of Restaurant objects")
        self._restaurants = value

    def reviews(self):
        return [review for review in self._reviews if review is not None]

    def customers(self):
        return {review.restaurant for review in self.reviews()}

class Restaurant: 
    all_restaurants = []
    def __init__(self, name):
        if not (isinstance(name, str)):
            raise ValueError("name must be a string")
        if not (1 <= len(name) <= 100):
            raise ValueError("name must not be greater than 100 characters")
        
        self._name = name
        self.all_restaurants.append(self)
        self.review = []
        self.customers = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        if not (isinstance(value, list) and all(isinstance(x, Review) for x in value)):
            raise ValueError("reviews must be a list of Review objects")
        self._reviews = value

    def reviews(self):
        return [review for review in self._reviews if review is not None]
    def customers(self):
        return {review.restaurant for review in self.reviews()}

class Review:

    all_reviews = []
    def __init__(self, Customer, rating):
        if not (isinstance(rating, int) and 1 <= rating <= 5):
            raise ValueError("rating must be an integer between 1 and 5, inclusive")
        self.rating = rating
        self.customer = Customer
        self.restaurant = Customer.restaurants[0]
        self.restaurant.reviews.append(self)
        self.customer.reviews.append(self)
        self.all_reviews.append(self)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value    

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):

    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def __repr__(self):
        return f"<Review for {self.restaurant.name} by {self.customer.name}>"
    # @classmethod
    # def all(cls):
    #     return cls.all_reviews
    # @classmethod
    # def top_rated(cls):
    #     return sorted(cls.all(), key=lambda x: x.rating, reverse=True)[:3]
    # @classmethod
    # def top_reviewed(cls):
    #     return sorted(cls.all(), key=lambda x: len(x.reviews), reverse=True)[:3]
    # @classmethod
    # def most_reviews(cls):
    #     return sorted(cls.all(), key=lambda x: len(x.reviews), reverse=True)[0]
    # @classmethod
    # def top_reviewed_restaurants(cls):
    #     return sorted(cls.all(), key=lambda x: len(x.reviews), reverse=True)[:3]
    # @classmethod
    # def top_rated_restaurants(cls):
    #     return sorted(cls.all(), key=lambda x: x.rating, reverse=True)[:3]
    # @classmethod
    # def top_rated_restaurants(cls):
    #     return sorted(cls.all(), key=lambda x: x.rating, reverse=True)[:3]