class Customer():
    all = []
    def __init__(self, first_name, last_name):
        if not (isinstance(first_name, str) and isinstance(last_name, str)):
            raise ValueError("Names must be of type str")
        if not (1 <= len(first_name) <= 25 and 1 <= len(last_name) <= 25):
            raise ValueError("Names must be between 1 and 25 characters, inclusive")
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.all.append(self)


    @property
    def name(self):
        return self.full_name


# first_name = "Brian"
# last_name = "Tsalwa"
# customer1 = Customer(first_name, last_name)

# print(customer1.name)


class Restaurant:
    all = []
    def __init__(self, name):
        if not (isinstance(name, str)):
            raise ValueError("name must be a string")
        if not (1 <= len(name) <= 100):
            raise ValueError("name must not be greater than 100 characters")
        self._name = name
        self.all.append(self)


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

# name = "Sushi"
# restaurant1 = Restaurant(name)

# print(restaurant1.name)
    
   
   




class Review:
    def __init__(self, customer, restaurant, rating):
        if not (isinstance(customer, Customer) and isinstance(restaurant, Restaurant)):
            raise ValueError("customer and restaurant must be instances of Customer and Restaurant classes")
        if not (isinstance(rating, int) and 1 <= rating <= 5):
            raise ValueError("rating must be an integer between 1 and 5, inclusive")
        self.customer = customer
        self.restaurant = restaurant
        self._rating = rating

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("customer must be an instance of the Customer class")
        self._customer = value

    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, value):
        if not isinstance(value, Restaurant):
            raise ValueError("restaurant must be an instance of the Restaurant class")
        self._restaurant = value

    @rating.setter
    def rating(self, value):
        raise AttributeError("rating attribute cannot be changed after the Review object is initialized")
        self.rating = value
