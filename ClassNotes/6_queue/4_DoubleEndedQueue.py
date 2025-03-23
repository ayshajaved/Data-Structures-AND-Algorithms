'''
Double ended queue is the queue in which the insertion and deletion occurs from both ends
'''
class Dequeue:
    def __init__(self):
        self.dequeue = []
    
    def get_size(self):
        return len(self.dequeue)

    def is_empty(self):
        return len(self.dequeue)==0
    
    def add_front(self, value):
        self.dequeue.insert(0, value)

    def add_rear(self, value):
        self.dequeue.append(value)    
            
    def print_queue(self):
        if self.is_empty():
            print("Queue cannot be printed.. It's empty")
        print(self.dequeue)
    
    def remove_front(self):
        if not self.is_empty():
            self.dequeue.pop(0)
        raise IndexError ("Queue is empty")
    
    def remove_rear(self):
        if not self.is_empty():
            self.dequeue.pop()

class Main:
    @staticmethod
    def run():
        queue =Dequeue()
        queue.add_front(2)
        queue.add_front(3)
        queue.add_rear(4)
        queue.add_rear(9)

        queue.print_queue()

if __name__ == "__main__":
    Main.run()