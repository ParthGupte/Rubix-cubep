import numpy as np
st=np.array([[' ',' ','R',' '],
             ['Y','B','W','G'],
             [' ',' ','O',' ']])
nul=np.full((3,3),' ')
def cube():
    W=np.full((3,3),'W')
    R=np.full((3,3),'R')
    G=np.full((3,3),'G')
    B=np.full((3,3),'B')
    Y=np.full((3,3),'Y')
    O=np.full((3,3),'O')
    cub={"W":W,"R":R,"G":G,"B":B,"Y":Y,"O":O}
    return cub
def display(cub):
    for i in cub.values():
        print(i)
        print()
def turn(ar,sig):
    C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
    if sig=='+':
        a,b,c,d=list(D[0]),list(L[:,2]),list(U[2]),list(R[:,0])
        print(a,b,c,d)
        L[:,2],U[2],R[:,0],D[0]=a,b,c,d
        print(D[0])
        C=turnface(C,'+')
    elif sig=='-':
        a,b,c,d=list(U[2]),list(R[:,0]),list(D[0]),list(L[:,2])
        L[:,2],U[2],R[:,0],D[0]=a,b,c,d
        C=turnface(C,'-')
    ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]=C,U,L,R,D
    return ar
'''ar=[[' ','U',' '],
       ['L','C','R'], 
       [' ','D',' ']]'''

def turnface(C,sig):
    A=np.full([3,3],'')
    if sig=='+':
        A[:,0],A[0],A[:,2],A[2],A[1,1]=list(C[2]),list(C[:,0])[::-1],list(C[0]),list(C[:,2])[::-1],C[1,1]
        print(C[2])
    elif sig=='-':
        A[:,0],A[0],A[:,2],A[2],A[1,1]=list(C[0])[::-1],list(C[:,2]),list(C[2])[::-1],list(C[:,0]),C[1,1]
    elif sig == 'r0':
        A[0], A[1], A[2] = list(C[2]), list(C[1]), list(C[0])
    elif sig == 'r1':
        A[:,0], A[:,1], A[:,2] = list(C[:,2]), list(C[:,1]), list(C[:,0])
    else:
        A = C.copy()
    return A
def move(m,cub):
    if m[0]=='W':
        C=cub['W']
        L=cub['B']
        R=cub['G']
        U=cub['R']
        D=cub['O']
        ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
        ar=turn(ar,m[1])
        C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
        cub['W']=C
        cub['B']=L
        cub['G']=R
        cub['R']=U
        cub['O']=D
    elif m[0]=='B':
        C=cub['B']
        R=cub['W']
        L=cub['Y']
        U=cub['R']
        U=turnface(U,'-')
        D=cub['O']
        D=turnface(D,'+')
        ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
        ar=turn(ar,m[1])
        C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
        U=turnface(U,'+')
        D=turnface(D,'-')
        cub['B']=C
        cub['Y']=L
        cub['W']=R
        cub['R']=U
        cub['O']=D
    elif m[0]=='Y':
        C=cub['Y']
        L=cub['G']
        R=cub['B']
        U=cub['R']
        U=turnface(U,'-')
        U=turnface(U,'-')
        D=cub['O']
        D=turnface(D,'+')
        D=turnface(D,'+')
        ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
        ar=turn(ar,m[1])
        C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
        U=turnface(U,'+')
        U=turnface(U,'+')
        D=turnface(D,'-')
        D=turnface(D,'-')
        cub['Y']=C
        cub['G']=L
        cub['B']=R
        cub['R']=U
        cub['O']=D
    elif m[0]=='G':
        C=cub['G']
        L=cub['W']
        R=cub['Y']
        U=cub['R']
        U=turnface(U,'+')
        D=cub['O']
        D=turnface(D,'-')
        ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
        ar=turn(ar,m[1])
        C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
        U=turnface(U,'-')
        D=turnface(D,'+')
        print(D,"here")
        cub['G']=C
        cub['W']=L
        cub['Y']=R
        cub['R']=U
        cub['O']=D
    elif m[0]=='R':
        C=cub['R']
        L=cub['B']
        L=turnface(L,'+')
        R=cub['G']
        R=turnface(R,'-')
        U=cub['Y']
        U=turnface(U,'-')
        U=turnface(U,'-')
        D=cub['W']
        ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
        ar=turn(ar,m[1])
        C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
        L=turnface(L,'-')
        R=turnface(R,'+')
        U=turnface(U,'+')
        U=turnface(U,'+')
        cub['R']=C
        cub['B']=L
        cub['G']=R
        cub['Y']=U
        cub['W']=D
    elif m[0]=='O':
        C=cub['O']
        L=cub['B']
        L=turnface(L,'-')
        R=cub['G']
        R=turnface(R,'+')
        U=cub['W']
        D=cub['Y']
        D=turnface(D,'-')
        D=turnface(D,'-')
        ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
        ar=turn(ar,m[1])
        C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
        L=turnface(L,'+')
        R=turnface(R,'-')
        D=turnface(D,'+')
        D=turnface(D,'+')
        cub['O']=C
        cub['B']=L
        cub['G']=R
        cub['W']=U
        cub['Y']=D
    else:
        print("Invalid move")
    return cub

def show(cub):
    for i in cub.values():
        print(i)
        print()

def main():
    print("Welcome!")
    cub=cube()
    show(cub)
    print("Imagine the above arrays to be placed in the following net to understand how the cube is working:")
    print(st)
    print("To turn enter the face you want to turn followed by + or - to indicate clockwise or anticlockwise resp")
    print("For example to turn white face clockwise enter W+")
    print("Clockwise or anticlockwise is as seen while facing the side")
    while True:
        m=input("Enter Move: ")
        if m.lower()=='exit':
            break
        cub=move(m,cub)
        show(cub)
        print(st)

# main()
ar0 = np.array([['1','2','3'],['4','5','6'],['7','8','9']])
ar = turnface(ar0,'-')
print(ar0)
print(ar)