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
        