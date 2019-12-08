import numpy as np
print(' ')
print('Input should be in "n x 2" matrix')

row = int(input("Enter the number of rows:")) 
col = 2

print("Enter the values 0f the matrix (Left to Right) : ") 
l = list(map(int, input().split())) 
e = np.array(l).reshape(row, col) 

print(e) 

print(' ')


def Python3(e):  
    if len(e) >= 10:

        e1 = 10

    else:

        e1 = len(e)
            
    for n in range(e1):
        
        f = np.polyfit(e[:,0], e[:,1],n)
    
        g = np.polyval(f, e[:,0])
        
        p = np.linalg.norm(e[:,1] - g)
        
        x = [n,p]
        
        if n==0:
            
            y = x
            
        elif y[1] >= x[1]:
            
            z = x[0]
            
    p = np.polyfit(e[:,0],e[:,1],z)

    print('Coefficients: ',np.around(p,2))

Python3(e)