'''
You are given a directed acyclic graph (DAG) that contains N nodes.

Write a function that can find all the possible paths from node 0 to node N - 1.

graph[a] is a list of all nodes b for which the edge a -> b exists.

Understand:
graph = [[1, 2],[3],[3],[4],[]] --> [[0,1,3,4], [0,2,3,4]]
graph = [[1,2], [3], [3], []] --> [[0,1,3], [0,2,3]]
graph = [[4,3,1], [3,2,4], [3], [4], []] --> [[0,1,2,3,4],  [0,1,3,4],  [0,1,4],  [0,3,4],  [0,4]]
graph = [[1], []] --> [[0,1]]

The index of the element is the node value. The items in the element are what the node[i] is connected and pointing to. If the element is empty, the node is pointing to nothing.
Create a visited variable. Start by appending the 0 index. From the 0th index, pop off a value from the element and append to visited. Take that value and use it as an index recursively to get the next i index to pop off that value and append. When there is no next index, sort the visited variable and append it to a result variable. Do this until graph is empty. 
'''

def csFindAllPathsFromAToB(graph): #my solution
    result = []
    while any(graph):
        i = 0
        visited = []
        path = helper(i, graph, visited)
        result.append(path)
    return sorted(result)
    
def helper(i, graph, visited):
    while i != []:
        if i not in visited:
            visited.append(i)
        if len(graph[i]) > 0:
            i = graph[i].pop()
            helper(i, graph, visited)
        else:
            i = []
            return visited

    return visited   

def csFindAllPathsFromAToB(graph): #leetcode solution
    N = len(graph) - 1
    paths = [[0]]
    ans = []
    while paths:
        path = paths.pop()
        for n in graph[path[-1]]:
            if n == N:
                ans.append(path + [n])
            else:
                paths.append(path + [n])
    return sorted(ans)

#Lambda solutions from Steve:
    
from collections import deque  

def csFindAllPathsFromTheSourceToTheTarget(graph):
    target = len(graph) - 1
    results = []
    def backtrack(curr, path):
        # if we reach the target, no need to explore further
        if curr == target:
            results.append(list(path))
            return
        # explore the neighbor nodes one after another
        for next in graph[curr]:
            path.append(next)
            backtrack(next, path)
            path.pop()
    # kick off the backtracking, starting from the source node
    path = deque([0])
    backtrack(0, path)
    return results

# Alternate no-deque solution
def csFindAllPathsFromAToB(graph):
    # This is an acyclic graph--no need to keep a "visited" set because
    # the only purpose of that set is to avoid cycles.
    final_node = len(graph) - 1   # (n-1)th node
    results = []  # To return
    # Make an inner function for recursion
    def dft(path):
        # Currently visiting the last node in the path        
        this_node = path[-1]
        # If we found the final node, this must be a path to it
        if this_node == final_node:
            results.append(path)
            return
        # Visit all the neighbors
        for neighbor in graph[this_node]:
            dft(path + [neighbor])
    # Start visiting from the 0th node
    dft([0])
    return results

# Non-recursive version
#
# This _should_ work, but it returns the results out of order
# and causes the tests not to pass. The tests _should_ still pass.
# Looking into this.
def csFindAllPathsFromAToB(graph):
    # This is an acyclic graph--no need to keep a "visited" set because
    # the only purpose of that set is to avoid cycles.
    final_node = len(graph) - 1   # (n-1)th node
    results = []  # To return
    stack = [[0]]  # Add starting path to stack
    while len(stack) > 0:
        # Grab the current path from the top of the stack
        path = stack.pop()
        # Currently visiting the last node in the path        
        this_node = path[-1]
        # If we found the final node, this must be a path to it
        if this_node == final_node:
            results.append(path)
            continue
        # Visit all the neighbors
        for neighbor in graph[this_node]:
            stack.append(path + [neighbor])  # Push next paths to explore
    return sorted(results)


# Alternate backtracking version
def csFindAllPathsFromAToB(graph):
    result = []
    # kick off the backtracking, starting from the source node
    path = [0]
    backtrack(graph, 0, path, result)
    return result
def backtrack(graph, vertex, path, result):
    # if we reach the target, no need to explore further
    if vertex == len(graph) - 1:
        result.append(path[:])
        return
    # explore the neighbor nodes one after another
    for neighbor in graph[vertex]:
        path.append(neighbor)
        backtrack(graph, neighbor, path, result)
        path.pop()
