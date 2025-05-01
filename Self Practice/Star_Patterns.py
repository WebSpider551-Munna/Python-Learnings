# Printing Star Patterns
'''n=5
for j in range(n):
    print(' * '*n) '''
print('_'*20)
#____________________________________________________#
n=5
for i in range(n):
    for j in range(n):
        print(' * ',end='')
    print()

print('_'*20)
#____________________________________________________#
n=5
for i in range(n):
    for j in range(i+1):
        print(' * ',end='')
    print()

print('_'*20)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i,n):
        print(' * ',end='')
    print()

print('_'*20)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i,n):
        print('   ',end='')
    for j in range(i+1):
        print(' * ',end='')
    print()

print('_'*20)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i+1):
        print('   ',end='')
    for j in range(i,n):
        print(' * ',end='')
    print()

print('_'*20)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i,n):
        print(' _ ',end='')
    for j in range(i+1):
        print(' * ',end='')
    for j in range(i+1):
        print(' - ',end='')
    for j in range(i,n):
        print(' * ',end='')

    print()

print('_'*50)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i,n):
        print('   ',end='')
    for j in range(i):
        print(' * ',end='')
    for j in range(i+1):
        print(' * ',end='')


    print()

print('_'*50)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i+1):
        print('   ',end='')
    for j in range(i,n-1):
        print(' * ',end='')
    for j in range(i,n):
        print(' * ',end='')


    print()

print('_'*50)
#____________________________________________________#

n=5
for i in range(n-1):
    for j in range(i,n):
        print('   ',end='')
    for j in range(i):
        print(' * ',end='')
    for j in range(i+1):
        print(' * ',end='')
    print()
for i in range(n):
    for j in range(i+1):
        print('   ',end='')
    for j in range(i,n-1):
        print(' * ',end='')
    for j in range(i,n):
        print(' * ',end='')
    print()

print('_'*50)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i+1):
        print('   ',end='')
    for j in range(i,n-1):
        print(' * ',end='')
    for j in range(i,n):
        print(' * ',end='')
    print()
for i in range(n):
    for j in range(i,n):
        print('   ',end='')
    for j in range(i):
        print(' * ',end='')
    for j in range(i+1):
        print(' * ',end='')
    print()
print('_'*50)
#____________________________________________________#

n=5
for i in range(n):
    for j in range(i+1):
        print('   ',end='')
    for j in range(i,n):
        print(' * ',end='')
    print()
for i in range(n):
    for j in range(i,n):
        print('   ',end='')
    for j in range(i):
        print('   ',end='')
    for j in range(i+1):
        print(' * ',end='')
    print()
print('_'*50)
#____________________________________________________#