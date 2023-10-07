import random
import time


def double_first_amount(amounts):
    # Solve ZeroDivisionError
    time.sleep(1)
    return amounts[0] * 2

def sum_odd_amounts(amounts):
    total_sum = 0
    # Solve ZeroDivisionError
    time.sleep(1)
    for a in amounts:
        if a % 2:
            total_sum += a
    return total_sum

random_amounts = [random.randint(1, 100) for _ in range(10_000_000)]

start_time = time.time()
double_first_amount(random_amounts)
end_time = time.time()
double_duration = end_time - start_time

start_time = time.time()
sum_odd_amounts(random_amounts)
end_time = time.time()
sum_duration = end_time - start_time

print(f'Duration double: {double_duration}')
print(f'Duration sum: {sum_duration}')
print(f'Ratio of durations {sum_duration/double_duration}')