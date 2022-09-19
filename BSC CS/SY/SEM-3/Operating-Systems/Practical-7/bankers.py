if __name__=="__main__":

	n = 5 # Number of processes
	m = 3 # Number of resources

    # Total resources is [10, 5, 7]
	
	# Allocation Matrix
	alloc = [[0, 1, 0],
             [2, 0, 0],
			 [3, 0, 2],
             [2, 1, 1] ,
             [0, 0, 2]]
	
	# MAX Matrix
	max = [[7, 5, 3],
           [3, 2, 2],
		   [9, 0, 2],
           [2, 2, 2],
           [4, 3, 3]]
	
	avail = [3, 3, 2] # Available Resources
	
	f = [0]*n
	ans = [0]*n
	ind = 0
	for k in range(n):
		f[k] = 0
		
	need = [[ 0 for i in range(m)]for i in range(n)]
	for i in range(n):
		for j in range(m):
			need[i][j] = max[i][j] - alloc[i][j]
	y = 0
	for k in range(5):
		for i in range(n):
			if (f[i] == 0):
				flag = 0
				for j in range(m):
					if (need[i][j] > avail[j]):
						flag = 1
						break
				
				if (flag == 0):
					ans[ind] = i
					ind += 1
					for y in range(m):
						avail[y] += alloc[i][y]
					f[i] = 1
					
	print("Following is the SAFE Sequence")
	
	for i in range(n):
		print(f" Process {ans[i]} completed its work")
        
