f = open('input.txt', 'r')
my_input = [line.strip('\n') for line in f]

def count_num_trees(right_traverse_count, down_traverse_count, course):
  right = 0
  down = 0
  line_len = len(course[0])
  encounter = []
  for line in course:
    if down % down_traverse_count == 0:
      encounter.append(line[right])
      right += right_traverse_count
    if right > line_len - 1:
      right = right % line_len
    down += 1
    
  count = 0
  for item in encounter:
    if item == '#':
      count +=1
  
  return count

# First part
print(
  count_num_trees(3,1,my_input)
)

# Second part
print(
  count_num_trees(1, 1, my_input)*
  count_num_trees(3, 1, my_input)*
  count_num_trees(5, 1, my_input)*
  count_num_trees(7, 1, my_input)*
  count_num_trees(1, 2, my_input)
)