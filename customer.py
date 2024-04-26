class Customer():
    def __init__(self, first_name, last_name):
        if not (isinstance(first_name, str) and isinstance(last_name, str)):
            raise ValueError("Names must be of type str")
        if not (1 <= len(first_name) <= 25 and 1 <= len(last_name) <= 25):
            raise ValueError("Names must be between 1 and 25 characters, inclusive")
        self.first_name = first_name
        self.last_name = last_name