import sys
file_1 = open(sys.argv[1],'r')
Circle = file_1.read()  
X0 = float(Circle[:Circle.index(' ')])
Y0 = float(Circle[Circle.index(' '):Circle.index('\n')])
Rad = float(Circle[Circle.index('\n')+1:])
file_1.close
Rad = Rad**2
Points = str()
file_2 = open(sys.argv[2],'r')
for line in file_2:
    X1 = float(line[:line.index(' ')]) - X0
    Y1 = float(line[line.index(' '):line.index('\n')]) - Y0
    SquareVector = X1**2 + Y1**2
    Points += str((SquareVector != Rad) + (SquareVector > Rad)) + '\n'  
file_2.close
print(Points)