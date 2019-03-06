import Input
import State
import AStar
import time

def h1h2():
    for i in range(10):
        table = Input.Input(1)
        print("h1(n):", end=' ')
        test = AStar.AStar(table, 1)
        time_start = time.time()
        test.run()
        time_end = time.time()
        print('Cost:', time_end - time_start, 's')

        print("h2(n):", end=' ')
        test = AStar.AStar(table, 2)
        time_start = time.time()
        test.run()
        time_end = time.time()
        print('Cost:', time_end - time_start, 's')

def h1():
    table = Input.Input(0)
    test = AStar.AStar(table, 1)
    test.run()

def h2():
    table = Input.Input(0)
    test = AStar.AStar(table, 2)
    test.run()

print("h1(n):")
h1()
print('-------------------------------------------------------------')
print("h2(n):")
h2()

input()