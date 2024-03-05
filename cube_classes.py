import numpy as np
st=np.array([[' ',' ','R',' '],
             ['Y','B','W','G'],
             [' ',' ','O',' ']])
nul=np.full((3,3),' ')

class Cube:
    def __init__(self) -> None:
        self.W = np.full((3,3),'W')
        self.R = np.full((3,3),'R')
        self.G = np.full((3,3),'G')
        self.B = np.full((3,3),'B')
        self.Y = np.full((3,3),'Y')
        self.O = np.full((3,3),'O')
        self.cub = {"W":self.W,"R":self.R,"G":self.G,"B":self.B,"Y":self.Y,"O":self.O}
        self.face_map = {'W':['B','G','R','O'],'B':['Y','W','R','O'],'G':['W','Y','R','O'],'Y':['G','B','R','O'],'R':['B','G','Y','W'],'O':['B','G','W','Y']}
        self.turn_map = {'W':['','','','',''],'B':['','','-','+'],'G':['','','+','-'],'Y':['','','++','++'],'R':['+','-','++',''],'O':['-','+','','++']}
        
    def display(self):
        cub = self.cub
        for i in cub.values():
            print(i)
            print()
    
    def score(self):
        '''Returns what percent of the cube is solved
        How many peices are in the correct position and orientation?/Total no of peices(=20)'''
    
    def pos_score(self):
        '''Returns percent of pices in the right position but not in the right orientation'''
    
    def turnface(self,C,sig): #turning an array
        A=np.full([3,3],'')
        if sig=='+':
            A[:,0],A[0],A[:,2],A[2],A[1,1]=list(C[2]),list(C[:,0])[::-1],list(C[0]),list(C[:,2])[::-1],C[1,1]
            # print(C[2])
        elif sig=='-':
            A[:,0],A[0],A[:,2],A[2],A[1,1]=list(C[0])[::-1],list(C[:,2]),list(C[2])[::-1],list(C[:,0]),C[1,1]
        elif sig == 'r0':
            A[0], A[1], A[2] = list(C[2]), list(C[1]), list(C[0])
        elif sig == 'r1':
            A[:,0], A[:,1], A[:,2] = list(C[:,2]), list(C[:,1]), list(C[:,0])
        else:
            A = C.copy()
        return A

    def turn(self,ar,sig): #turning array plus adjacent stuff
        '''ar=[[' ','U',' '],
           ['L','C','R'], 
           [' ','D',' ']]'''
        
        C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
        if sig=='+':
            a,b,c,d=list(D[0]),list(L[:,2]),list(U[2]),list(R[:,0])
            L[:,2],U[2],R[:,0],D[0]=a,b,c,d
            C = self.turnface(C,'+')
        elif sig=='-':
            a,b,c,d=list(U[2]),list(R[:,0]),list(D[0]),list(L[:,2])
            L[:,2],U[2],R[:,0],D[0]=a,b,c,d
            C = self.turnface(C,'-')
        ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]=C,U,L,R,D
        return ar
    
    def get_side(self,face):
        cub = self.cub
        face_map = self.face_map
        turn_map = self.turn_map
        C = cub[face].copy()
        sides = []
        for i in range(4):
            F_name = face_map[face][i]
            F = cub[F_name].copy()
            for sig in turn_map[F_name][i]:
                F = self.turnface(F,sig)
            sides.append(F)
        L, R, U, D = sides
        ar = [['',U,''],[L,C,R],['',D,'']]
        return ar
            


    # def move(self,m):
    #     cub = self.cub
    #     face = m[0]
    #     face_map = self.face_map
    #     turn_map = self.turn_map




    def move(self,m):
        cub = self.cub
        if m[0]=='W':
            C=cub['W'].copy()
            L=cub['B'].copy()
            R=cub['G'].copy()
            U=cub['R'].copy()
            D=cub['O'].copy()
            ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
            ar=self.turn(ar,m[1])
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
            U=self.turnface(U,'-')
            D=cub['O']
            D=self.turnface(D,'+')
            ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
            ar=self.turn(ar,m[1])
            C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
            U=self.turnface(U,'+')
            D=self.turnface(D,'-')
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
            U=self.turnface(U,'-')
            U=self.turnface(U,'-')
            D=cub['O']
            D=self.turnface(D,'+')
            D=self.turnface(D,'+')
            ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
            ar=self.turn(ar,m[1])
            C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
            U=self.turnface(U,'+')
            U=self.turnface(U,'+')
            D=self.turnface(D,'-')
            D=self.turnface(D,'-')
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
            U=self.turnface(U,'+')
            D=cub['O']
            D=self.turnface(D,'-')
            ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
            ar=self.turn(ar,m[1])
            C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
            U=self.turnface(U,'-')
            D=self.turnface(D,'+')
            print(D,"here")
            cub['G']=C
            cub['W']=L
            cub['Y']=R
            cub['R']=U
            cub['O']=D
        elif m[0]=='R':
            C=cub['R']
            L=cub['B']
            L=self.turnface(L,'+')
            R=cub['G']
            R=self.turnface(R,'-')
            U=cub['Y']
            U=self.turnface(U,'-')
            U=self.turnface(U,'-')
            D=cub['W']
            ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
            ar=self.turn(ar,m[1])
            C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
            L=self.turnface(L,'-')
            R=self.turnface(R,'+')
            U=self.turnface(U,'+')
            U=self.turnface(U,'+')
            cub['R']=C
            cub['B']=L
            cub['G']=R
            cub['Y']=U
            cub['W']=D
        elif m[0]=='O':
            C=cub['O']
            L=cub['B']
            L=self.turnface(L,'-')
            R=cub['G']
            R=self.turnface(R,'+')
            U=cub['W']
            D=cub['Y']
            D=self.turnface(D,'-')
            D=self.turnface(D,'-')
            ar=np.array([[nul,U,nul],[L,C,R],[nul,D,nul]])
            ar=self.turn(ar,m[1])
            C,U,L,R,D=ar[1,1],ar[0,1],ar[1,0],ar[1,2],ar[2,1]
            L=self.turnface(L,'+')
            R=self.turnface(R,'-')
            D=self.turnface(D,'+')
            D=self.turnface(D,'+')
            cub['O']=C
            cub['B']=L
            cub['G']=R
            cub['W']=U
            cub['Y']=D
        else:
            print("Invalid move")
        

cube1 = Cube()
cube1.display()
cube1.move('B+')
print("After Move:")
cube1.display()
ar = cube1.get_side('Y')
print(ar)
# cube1.move('R-')
# print("After Move:")
# cube1.display()