import numpy as np
import cv2 as cv

###############################################


H = np.random.randint(3, 11)
W = np.random.randint(3, 11)
C_in = np.random.randint(1, 11)
fh = np.random.randint(1, 8)
fw = np.random.randint(1, 8)

A= np.random.rand((H, W, C_in))
B= np.random.rand((fh, fw, C_in))
S1= cv.filter2D(src=A, ddepth=-1, kernel=B)
np.savetxt('A.txt', A)
np.savetxt('B.txt', B)

print('S1: ')
print(S1)



###############################################



A= np.loadtxt('A.txt')
B= np.loadtxt('B.txt')
H, W, C_in= A.shape
fh, fw, C_in = B.shape
#without padding: Sh, Sw= S.shape
Sh=H-fh+1
Sw=W-fw+1
S=np.zeros(Sw, Sh, C_in)


def dot(A, B):
    h, w = A.shape
    s=0
    for i in range(h):
        for j in range(w):
            s=s+A[i,j]*B[i, j]

for k in range (C_in):
    for j in range(Sw):
        for i in range(Sh):
            S[i, j, k]=dot(A[i:i+fh, j:j+fw, k], B)


print('S: ')
print(S)

np.savetxt('S.txt', S)