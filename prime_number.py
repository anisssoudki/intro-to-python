def say_hi(name):
    print(f'hello {name}')

name = input('whats ur name ')

say_hi(name)

def check_prime(num):
    is_prim = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            print(f'{num} is not prime number')
            break
        else: 
            print (f'{num} is a prime number')
            break
num = int(input('enter number '))

check_prime(num)
