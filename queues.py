# Romain Tranchant
# CIS 103 Fundamentals of Programming
# Queue implementation


# Define a class for Queue
class Queue:
# Constructor to initialize the queue as an empty list
    def __init__(self):
# Initialize an empty list to represent the queue
        self.queue = []

# Method to enqueue (add) an item to the queue
    def enqueue(self, item):
# Add the item to the end of the list (rear of the queue)
        self.queue.append(item)

# Method to dequeue (remove) an item from the queue
    def dequeue(self):
# Check if the queue is not empty before trying to dequeue
        if not self.is_empty():
# Remove and return the first item of the list (front of the queue)
            return self.queue.pop(0)
# Return an error message if the queue is empty
        return "Error: Queue is empty"

# Method to peek at the front item of the queue without removing it
    def peek(self):
# Check if the queue is not empty before trying to peek
        if not self.is_empty():
# Return the first item of the list (front of the queue) without removing it
            return self.queue[0]
# Return an error message if the queue is empty
        return "Error: Queue is empty"

# Method to check if the queue is empty
    def is_empty(self):
# Return True if the queue is empty, False otherwise
        return len(self.queue) == 0


# Create a new Queue object
queue = Queue()

# Print a message indicating the items being enqueued
print("Enqueuing the items 10, 20, 30")

# Enqueue items to the queue
queue.enqueue(10)  # Enqueue 10 to the queue
queue.enqueue(20)  # Enqueue 20 to the queue
queue.enqueue(30)  # Enqueue 30 to the queue

# Print the result of dequeuing the first item
print("Dequeued the first item :", queue.dequeue())  # Output: 10

# Print whether the queue is empty
print("Is the queue empty?", queue.is_empty())  # Output: False

# Dequeue the last two items and print their values
print("Dequeuing the last 2 items:", queue.dequeue(), queue.dequeue())  # Output: 20 30

# Print whether the queue is empty after removing all items
print("Is the queue empty?", queue.is_empty())  # Output: True

# Print a separator for better output readability
print("*****************************************")


# Function to simulate a checkout line for customers
def checkout(customers, waiting_time):
    checkout_queue = Queue()  # Create a new Queue to manage the customers in line
    total_time = 0  # Initialize total waiting time

# Iterate through each customer in the list
    for customer in customers:
# Add each customer to the checkout queue
        checkout_queue.enqueue(customer)

# Serve each customer in the queue
        while not checkout_queue.is_empty():
# Print the current customer being served
            print(f"Serving: {checkout_queue.dequeue()}")
# Add the waiting time for the served customer to the total time
            total_time += waiting_time

# After all customers have been served, print the estimated waiting times
    print("Estimated Waiting time per customer: 5 minutes")
# Print the total waiting time
    print(f"Estimated total waiting time: {total_time} minutes")

# List of customers waiting for checkout
customers = ["Alice", "Bob", "Charlie", "Diana"]
# Set the estimated waiting time per customer (in minutes)
waiting_time = 5

# Call the checkout function to simulate the checkout process
checkout(customers, waiting_time)
