'''
Priority Queue to develop a task schedular system, that prioritizes the task based on their execution time and the maximum time is given

- They should not exceed the maximum time
- Priotiy queue must be used
'''
import heapq

class TaskScheduler:  # Fixed typo in class name
    def __init__(self, tasks, max_time):
        self.max_time = max_time
        self.queue = [] 
        self.total_time = 0 
        self.tasks = tasks  
        self.scheduled_tasks = [] 
        
        # Add tasks during initialization
        for task_id, execution_time in self.tasks:
            self.add_task(task_id, execution_time)

    def add_task(self, task_id, execution_time):
        if self.total_time + execution_time <= self.max_time:
            heapq.heappush(self.queue, (execution_time, task_id))
            self.total_time += execution_time
            self.scheduled_tasks.append(task_id)
        else:
            print(f"Task {task_id} (execution time: {execution_time} ms) exceeds max_time. Skipped.")

    def get_scheduled_tasks(self):
        task_dict = {task_id: exec_time for task_id, exec_time in self.tasks}
        return sorted(self.scheduled_tasks, key=lambda x: task_dict[x])

class Main:
    @staticmethod
    def run():
        tasks = [
            (1, 10),  
            (2, 15),  
            (3, 5),   
            (4, 20),  
            (5, 5)    
        ]
        max_time = 30
        scheduler = TaskScheduler(tasks, max_time)    
        # Print results
        scheduled_tasks = scheduler.get_scheduled_tasks()
        print("Scheduled tasks:", scheduled_tasks)
        print("Total execution time:", scheduler.total_time, "ms")

if __name__ == "__main__":
    Main.run()