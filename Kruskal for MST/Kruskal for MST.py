
class DisjointSet():
    _id = 0
    
    def __init__(self, face = None):
        
        # a disjoint set begins as its own parent
        self.parent = self
        
        # if no face e.g. 'a' or 'x' is chosen, give the names 'x1','x2' ...
        self._id += 1
        if face: self.face = face
        else: self.face = "x" + str(self._id)
        
    def Find(self):
        
        # if this disjoint set is its own parent, return it
        if self.parent == self:
            return self
        
        # if not, then perform this same check on its parent, this will recurse until a parent is found
        else:
            return self.parent.Find()
​
    def Union(self,newParent):
        
        # change the parent of this disjoint set to newParent
        self.parent = newParent
    
​
class Graph():
    
    def __init__(self, V):
        
        self.verts = V
        self.edges = list()
    
    
    def UnionFind(self):
        
        # create a Disjoint Set for each vertex of this graph
        disjoints = [DisjointSet(v) for v in self.verts]
        
        # iterate through each edge of this graph, collect the verts on either end
        for e in self.edges:
            u,v = e[0],e[1]
            
            # find the location of each vertex in self.verts
            u_index = self.verts.index(u)
            v_index = self.verts.index(v)
            
            # overwrite the verts with their corresponding disjoint set
            u = disjoints[u_index]
            v = disjoints[v_index]
​
            # if the disjoint sets share a parent, then a cycle is found
            if u.parent.Find() == v.parent.Find():
                return True
            
            # if they do not share a parent, Union them, now they do share a parent, if they are ever called upon again
            else:
                v.Union(u)
                
        # if all of the edges are iterated, and no cycles are found, return false
        return False
        
    
    
    def Kruskal(self):
        
        # produce a clone of this graph, with the same vertices, and no edges
        MST = Graph(self.verts)
        
        # organize the edges of this graph by weight ascending
        E = self.reorderEdges()
        
        # iterate through each edge, and add the edge to the clone
        for e in E:
            MST += e
            
            # if adding the edge produces a cycle, them remove the edge
            if MST.UnionFind():
                MST -= e
​
        # once all edges are removed, return the clone, it is the Minimum Spanning Tree of this graph
        return MST
    
            
        
        
        
            
    def __add__(self, b):
        
        # if the operand b is a string, treat it as a vertex, and add it directly to self.verts
        if type(b) == type(str()):
            self.verts += [b]
            
        # if the operand b is a tuple, treat it as an edge and add it directly to self.edges
        elif type(b) == type(tuple()):
            self.edges += [(b[0],b[1],b[2])]
            
        # this is here just to complete all cases for the elif statement
        else:
            pass
        
        return self
        
        
    def __sub__(self, b):
        
        # if the operand b is a string, treat it as a vertex, and remove it directly from self.verts
        if type(b) == type(str()):
            self.verts -= [b]
            
        # if the operand b is a tuple, treat it as an edge and remove it directly from self.edges
        elif type(b) == type(tuple()):
            self.edges.remove((b[0],b[1],b[2]))
            
        # this is here just to complete all cases for the elif statement
        else: 
            pass
        
        return self
            
            
    def reorderEdges(self):
        
        # create a list of the weights of this graph
        W = [e[2] for e in self.edges]
        
        # sort the weights in ascending order
        W = self.Mergesort(W)
        
        # create a list to store the reordered edges
        E = list()
        
        # for each edge in this graph, find the corresponding weight from the reorganized weights
        for e in self.edges:
            for w in W:
                
                # match the position of the edge e, with the position of its corresponding weight
                if e[2] == w:
                    E += [e]
                    break
                    
        # return the reorganized edges
        return E
            
         
    def Mergesort(self, lst):
    
        # create pointers at the start and end of the list
        start = 0
        end = len(lst)
    
        # if the list can still be split, split it
        if end > 1:
            
            # create a pointer to the middle, around which to split the list
            mid = end // 2
        
            # split the list into left and right sides
            L = self.Mergesort(lst[start:mid])
            R = self.Mergesort(lst[mid:end+1])
        
            # create pointers for iterating through the list, collect the first elements, and produce a return list
            i,j = 0,0
            l = L[0] 
            r = R[0] 
            newlst = []
        
            # begin merging the two lists
            #while either list L or R, still has an element inside
            while i < len(L) or j < len(R):
            
                # if list L still has an element, and that element is smaller than list R's element
                if l < r and i < len(L):
                    
                    # add the smaller element to the return list, increment the pointers position in the list
                    newlst += [l]
                    i += 1
                    
                    # if there is an element at the pointer's new position, add it. If not, treat the element as infinity
                    try: l = L[i] 
                    except IndexError: l = float('inf')
                        
                # a repeat of what happens to L, for R.
                elif j < len(R):
                    newlst += [r]
                    j += 1
                    try: r = R[j] 
                    except IndexError: r = float('inf')
                        
                # this is here solely to complete all cases of the elif statement
                else:
                    pass
                    
            # finally, return the newly ordered list
            return newlst
        
        # if the list cannot be split, but contains an element, then return the single element and begin merging
        elif end == 1:
            return lst
        
        # if the list does not contain an element, return an infinite value that will never be appended
        else:
            return [float('inf')]
        
        
        
def main():
    verts = ["a","b","c","d","e","f","g","h","i"]
    G = Graph(verts)
    G += ("a","b",3)
    G += ("a","d",12)
    
    G += ("b","c",7)
    G += ("c","e",8)
    G += ("d","e",10)
    
    G += ("e","f",9)
    G += ("e","h",12)
    G += ("f","g",10)
    G += ("h","i",3)
    
    print(G.Kruskal().edges)
    
main()
    
​
​