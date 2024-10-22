
# Solution by Gauss-Jordan Elimination / RREF
print('')
print('Enter first matrix A')
matrix=[]
while 1:
    x=input().split()
    if x!=[]:
        matrix.append(list(map(float,x)))
    else:
        break
print('Enter second matrix B HORIZONTALLY')
B=list(map(float, input().split()))
for i in range(len(B)):
    (matrix[i]).append(B[i])
print('')

def f():
    # print('f()',matrix)
    print("This matrix is just for your reference.")

    for i in range(noofrow):
        print('[',end='')
        for j in range(noofcol):
            ele=round(matrix[i][j],7)
            m=list(str(ele))
            n=['-','0','.','0']
            if m == n:
                ele=0.0
            l=len(str(ele))
            print(' '*(10-l),ele,end='')
        print('  ]')

    print('')
    checkrow=len(matrix)-1;zeros=[]
    sol=[]
    for i in range(len(matrix)):
        sol.append(0)
    
    while checkrow>=0:
        checkcol=len(matrix[0])-2;zeros=0
        while checkcol>=0:
            ele=round(matrix[checkrow][checkcol],7)
            m=list(str(ele))
            n=['-','0','.','0']
            if m == n:
                ele=0.0
            if ele == 1.0 :
                sol[checkrow] = matrix[checkrow][-1]
                checkrow-=1;checkcol-=1
                continue
            elif ele == 0.0 :
                zeros+=1
                checkcol-=1
                continue
            else:
                print('A free variable encountered')
                print("")
                print("Press Enter to Exit")
                hfhg=input()
                quit()
        if zeros == len(matrix[0])-1:
            print('Zero row encountered')
            print("")
            print("Press Enter to Exit")
            hfhg=input()
            quit()
    
    print('')
    for i in range(len(sol)):
        print('X'+str(i+1)+' =',round(sol[i],7))



noofrow=len(matrix); noofcol=len(matrix[0])
checkrow=0
while checkrow<noofrow:
    checkcol=0
    while checkrow<noofrow and checkcol<noofcol:
        # print('checkrow=',checkrow,'and checkcol=',checkcol)


        if (matrix[checkrow]).count(0.0) == noofcol:
            # print('Zero Row')
            checkrow+=1
            break
        
        element=matrix[checkrow][checkcol]
        if element == 0:
            for i in range(checkrow+1,noofrow):
                if matrix[i][checkcol] != 0:
                    (matrix[checkrow],matrix[i]) = (matrix[i],matrix[checkrow])
                    break
        # print('line49',matrix)
        

        element=matrix[checkrow][checkcol]
        # print('element is',element)
        if element == 0:
            checkcol += 1
            continue
        if element != 0:
            for i in range(noofcol):
                matrix[checkrow][i] /= element
        for i in range(checkrow+1,noofrow):
            ratio = (matrix[i][checkcol]) / (matrix[checkrow][checkcol])
            if ratio != 0:
                for j in range(checkcol,noofcol):
                    matrix[i][j] -= (ratio)*(matrix[checkrow][j])
        # print('line65',matrix)

        checkrow+=1
        checkcol+=1


checkrow=0
while checkrow<noofrow:
        if (matrix[checkrow]).count(0.0) == noofcol:
            # print('Zero Row')
            rowno=noofrow-1
            while rowno>checkrow:
                if (matrix[rowno]).count(0.0) < noofcol:
                    (matrix[checkrow],matrix[rowno]) = (matrix[rowno],matrix[checkrow])
                    break
                rowno-=1
            checkrow+=1
            break
        checkrow+=1

# print('line70',matrix)


r=0
i=len(matrix)-1
while i>=0:
    j=len(matrix[0])-1
    while j>=0:
        if matrix[i][j] == 1.0:
            r=1;checkrow=i;checkcol=j
            break
        j-=1
    if r==1:
        break
    i-=1
# print(checkrow,checkcol)


while checkrow>0:
    while checkcol>0:
        if matrix[checkrow][checkcol] == 1.0:
            for i in range(checkrow-1,-1,-1):
                ratio=matrix[i][checkcol]
                for j in range(checkcol,noofcol):
                    matrix[i][j]-=(matrix[checkrow][j])*(ratio)
            checkrow-=1
            checkcol-=1
        else:
            checkcol-=1
    checkrow-=1


f()

print("")
print("Press Enter to Exit")
hfhg=input()