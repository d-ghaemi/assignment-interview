######################################## part 2 #############################################
def readMat(f_name):
    file = open(f_name, 'r')
    content = file.read()
    
    A=content.replace("[[[","[[")
    A=A.replace("]]]","]]")
    temp=len(A)+1
    while(temp>len(A)):
        temp=len(A)
        A=A.replace(" ]","]")
        
    
    A=A.split("]]")[:-1]

    H=len(A)
    for i in range(H):
        A[i]= (A[i]).replace('[','')
        A[i]= (A[i]).replace('\n  ','')
        A[i]= (A[i]).replace('\n ','')
        A[i]= (A[i]).replace('\n','')
        A[i]= (A[i]).split(']')
        

    
    W= len(A[0])

    for i in range(H):
        for j in range(W):
            #print(A[i][j])
            temp=len(A[i][j])+1
            while(temp>len(A[i][j])):
                temp=len(A[i][j])
                A[i][j]=A[i][j].replace("  "," ")
            A[i][j]=(A[i][j]).split(' ')

    C_in= len(A[0][0])
    for i in range(H):
        for j in range(W):
            for k in range(C_in):
                A[i][j][k]=float(A[i][j][k])
            
    #print('content')
    #print(A[0][0][0])
    #print('ast')
    
    file.close()
    return A, H, W, C_in

import os


A, H, W, C_in=readMat('A.txt')
B, fh, fw, C_in=readMat('B.txt')
print(H, W, C_in)
print(fh, fw, C_in)
#############################################################################################




######################################## part 3 #############################################
#without padding: Sh, Sw= S.shape
Sh=H-fh+1
Sw=W-fw+1
print(Sh, Sw, C_in)
S=[[[0 for k in range(C_in)]for j in range(Sw)]for i in range(Sh)]

################################ functions ########################################
def dot(A, B, h, w):
    s=0
    for i in range(h):
        for j in range(w):
            s=s+A[i][j]*B[i][j]
    #print(s)
    return s

def partA(A, i, fh, j, fw, k):
    pA=[[0 for n in range(fw)]for m in range(fh)]
    for m in range(fh):
        for n in range(fw):
            (pA[m])[n]= A[i+m][j+n][k]
    return pA

def partB(B, fh, fw, k):
    pB=[[0 for n in range(fw)]for m in range(fh)]
    for m in range(fh):
        for n in range(fw):
            pB[m][n]= B[m][n][k]
    return pB

##################################################################################

for k in range (C_in):
    for j in range(Sw):
        for i in range(Sh):
            ((S[i])[j])[k]=dot(partA(A, i, fh, j, fw, k), partB(B, fh, fw, k), fh, fw)
            

print('S: ')
print(S)
#############################################################################################




######################################## part 4 #############################################
grad_S_A=[[[[[0 for k in range(C_in)]for l in range(H)]for m in range(W)]for j in range(Sw)]for i in range(Sh)]

for k in range (C_in):
    for m in range(W):
        for l in range(H):
            for j in range(Sw):
                for i in range(Sh):
                    if i<=l & l<i+fh:
                        if j<=m & m<j+fw:
                            ((((grad_S_A[i])[j])[m])[l])[k]=B[l-i][m-j][k]

print('grad_S_A: ')
print(grad_S_A)



grad_S_B=[[[[[0 for k in range(C_in)]for l in range(fh)]for m in range(fw)]for j in range(Sw)]for i in range(Sh)]

for k in range (C_in):
    for m in range(fw):
        for l in range(fh):
            for j in range(Sw):
                for i in range(Sh):
                        ((((grad_S_B[i])[j])[m])[l])[k]=A[l+i][m+j][k]


print('grad_S_B: ')
print(grad_S_B)
#############################################################################################




######################################## part 5 #############################################

f = open("S.txt", 'w')
f.write(str(S))
f.close()

f = open("grad_S_A.txt", 'w')
f.write(str(grad_S_A))
f.close()

f = open("grad_S_B.txt", 'w')
f.write(str(grad_S_B))
f.close()

############## check writen files ################
f = open("S.txt", 'r')
content = f.read()
print('S')
print(content)
f.close()

f = open("grad_S_A.txt", 'r')
content = f.read()
print('grad_S_A')
print(content)
f.close()

f = open("grad_S_B.txt", 'r')
content = f.read()
print('grad_S_B')
print(content)
f.close()

#############################################################################################

