import math 

seen = set()
edges = []

def dfs(node, k, A):
	
	for i in range(k):
		str = node + A[i]
		if (str not in seen):
			seen.add(str)
			dfs(str[1:], k, A)
			edges.append(i)


def deBruijn(n, k, A):
	
	seen.clear()
	edges.clear()
	startingNode = A[0] * (n - 1)
	dfs(startingNode, k, A)
	
	S = ""
        
	l = int(math.pow(k, n))
	for i in range(l):
		S += A[edges[i]]
		
	S += startingNode
	return S

n = 3
k = 2
A = "01"

print(deBruijn(n, k, A))

