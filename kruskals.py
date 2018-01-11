import sys
import time

WHITE = 0
GRAY = 1
BLACK = 2


class heapSort:
    def __init__(self):
        pass

    def heapify(self,graph, n, i):
        largest = i  
        smallest = i
        l = 2 * i + 1     
        r = 2 * i + 2     
     
        if l < n and graph[i].weight > graph[l].weight:
            smallest = l

        if r < n and graph[smallest].weight > graph[r].weight:
            smallest = r
     
        if smallest != i:
            graph[i],graph[smallest] = graph[smallest],graph[i]  
     
            self.heapify(graph, n, smallest)
     
    def heap_sort(self,graph):
        n = len(graph)
     
        for i in range(n, -1, -1):
            self.heapify(graph, n, i)
     
        for i in range(n-1, 0, -1):
            graph[i], graph[0] = graph[0], graph[i]   
            self.heapify(graph, i, 0)




class UF:

    def __init__(self,vlist):
        self.parent = {i : i for i in vlist}
        self.rank = {i:1 for i in vlist}

    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,a,b):
        a_parent = self.find(a)
        b_parent = self.find(b)

        if a_parent == b_parent:
            return
        if(self.rank[a_parent] > self.rank[b_parent]):
            self.parent[b_parent] = a_parent
        elif(self.rank[b_parent] > self.rank[a_parent]):
            self.parent[a_parent] = b_parent
        else:
            self.parent[a_parent] = b_parent
            self.rank[b_parent] = self.rank[b_parent] + 1

class Edge:
    def __init__(self,source,dest,wt):
        self.source = source
        self.dest = dest
        self.weight = wt


class Kruskals:

    def __init__(self, graph, vertex, source, dest):
        
        self.graph = self.convertAdjacencyToEdgeList(graph)

        self.vertex = vertex
        self.source = source
        self.dest = dest
        self.status = {}
        self.dad = {}
        self.bw = {}
        for v in vertex:
            self.status[v] = WHITE
            self.bw[v] = sys.maxint
            self.dad[v] = None

        if (source not in graph or dest not in graph):
            print "kruskals.py: Invalid source or destination. Exiting."
            exit(0)
 
        self.status[source] = GRAY

    def convertAdjacencyToEdgeList(self,graph):
        temp_graph = []
        for u in graph:
            for v in graph[u]:
                 temp_graph.append(Edge(u,v,graph[u][v]))
        return temp_graph

    def convertEdgeListToAdjacency(self,graph):
        temp_graph = {}
        for edge in graph:
            if edge.source not in temp_graph:
                temp_graph[edge.source] = {edge.dest:edge.weight}
            else:
                temp_graph[edge.source][edge.dest] = edge.weight
            if edge.dest not in temp_graph:
                temp_graph[edge.dest] = {edge.source:edge.weight}
            else:
                temp_graph[edge.dest][edge.source] = edge.weight
        return temp_graph

    def findPath(self):


        hs =  heapSort()
        start_time = time.clock()
        #self.graph = reversed(sorted(self.graph, key=lambda i: i.weight))
        hs.heap_sort(self.graph)

        new_graph1 = []
        uf = UF(self.vertex)
        for edge in self.graph:
            src = edge.source
            dest = edge.dest
            if(uf.find(src) != uf.find(dest)):
                uf.union(dest,src)
                new_graph1.append(edge)

        start1 = time.clock() 
        new_graph = self.convertEdgeListToAdjacency(new_graph1)
        subtract_time = time.clock() - start1
        qu = [self.source]
        while(self.status[self.dest] != BLACK and len(qu)):
            u = qu.pop(0)
            for v in new_graph[u]:
                if(self.status[v] == WHITE):
                    self.status[v] = GRAY
                    self.bw[v] = min(self.bw[u], new_graph[u][v])
                    self.dad[v] = u
                    qu.append(v)
                elif(self.status[v] == GRAY and self.bw[v] < min(self.bw[u], new_graph[u][v])):
                    self.dad[v] = u
                    self.bw[v] = min(self.bw[u], new_graph[u][v])

            self.status[u] = BLACK

        end_time = time.clock()
        time_elapsed = end_time - start_time - subtract_time
        res_bw, res_path = self.bw[self.dest], ""
        src_dest = "source: " + str(self.source) + " Dest: " + str(self.dest)
        report = ["Kruskals             ", str(float('{0:.4f}'.format(time_elapsed))) + " secs", src_dest, "max_bw: " + str(res_bw), res_path]
        return report


    def buildPath(self):
        path = []
        curr = self.dest
        while(curr != self.source):
            path.append(curr)
            curr = self.dad[curr]
        path.append(curr)
        return " --> ".join(reversed(map(str,path)))
  
def test():
    hs = heapSort()
    e1 = Edge("u1","v1",3)     
    e2 = Edge("u2","v2",13)     
    e3 = Edge("u3","v3",33)     
    e4 = Edge("u4","v4",12)     
    e5 = Edge("u5","v5",27)     
    e6 = Edge("u6","v6",98)     
    e7 = Edge("u7","v7",44)  
    
    gph = [e1,e2,e3,e4,e5,e6,e7]
    
    hs.heap_sort(gph)
    
    for g in gph:
        print g.weight   
