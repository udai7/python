import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logging=logging.getLogger("ArithmeticApp")

def add(a,b):
    logging.debug("The addition operation is taking place")
    return a+b

def subtract(a,b):
    logging.debug("The subtraction operation is taking place")
    return a-b

def multiply(a,b):
    logging.debug("The multiplication operation is taking place")
    return a*b

def divide(a,b):
    logging.debug("The division operation is taking place")
    return a/b

add(10,15)
subtract(10,15)
multiply(10,15)
divide(10,2)