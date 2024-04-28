class Customer():
    all_customers = []
    def __init__(self, first_name, last_name):
        if not (isinstance(first_name, str) and isinstance(last_name, str)):
            raise ValueError("Names must be of type str")
        if not (1 <= len(first_name) <= 25 and 1 <= len(last_name) <= 25):
            raise ValueError("Names must be between 1 and 25 characters, inclusive")
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.all_customers.append(self)

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
        




# first_name = "Brian"
# last_name = "Tsalwa"
# customer1 = Customer(first_name, last_name)

# print(customer1.full_name)


class Restaurant:
    all_restaurants = []
    def __init__(self, name):
        if not (isinstance(name, str)):
            raise ValueError("name must be a string")
        if not (1 <= len(name) <= 100):
            raise ValueError("name must not be greater than 100 characters")
        
        
        self._name = name
        self.all_restaurants.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (isinstance(value, str)):
            raise ValueError("name must be a string")
        if not (1 <= len(value) <= 100):
            raise ValueError("name must not be greater than 100 characters")
        self._name = value
        if not (isinstance(value, Customer(uniqu)))

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not (isinstance(value, Customer)):
            raise ValueError("customer must be an instance of Customer class")
        self._customer = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        if not (isinstance(value, list)):
            raise ValueError("reviews must be a list")
        self._reviews = value

# name = "Sushi"
# restaurant1 = Restaurant(name)

# print(restaurant1.name)

class Review:

    def __init__(self, rating, customer, restaurant):
        self.rating = rating
        self.customer = customer
        self.restaurant = restaurant
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be of type Customer.")
        if not isinstance(restaurant, Restaurant):
            raise ValueError("Restaurant must be of type Restaurant.")
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5.")
        self.customer.reviews.append(self)
        self.restaurant.reviews.append(self)

        @property
        def customer(self):
            return self._customer
        @customer.setter
        def customer(self, value):
            if not isinstance(value, Customer):
                raise ValueError("Customer must be of type Customer.")
            self._customer = value

        @property
        def restaurant(self):
            return self._restaurant
        @restaurant.setter
        def restaurant(self, value):
            if not isinstance(value, Restaurant):
                raise ValueError("Restaurant must be of type Restaurant.")
            self._restaurant = value

        @property
        def rating(self):
            return self._rating
        @rating.setter
        def rating(self, value):
            if not isinstance(value, int) or value < 1 or value > 5:
                raise ValueError("Rating must be an integer between 1 and 5.")
            self._rating = value
