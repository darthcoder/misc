import numpy as np

A = np.array([[1,3,1], [1,1,-1], [3, 11, 5]])

# print(A)
b = np.array([9, 1, 35])

n = len(A)
# print(n)


#--------------------- Elimination -----------------------------------

for j in range(n-1):
    # print(j)
    for i in range(j+1, n):
        # print(i)
        factor = A[i,j]/A[j,j]
        
        for k in range(j+1,n):
            A[i,k] = A[i,k] - factor*A[j,k]

        b[i] = b[i] - factor*b[j]

print(A)
print(b)

#----------------------- Back substitution ---------------------------

x = np.zeros(n)

k = n-1
x[k] = b[k]/A[k,k]

for i in range(k,1,-1):
    for j in range(i+1,k+1):
        b[i] = b[i] - A[i,j] * x[j]

    x[i] = b[i]/A[i,i]

print(x)
