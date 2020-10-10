from concurrent.futures.thread import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = executor.map(lambda a:print(a), [x for x in range(10)])
    for future in futures:
        print(future)

