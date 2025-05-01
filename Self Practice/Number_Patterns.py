#              Printing Number Patterns              #
#____________________________________________________#
n=5
for i in range(n):
    for j in range(n):
        print(i,end=' ')
    print()

print('_'*20)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(n):
        print(i+1,end=' ')
    print()

print('_'*20)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i,n):
        print(i+1,end=' ')
    print()

print('_'*20)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i+1):
        print(i+1,end=' ')
    print()

print('_'*20)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i+1):
        print('',end='   ')
    for j in range(i,n):
        print(i+1,end='  ')
    print()

print('_'*20)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i,n):
        print('',end='   ')
    for j in range(i+1):
        print(i+1,end='  ')
    print()

print('_'*50)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i,n):
        print(i+1,end='  ')
    print()
for i in range(n):
    for j in range(i+1):
        print(i+1,end='  ')
    print()    
for i in range(n):
    for j in range(i+1):
        print('',end='   ')
    for j in range(i,n):
        print(i+1,end='  ')
    print()
for i in range(n):
    for j in range(i,n):
        print('',end='   ')
    for j in range(i+1):
        print(i+1,end='  ')
    print()

print('_'*50)
#____________________________________________________#