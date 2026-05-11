from stack_file import Stack
from queue_file import Queue

# 1. Reverse a String Using a Stack
def reverse_str(str):
    stack = Stack()
    for char in str:
        stack.push(char)
    reverse_string = ""
    for char in stack:
        reverse_string += stack.pop()
    
    return reverse_string

# 2. For each temperature find how many days until a warmer temperature.
#ex: [22, 18, 28, 32, 25, 20, 23]
#out: [2, 1, 1, 0, 0, 1, 0]
def daily_temperatures(temperatures):
    stack = Stack()
    result = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while not stack.is_empty() and temp > temperatures[stack.peek()]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.push(i)

    return result

# 3. First Non-Repeating Character in a Stream. As characters arrive return the first non-repeating one
def first_not_repeat(stream):
    queue = Queue()
    characters = {}
    for char in stream:
        char_count[char] = char_count.get(char, 0) + 1
        queue.enqueue(char)
        while not queue.is_empty() and char_count[queue.peek()] > 1:
            queue.dequeue()

        if not queue.is_empty():
            print(queue.peek())
        else:
            print("No non-repeating character")
        