# pyramid

# for row in range(1,7):
#     for col in range(1,row+1):
#         print("* ",end="\t")
#     print()

# reverse
# for row in range(7,1,-1):
#     for col in range(row,1,-1):
#         print("* ",end="\t")
#     print()

for row in range(1,7):
    for space in range(6,row,-1):
        print(end="  ")
    for col in range (1,row+1):
            print("*  ",end=" ")
    print()