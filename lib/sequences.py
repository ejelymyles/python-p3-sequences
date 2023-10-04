#!/usr/bin/env python3

def print_fibonacci(length):
        
    if length <= 0:
        print("[]")
        return

    a, b = 0, 1

   
    fibonacci_sequence = []

    for _ in range(length):
        fibonacci_sequence.append(a)  
        a, b = b, a + b               

  
    print(fibonacci_sequence)
    pass