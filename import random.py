import random
grid = [" "] * 5


'''for row in range(5):
   row_list = []
   for col in range(5):
       row_list.append(" ")
   grid.append(row_list)'''
for i in grid:
    random_col = random.randint(0, 1)
    if random_col == 1:
      grid[random_col] = "X"
      print(random_col)

print(grid)
