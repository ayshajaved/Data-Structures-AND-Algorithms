'''
Create a Station Node:
Each station will have the following attributes:
-Station Name
-Distance from Previous Station (in km)
-Next Station pointer
-Previous Station pointer

Operations to Implement:
Add a station at the beginning of the route.
Add a station at the end of the route.
Add a station at a specific position in the route.

Remove a Station from the Route:
Remove a station by its position in the route.
Remove the first station in the route.
Remove the last station in the route.

Display the Entire Route:
Display the route in both forward (start to end) and reverse (end to start) order, showing the
station names and distances between them.

Find the Total Distance:
Implement a function to calculate and display the total distance of the entire route from the
first to the last station.

Find Shortest Path Between Two Stations:
Implement a function that takes two station names and calculates the total distance between
them by traversing the route.

Bonus Challenge:
Optimize for Multiple Routes:
Allow the creation and management of multiple routes (e.g., Route A, Route B, Route
C). Each route should be managed independently using a doubly linked list, and users
should be able to switch between routes for modifications or queries.
'''
#Solution
'''
Lab Assignment:1
Name : ayesha javed
Roll number: sp24-bse-020-B

Station Route System:
--> Class of Station Node
--> Class of Station

Attributes:
1: Station name
2: Distance from the previous station in km
3: Next pointer
4: previous pointer

Methods:
1: Add Station
2: delete Station
3: Display Stations
'''

class StationNode:
    def __init__(self, name, distance=0):
        self.name = name 
        self.distance_from_prev = distance #distance from the previous node in km
        self.next = None
        self.prev = None
class Route:
    def __init__(self, routeName):
        self.head = None
        self.tail = None
        self.route_name = routeName
    #Route Operations    
    def add_station_beginning(self, name, distance_from_prev=0):
        new_station = StationNode(name, distance_from_prev)
        if not self.head:
            self.head = self.tail = new_station
        else:
            new_station.next = self.head
            self.head.prev = new_station
            self.head = new_station

    # Add station at end
    def add_station_end(self, name, distance_from_prev):
        new_station = StationNode(name, distance_from_prev)
        if not self.head:
            self.head = self.tail = new_station
        else:
            new_station.prev = self.tail
            self.tail.next = new_station
            self.tail = new_station

    # Add station at specific position (1-based index)
    def add_station_at_position(self, name, position, distance_from_prev):
        if position < 1:
            print("Position must be positive")
            return
        
        new_station = StationNode(name, distance_from_prev)
        if not self.head or position == 1:
            self.add_station_beginning(name, distance_from_prev)
            return

        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            self.add_station_end(name, distance_from_prev)
        else:
            new_station.next = current.next
            new_station.prev = current
            current.next.prev = new_station
            current.next = new_station

    # Remove first station
    def remove_first(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # Remove last station
    def remove_last(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # Remove station at position (1-based index)
    def remove_at_position(self, position):
        if not self.head or position < 1:
            return

        if position == 1:
            self.remove_first()
            return

        current = self.head
        count = 1
        while current and count < position:
            current = current.next
            count += 1

        if not current:
            return
        if current == self.tail:
            self.remove_last()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    # Display forward
    def display_forward(self):
        if not self.head:
            print(f"{self.route_name}: Empty route")
            return
        print(f"{self.route_name} Forward:")
        current = self.head
        while current:
            if current.next:
                print(f"{current.name} --({current.next.distance_from_prev}km)--> ", end="")
            else:
                print(f"{current.name}")
            current = current.next

    # Display reverse
    def display_reverse(self):
        if not self.head:
            print(f"{self.route_name}: Empty route")
            return
        print(f"{self.route_name} Reverse:")
        current = self.tail
        while current:
            if current.prev:
                print(f"{current.name} <--({current.distance_from_prev}km)-- ", end="")
            else:
                print(f"{current.name}")
            current = current.prev

    # Calculate total distance
    def total_distance(self):
        if not self.head:
            return 0
        total = 0
        current = self.head.next
        while current:
            total += current.distance_from_prev
            current = current.next
        return total

    # Find distance between two stations
    def distance_between(self, start_name, end_name):
        if not self.head:
            return -1

        # Find start station
        current = self.head
        while current and current.name != start_name:
            current = current.next
        if not current:
            print(f"Station {start_name} not found")
            return -1

        # Search forward
        total_forward = 0
        temp = current
        while temp and temp.name != end_name:
            if temp.next:
                total_forward += temp.next.distance_from_prev
            temp = temp.next
        if temp:
            return total_forward

        # Search backward
        total_backward = 0
        temp = current
        while temp and temp.name != end_name:
            if temp.prev:
                total_backward += temp.distance_from_prev
            temp = temp.prev
        if temp:
            return total_backward

        print(f"Station {end_name} not found")
        return -1

class RouteManager:
    def __init__(self):
        self.routes = {}

    def create_route(self, routeName):
        if routeName not in self.routes:
            self.routes[routeName] = Route(routeName)
            print(f"Created route: {routeName}")
        else:
            print(f"Route {routeName} already exists")

    def get_route(self, route_name):
        return self.routes.get(route_name)

#Route A created
manager = RouteManager()
manager.create_route("Route A")
route_a = manager.get_route("Route A")

print("******************************")
print("    Station Route System")
print("******************************")

route_a.add_station_beginning("Station 1")
route_a.add_station_end("Station 2", 5)
route_a.add_station_end("Station 3", 3)
route_a.add_station_at_position("Station 4", 2, 2)

route_a.display_forward()
route_a.display_reverse()

print(f"Total distance: {route_a.total_distance()}km")
print(f"Distance between Station 1 and Station 3: {route_a.distance_between('Station 1', 'Station 3')}km")

# Create and populate Route B
manager.create_route("Route B")
route_b = manager.get_route("Route B")
route_b.add_station_beginning("City 1")
route_b.add_station_end("City 2", 10)
route_b.add_station_end("City 3", 42)

# Demonstrate operations
route_a.remove_at_position(2)
print("\nAfter removing position 2:")
route_a.display_forward()

#Displaying Route B
route_b.display_forward()