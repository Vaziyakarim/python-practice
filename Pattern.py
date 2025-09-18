#Pyramid
# # rows = 5

# for i in range(1, rows + 1):

#     print(" " * (rows - i), end="")
  
#     for j in range(1, i + 1):
#         print(j, end="")
   
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print()

#Diamond
rows = 5


for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
