class Car:
    _all = []

    def __init__(self, make, model, year, owner=None):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner  # Owner attribute

        # Add the car instance to the list of all cars
        Car._all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner

    # Other methods as needed

