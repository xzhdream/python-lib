import time
from concurrent.futures.process import ProcessPoolExecutor

def main():
    with ProcessPoolExecutor(max_workers=2) as ex:
        future = ex.submit(pow,2,4)
        print('-----')

        print(future.result())
        print('=====')

if __name__ == '__main__':
    main()

