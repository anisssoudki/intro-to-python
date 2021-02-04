import random
 
# The limit for the extended ASCII Character set
MAX_LIMIT = 255
 
random_string = ''
 
for _ in range(10):
    random_integer = random.randint(0, MAX_LIMIT)
    # Keep appending random characters using chr(x)
    random_string += (chr(random_integer))
 
print(random_string, len(random_string))

random_string2 = ''
 
for _ in range(10):
    # Considering only upper and lowercase letters
    random_integer = random.randint(97, 97 + 26 - 1)
    flip_bit = random.randint(0, 1)
    # Convert to lowercase if the flip bit is on
    random_integer = random_integer - 32 if flip_bit == 1 else random_integer
    # Keep appending random characters using chr(x)
    random_string2 += (chr(random_integer))
 
print(random_string2, len(random_string))

 
random.seed(1)
 
# Get the state of the generator
state = random.getstate()
 
print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))
 
# Restore the state to a point before the sequence was generated
random.setstate(state)
print('Generating the same identical sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))
