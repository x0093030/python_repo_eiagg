if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
    print ([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n])
    #list = []
    #for x in range(0,x+1):
        #for y in range(0,y+1):
            #for z in range(0,z+1):
                #if (x+y+z == n):
                    #continue
                #else:
                    #list.append([x,y,z])
    
    #print(list)
