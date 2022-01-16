import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 3)
    f2 = executor.submit(do_something, 1)
    f3 = executor.submit(do_something, 4)
    f4 = executor.submit(do_something, 2)

    print(f1.result())
    print(f2.result())
    print(f3.result())
    print(f4.result())

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')