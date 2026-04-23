# Generate a random integer between min and max using random.random() with a specific distance (max - min)
import random
def randInt(max=100, min=0):
    if min > max:
        min, max = max, min

    if max < 0:
        return "Max cannot be less than 0"
    
    num = random.random() * (max - min) + min

    return round(num)

print(randInt()) 
print(randInt(max=50))
print(randInt(min=50)) 
print(randInt(min=50, max=500))
print(randInt(max=-20))
print(randInt(min=100, max=50))