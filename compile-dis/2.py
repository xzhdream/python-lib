import sys

pi = 3.14

def square(r):
    frame = sys._getframe()
    while frame:
        print('#', frame.f_code.co_name)
        print('Locals:', list(frame.f_locals.keys()))
        print('Globals:', list(frame.f_globals.keys()))
        print()

        frame = frame.f_back

    return r ** 2

def circle_area(r):
    return pi * square(r)

def main():
    print(circle_area(5))

if __name__ == '__main__':
    main()