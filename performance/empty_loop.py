import time


def heavy_work():
    for _ in range(1_000_000):
        pass

start_time = time.time()
heavy_work()
end_time = time.time()
print(f'Duraction: {end_time - start_time}')