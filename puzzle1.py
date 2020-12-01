f = open('input.txt', 'r')
expense_report = []

for line in f:
  line = int(line.replace('\n', ''))
  expense_report.append(line)

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

find_2_num_sum_2020_product(sorted_expense_report)
find_3_num_sum_2020_product(sorted_expense_report)