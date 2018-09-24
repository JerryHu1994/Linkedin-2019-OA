def zombiecluster(M):
	num = len(M)
        visited = [False]*num
        ret = 0  
        for i in range(num):
            if visited[i]:  continue
            stack = [i]
            while len(stack):
                curr = stack.pop()
                visited[curr] = True
                for i in range(num):
                    if M[curr][i] and curr!=i and not visited[i]:
                        stack.append(i)
            ret += 1
        return ret
print zombiecluster([[1,1,0],[1,1,0],[0,0,1]])