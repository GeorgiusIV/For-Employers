#!/usr/bin/python
# -*- coding: utf-8 -*-


class DisjointSet:

    _id = 0

    def __init__(self, face=None):

        # a disjoint set begins as its own parent

        self.parent = self

        # if no face e.g. 'a' or 'x' is chosen, give the names 'x1','x2' ...

        self._id += 1
        if face:
            self.face = face
        else:
            self.face = 'x' + str(self._id)

    def find(self):

        # if this disjoint set is its own parent, return it

        if self.parent == self:
            return self
        else:

        # if not, recurse on the parent, repeat until parent is found

            return self.parent.find()

    def union(self, newParent):

        # change the parent of this disjoint set to newParent

        self.parent = newParent


class Graph:

    def __init__(self, V):

        self.verts = V
        self.edges = list()

    def union_find(self):

        # create a Disjoint Set for each vertex of this graph

        disjoints = [DisjointSet(v) for v in self.verts]

        # iterate through each edge of this graph, collect the verts either side

        for e in self.edges:
            (u, v) = (e[0], e[1])

            # find the location of each vertex in self.verts

            u_index = self.verts.index(u)
            v_index = self.verts.index(v)

            # overwrite the verts with their corresponding disjoint set

            u = disjoints[u_index]
            v = disjoints[v_index]

            # if the disjoint sets share a parent, then a cycle is found

            if u.parent.Find() == v.parent.find():
                return True
            else:

            # if they do not share a parent, Union them, now they do.

                u.union(v)

        # if all edges are iterated, and no cycles are found, return false
        
        return False

    def kruskal(self):

        # produce a clone of this graph, with the same vertices, and no edges

        MST = Graph(self.verts)

        # organize the edges of this graph by weight ascending

        E = self.reorder_edges()

        # iterate through each edge, and add the edge to the clone

        for e in E:
            MST += e

            # if adding the edge produces a cycle, them remove the edge

            if MST.union_find():
                MST -= e

        # once reorganized, return the clone - the Minimum Spanning Tree

        return MST

    def __add__(self, operand):

        # if operand is list, iterate through each entry of the list

        if type(operand) == type(list()):
            for o in operand:
                self.__add__(o)
        elif type(operand) == type(str()):

        # if operand is string, treat it as vertex - add directly to self.verts

            self.verts += [operand]
        elif type(operand) == type(tuple()):

        # if operand is tuple, treat it as edge - add directly to self.edges

            self.edges += [(operand[0], operand[1], operand[2])]
        else:

        # complete all cases for the if-elif-else statement

            pass

        return self

    def __sub__(self, operand):

        # if operand is list, iterate through each entry of the list

        if type(operand) == type(list()):
            for o in operand:
                self.__add__(o)
        elif type(operand) == type(str()):

        # if operand is string, treat it as vertex - remove from self.verts

            self.verts -= [operand]
        elif type(operand) == type(tuple()):

        # if operand is tuple, treat it as edge - remove from self.edges

            self.edges.remove((operand[0], operand[1], operand[2]))
        else:

        # complete all cases for the if-elif-else statement

            pass

        return self

    def reorder_edges(self):

        # create a list of the weights of this graph

        W = [e[2] for e in self.edges]

        # sort the weights in ascending order

        W = self.merge_sort(W)

        # create a list to store the reordered edges

        E = list()

        # per edge in the graph, find the shared weight from reorganized weights

        for w in W:
            for e in self.edges:

                # match edge e, with the position of its shared weight

                if e not in E and e[2] == w:
                    E += [e]
                    break

        # return the reorganized edges

        return E

    def merge_sort(self, lst):

        # create pointers at the start and end of the list

        start = 0
        end = len(lst)

        # if the list can still be split, split it

        if end > 1:

            # create a pointer to the middle, around which to split the list

            mid = end // 2

            # split the list into left and right sides

            L = self.merge_sort(lst[start:mid])
            R = self.merge_sort(lst[mid:end + 1])

            # create pointers for iterating through the list

            (i, j) = (0, 0)
            
            #collect the first elements, and produce a return list
            
            l = L[0]
            r = R[0]
            newlst = []

            # begin merging the two lists
            # while either list L or R, still has an element inside

            while i < len(L) or j < len(R):

                # if list L still has an element, 
                # and that element is smaller than list R's element

                if l < r and i < len(L):

                    # add the smaller element to the return list, 
                    # increment the pointers position in the list

                    newlst += [l]
                    i += 1

                    # if there is an element at the pointer's new position,
                    # add it. If not, treat the element as infinity

                    try:
                        l = L[i]
                    except IndexError:
                        l = float('inf')
                elif j < len(R):

                # a repeat of what happens to L, for R.

                    newlst += [r]
                    j += 1
                    try:
                        r = R[j]
                    except IndexError:
                        r = float('inf')
                else:

                # complete all cases of the if-elif-else statement

                    pass

            # finally, return the newly ordered list

            return newlst
        elif end == 1:

        # if the list cannot be split, but contains an element, 
        # then return the single element and begin merging

            return lst
        else:

        # if the list does not contain an element,
        # return an infinite value that will never be appended

            return [float('inf')]


def main():
    verts = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        ]
    G = Graph(verts)
    G += [
        ('a', 'b', 3),
        ('a', 'd', 12),
        ('b', 'c', 7),
        ('c', 'e', 8),
        ('d', 'e', 10),
        ('e', 'f', 9),
        ('e', 'h', 12),
        ('f', 'g', 10),
        ('h', 'i', 3),
        ]

    print G.kruskal().edges


if __name__ == '__main__':
    main()