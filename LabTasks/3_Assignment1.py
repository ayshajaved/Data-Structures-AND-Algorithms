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

class stationNode:
    def __init__(self, name, distance):
        self.name = name 
        self.distance = distance #distance from the previous node in km
        self.next = None
        self.prev = None
class Station:
    def __init__(self):
        self.head = None

    #Operations    
    def addStation(self, name, distance):
        node = stationNode(name, distance)
        if not self.head:
            self.head = node
        else:
           node.next = self.head
           self.head.prev = node
           self.head = node
    def addAtStart(self,name, distance):
        #adding the station at start
        if self.head:
            node = stationNode(name, distance)
            self.head.prev = node
            node.next = self.head
            self.head = node
    def addAtEnd(self, name,distance):
         #adding the station at the end
        node = stationNode(name, distance)
        currentNode= self.head
        while(currentNode is not None):
            currentNode = currentNode.next
        currentNode.next = node
        node.prev = currentNode
    def deleteStation(self, name):
        currentNode = self.head
        while(currentNode.name != name):
            # print(currentNode.name)
            currentNode = currentNode.next
        # currentNode.prev.next = currentNode.next
        # currentNode.next.prev = currentNode
    def display(self):
        #Displaying all the stations
        currentNode = self.head
        while(currentNode is not None):
            print(f"Name of the station: {currentNode.name}\nDistance from the previous station(km): {currentNode.distance}")
            currentNode = currentNode.next
    def distanceBetweenTwoStations(self,first, second):
        currentNode = self.head
        distance = 0
        while (currentNode.name != first):
            currentNode = currentNode.next
        while(currentNode.name != second):
            distance += currentNode.distance
            currentNode  = currentNode.next
        print(distance)
    def totalDistance(self):
        totalDistance = 0
        #Finding the total distance of all the nodes
        currentNode= self.head
        while(currentNode is not None):
            totalDistance += currentNode.distance
            currentNode = currentNode.next
        return totalDistance
stationRouteSystem = Station()
print("******************************")
print("Displaying all the Stations..")
print("*******************************")
stationRouteSystem.addStation("Station 1", 10)
stationRouteSystem.addStation("Station 2", 20)
stationRouteSystem.addStation("Station 3", 30)
stationRouteSystem.addStation("Station 4",40)
stationRouteSystem.addStation("Station 5", 50)
stationRouteSystem.addAtStart("Station 0", 3)
# stationRouteSystem.addAtEnd("station 8", 34)
stationRouteSystem.display()

#displaying the total distance
print("\nTotal distance of all the stations: ")
print(stationRouteSystem.totalDistance())
print()

#Deleting the node
print("After Deleting..")
stationRouteSystem.deleteStation("Station 1")
stationRouteSystem.display()

#calculating the distance between two stations
print("Distance Between Two Stations: ")
print(stationRouteSystem.distanceBetweenTwoStations("Station 2", "Station 5"))














