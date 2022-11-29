import time

a = range(10000000)
x = set(a)
y = list(a)

# for set:
start_time = time.time()
for n in x:
    if n == 9999999:
        print(f"For set, found '9999999' at: {time.time() - start_time}")


# for list:
start_time2 = time.time()
for m in y:
    if m == 9999999:
        print(f"For list, found '9999999' at: {time.time() - start_time2}")


