#for x in range(8,9):
#    for y in range(1,11):
#        print('%d * %d = %d' %(x,y,x*y))
#
#range function is used to generate a sequence of numbers.
#syntax of range function is range(start, stop, step)
# start: the starting number of the sequence (inclusive)
# stop: the end number of the sequence (exclusive)
# step: the difference between each number in the sequence (optional, default is 1)
# Example: range(1, 10, 2) generates the sequence 1, 3, 5, 7, 9
# Example: range(10) generates the sequence 0, 1, 2, ..., 9
# Example: range(5, 10) generates the sequence 5, 6, 7, 8, 9
# Example: range(5, 10, 2) generates the sequence 5, 7, 9
# Example: range(10, 5, -1) generates the sequence 10, 9, 8, 7, 6
# Example: range(10, 5, -2) generates the sequence 10, 8, 6
# Example: range(5, 10, -1) generates an empty sequence because the start is greater than the stop and the step is positive

#n = 5
#for rows in range(1, n+1):
#    for columns in range(1,rows+1):
#        print('*', end= ' ')
#    print()

n = 6
for rows in range(1,n+1): # rows = 2
    for columns in range(1, rows+1): # Columns = 1,3 => 1,2
        print(rows, end=' ')
    print()

n = 5
for rows in range(1,n+1): # rows = 5
    for columns in range(1, rows+1): # Columns = [1,2,3,4,5,6] => 1,2,3,4,5
        print(columns, end=' ')
    print()
print('*'*50)
n = 8
for rows in range(1,n+1):  #rows = [1,2,3,4,5,6,7,8] => 1,2,3,4,5,6,7,8
    for columns in range(1,n-rows+2): #Columns = [1,2,3,4,5,6,7] => 1,2,3,4,5,6,7
        print(rows, end=' ')
    print()
print('*'*50)
n = 8
for rows in range(1,n+1):  
    #rows = [1,2,3,4,5,6,7,8] => 1,2,3,4,5,6,7,8
    for columns in range(1,n-rows+2): 
    #Columns = [1,2,3,4,5,6,7] => 1,2,3,4,5,6,7
        print(columns, end=' ')
    print()
print('*'*50)
n = 8
for rows in range(1,n+1):  
    for columns in range(rows,n+1): 
        print(columns, end=' ')
    print()

print('*'*50)
n = 8
for rows in range(1,n+1):  
    for columns in range(rows,n+1): 
        print(columns, end=' ')
    print()