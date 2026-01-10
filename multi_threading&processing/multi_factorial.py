import multiprocessing
import math
import sys
import time

#Increase the maximun number of digits for integer conversion
sys.set_int_max_str_digits(100000)

##Function to compute factorial of a given number

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,7000,8000]
    start_time=time.time()

    ##Create a pool of worker processes
    with multiprocessing.Pool(processes=4) as pool:
        results=pool.map(compute_factorial,numbers)

    end_time=time.time()
    print(f"Time taken:{end_time-start_time} seconds")