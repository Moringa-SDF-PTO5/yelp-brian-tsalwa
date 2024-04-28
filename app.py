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

    def __init__(self, id: int, rating: int, customer: 'Customer', restaurant: 'Restaurant'):

        self.id = id

        self.rating = rating

        self.customer = customer

        self.restaurant = restaurant