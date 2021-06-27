'''
What type of search usually returns the 
shortest path from the starting vertex 
to the target vertex once the target is found?
breadth-first search

In a BFS, we track what neighbors still 
need to be explored. In a BFS, this is 
done in a first in, first out order.

What data structure works best for keeping 
track of these unvisited neighbors?
queue
'''
'''
There are N students in a baking class together. 
Some of them are friends, while some are not friends. 
The students' friendship can be considered transitive. 
This means that if Ami is a direct friend of Bill, 
and Bill is a direct friend of Casey, Ami is an indirect 
friend of Casey. A friend circle is a group of students 
who are either direct or indirect friends of some level. 
That is, the friend circle consists of a person, their friends, 
their friends-of-friends, their friends-of-friends-of-friends, and so on.

Given a N*N matrix M representing the friend relationships 
between students in the class. If M[i][j] = 1, then the 
ith and jth students are direct friends with each other, 
otherwise not.

You need to write a function that can output the total 
number of friend circles among all the students.
'''

def csFriendCircles(friendships):
    output = 0
    visited = set()
    for row in range(len(friendships)):
        if friendships[row][row] == 1 and row not in visited:
            output += 1
            visited = dfs(row, friendships, visited)
    return output   

def dfs(row, friendships, visited):
    visited.add(row)
    for neigh in range(len(friendships[row])):
        if friendships[row][neigh] == 1 and neigh not in visited:
            dfs(neigh, friendships, visited)
    return visited

'''
Author's solution
'''

def dfs(friendships, visited, i):
    for j in range(len(friendships)):
        if friendships[i][j] == 1 and visited[j] == 0:
            visited[j] = 1
            dfs(friendships, visited, j)

def csFriendCircles(friendships):
    visited = [0] * len(friendships)
    count = 0
    
    for i in range(len(friendships)):
        if visited[i] == 0:
            dfs(friendships, visited, i)
            count += 1
    
    return count