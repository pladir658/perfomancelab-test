import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
IntrvlWay = str(1)
m -= 1
i = m 
while i%n != 0:
    IntrvlWay += ' ' + str(i%n+1)
    i += (m)
print(IntrvlWay)