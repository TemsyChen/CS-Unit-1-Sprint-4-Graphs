'''
Given a linked list of integers, remove any nodes 
from the linked list that have values that have 
previously occurred in the linked list. 
Your function should return a reference to the 
head of the updated linked list.

Example:
Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
Explanation: The input list contains redundant nodes 
(3), (6), and (2), so those should be removed from the list.
'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    if node is None:
        return
        
    current = node
    values = []
    
    while node:
        if node.value not in values:
            values.append(node.value)
            node = node.next
        else:
            current = node
            node = current.next
            
    return values
    
'''
Given a string s consisting of small English letters,
find and return the first instance of a non-repeating 
character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 
'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.

There are no characters in this string that do not repeat.
'''
'''
Understand:
find pattern
if palindrome (same as reverse), return '_'.
Find unique letters in the string. Return the first unique letter
'''

from collections import deque

def first_not_repeating_character(s):
    if len(s) == 1:
        return s
        
    letters = {}
    
    for char in s:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    
    unique_letters = []
    
    for letter in letters:
        if letters[letter] == 1:
            unique_letters.append(letter)
            
    if len(unique_letters) == 0:
        return '_'
    else:
        return unique_letters[0]
            
'''
In a city-state of n people, there is a rumor 
going around that one of the n people is a spy 
for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i]
 = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. 
Otherwise, return -1.
'''
def uncover_spy(n, trust):
    notSpy = []
    maybeSpy = []
    spy = None
    numTrustSpy = 0
    
    for relationship in trust:
        notSpy.append(relationship[0])
        #print(relationship[0])
        maybeSpy.append(relationship[1])
        #print(relationship[1])
        
    print(notSpy)
    print(maybeSpy)    
        
    for person in maybeSpy:
        if person in notSpy:
            continue
        else:
            spy = person
            
    for relationship in trust:
        if relationship[1] == spy:
            numTrustSpy += 1
            
    if not spy:
        return -1
    elif numTrustSpy != n-1:
        return -1
    else:
        return spy
        