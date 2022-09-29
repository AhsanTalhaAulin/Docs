import threading

def print_cube(num):
    print("Cube: {}". format(num * num * num))

def print_square(num):
    print("Square: {}". format(num * num))

def print_circle(num):
    print("Circle: {}". format(3.1416 * num * num))


t1 = threading.Thread(target=print_cube, args=(10, ))
t2 = threading.Thread(target=print_square, args=(6, ))
t3 = threading.Thread(target=print_circle, args=(100, ))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()