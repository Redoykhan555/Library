from collections import defaultdict

class Node:
    def __init__(self,acc = False):
        self.accepting = acc
        self.transitions = defaultdict(list)

def char(c):
    start = Node()
    end = Node(True)
    start.transitions[c].append(end)
    return (start,end)

def union(one,two):
    start = Node()
    end = Node(True)
    one[1].accepting = False
    two[1].accepting = False
    start.transitions['$'].append(one)
    start.transitions['$'].append(two)
    one[1].transitions['$'].append(end)
    two[1].transitions['$'].append(end)
    return (start,end)

def concat(one,two):
    one[1].accepting = False
    one[1].transitions['$'].append(two[0])
    return (one[0],two[1])

def star(s):
    start = Node()
    end = Node(True)
    start.transitions['$'].append(end)
    start.transitions['$'].append(s[0])
    s[1].transitions['$'].append(end)
    s[1].transitions['$'].append(s[0])
    s[1].accepting = False
    return (start,end)

def parse(s):
    pass






















