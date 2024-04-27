class Customer():
    all = []
    def __init__(self, first_name, last_name):
        if not (isinstance(first_name, str) and isinstance(last_name, str)):
            raise ValueError("Names must be of type str")
        if not (1 <= len(first_name) <= 25 and 1 <= len(last_name) <= 25):
            raise ValueError("Names must be between 1 and 25 characters, inclusive")
        self.first_name = first_name
        self.last_name = last_name
        self._customer_objects.append(self)

  
class Restaurant:
    all = []
    def __init__(self, name, ):
        self.name = name
        if not (isinstance(name, str)):
            raise ValueError("name must be a string")
        if not (1 <= len(name) <= 100 ):
            raise ValueError("name must not be greater than 100")
    @property
    def name(self):
        return 




class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
