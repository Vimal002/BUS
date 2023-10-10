import random

def generate_random_port():
    # Generate a random port number between 1024 and 65535
    return random.randint(1024, 65535)

# Generate and print a random port number
random_port = generate_random_port()
print("Random Port:", random_port)
