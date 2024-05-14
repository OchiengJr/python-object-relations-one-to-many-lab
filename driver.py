from typing import List

# Assuming the Trip class is defined elsewhere and imported here
class Trip:
    def __init__(self, destination: str, distance: float, duration: float):
        self.destination = destination
        self.distance = distance
        self.duration = duration

    def summary(self) -> str:
        return f"Trip to {self.destination}: {self.distance} km in {self.duration} hours"

class Driver:
    def __init__(self, name: str):
        """
        Initialize a Driver instance.

        :param name: The name of the driver.
        """
        self.name = name
        self.trips: List[Trip] = []

    def add_trip(self, trip: Trip) -> None:
        """
        Add a trip to the driver's list of trips.

        :param trip: A Trip instance to be added.
        """
        self.trips.append(trip)

    def my_trips(self) -> List[Trip]:
        """
        Return the list of trips for the driver.

        :return: A list of Trip instances.
        """
        return self.trips

    def my_trip_summaries(self) -> List[str]:
        """
        Return summaries of all trips for the driver.

        :return: A list of trip summaries.
        """
        return [trip.summary() for trip in self.trips]

# Example usage:
# driver = Driver("John Doe")
# trip1 = Trip("New York", 300, 5)
# trip2 = Trip("Boston", 200, 3.5)
# driver.add_trip(trip1)
# driver.add_trip(trip2)
# print(driver.my_trips())  # Should print the list of trips
# print(driver.my_trip_summaries())  # Should print the summaries of trips
