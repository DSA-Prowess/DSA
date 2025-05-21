# Given directed edges , build an adjacency list

# Example:
from collections import deque
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}
for src, dest in edges:
    if src not in adjList:
        adjList[src] = []
    if dest not in adjList:
        adjList[dest] = []
    adjList[src].append(dest)

print(adjList)


# Brute Force backtracking DFS approach
# Length of the part cant be more than vertices 
def dfs(node, target , adjList, visit):
    if node in visit:
        return 0 
    if node == target :
        return 1

    count = 0
    visit.add(node)
    for neigbor in adjList[node]:
        count += dfs(neigbor, target, adjList, visit)
    visit.remove(node)

    return count      


print(dfs("A", "E", adjList, set()))

#Shortest path from node to target
def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = deque()
    queue.append(node)

    while queue:
        for i in range(len(queue)):
            cur = queue.popleft()
            if cur == target:
                return length 
            for nei in adjList[cur]:
                if nei not in visit:
                    visit.add(nei)
                    queue.append(nei)
        length +=1
    return length

print(bfs("A", "E", adjList))