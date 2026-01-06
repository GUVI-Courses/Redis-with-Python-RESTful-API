# Function with parameters and return value

def add(a, b):
    return a + b

result = add(5, 3)
print("Addition Result:", result)


# Default and keyword arguments
def greet(name="Guest"):
    print("Hello", name)

greet()
greet(name="Ojas")
