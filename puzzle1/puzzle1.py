# This file branch is for my curiosity and for comparing execution time speeds.
import timeit

statement = """f = open('input.txt', 'r')

expense_report = [int(line) for line in f]

sorted_expense_report = sorted(expense_report)

# Find the two entries that sum to 2020; what do you get if you multiply them together?
def find_2_num_sum_2020_product(arr):
  j = len(arr) - 1
  i = 0
  found_sum = False
  while(j > i and not found_sum):
    if((arr[i] + arr[j]) > 2020):
      j-=1
    elif((arr[i] + arr[j]) < 2020):
      i+=1
    elif((arr[i] + arr[j]) == 2020):
      found_sum = True
  
  print(arr[i] * arr[j]) if found_sum else print("No sum for 2020 in array.")

# In your expense report, what is the product of the three entries that sum to 2020?
def find_3_num_sum_2020_product(arr):
  k = len(arr) - 1
  j = 1
  i = 0
  found_sum = False
  while(k > j and j > i and not found_sum):
    if((arr[i] + arr[j] + arr[k]) > 2020):
      k-=1
    elif((arr[i] + arr[j] + arr[k]) < 2020):
      if (j - i == 1):
        j+=1
      else:
        i+=1
    elif((arr[i] + arr[j] + arr[k]) == 2020):
      found_sum = True
  print(arr[i] * arr[j] * arr[k]) if found_sum else print("No sum for 2020 in array.")

sorted_expense_report = sorted(expense_report)
find_2_num_sum_2020_product(sorted_expense_report)
find_3_num_sum_2020_product(sorted_expense_report)
"""

print(f"Execution time is: {timeit.timeit(stmt = statement, number = 1)}")

# From https://www.reddit.com/r/adventofcode/comments/k4e4lm/2020_day_1_solutions/
# Comment by u/purplepineapples

statement ="""
with open("input.txt", 'r') as f:
    data = list(map(int, f.read().splitlines()))

sdata = set(data)
slen = len(data)

# a
for x in data:
    target = 2020 - x
    if target in sdata:
        print(x * target)
        break

# b
for i in range(slen):
    y = 2020 - data[i]
    for j in range(i, slen):
        target = y - data[j]
        if target in sdata:
            print(data[i] * data[j] * target)
"""

print(f"Execution time is: {timeit.timeit(stmt = statement, number = 1)}")

# From https://github.com/Axew11/AdventOfCode/blob/master/Advent%20of%20Code%202020/day_1.py

statement="""
with open("input.txt", 'r') as f:
    array = [int(line) for line in f]
    flag = True
    for x in array[:-1]:
        if flag and (2020 - x) in array:
            print(f"Day 1 Part 1: {x * (2020 - x)}")
            flag = False
        for y in array:
            if (2020 - y - x) in array:
                print(f"Day 1 Part 2: {x * y * (2020 - y - x)}")
"""

print(f"Execution time is: {timeit.timeit(stmt = statement, number = 1)}")

# Conclusion (Code only run once)
# First statement: Execution time is: 0.0007472809993487317
# Second statement: Execution time is: 0.002486722998582991
# Third statement: Execution time is: 0.05776282399892807
