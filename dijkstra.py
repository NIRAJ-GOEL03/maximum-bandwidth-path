import generate_graph
import sys
import time

UNSEEN = 0
FRINGE = 1
INTREE = 2


class Dijkstra:
    def __init__(self, graph, vertex, source, dest):

        self.graph = graph
        self.vertex = vertex
        self.source = source
        self.dest = dest        
        self.status = {}
        self.dad = {}
        self.bw = {}
        for v in vertex:
            self.status[v] = UNSEEN
            self.bw[v] = sys.maxint
            self.dad[v] = None

        if (source not in graph or dest not in graph):
            print "dijkstra.py: Invalid source or destination. Exiting."
            exit(0)
 
        self.status[source] = INTREE
        for v in graph[source]:
            self.status[v] = FRINGE             # INSERT INTO HEAP
            self.dad[v] = source
            self.bw[v] = graph[source][v]       # UPDATE TO HEAP
        

    def maxBwFringe(self):                      # USE MAXIMUM function of heap instead
        fringes = []
        for f in self.status:
            if self.status[f] == FRINGE:
                fringes.append(f)
        
        max_bw = 0
        max_bw_fringe = None
        for fringe in fringes:
            if self.bw[fringe] > max_bw:
                max_bw = self.bw[fringe]
                max_bw_fringe = fringe

        return max_bw_fringe


    def dijkstra(self):

        start_time = time.clock()
        while(self.status[self.dest] != INTREE):
            u = self.maxBwFringe()
            self.status[u] = INTREE         # DELETE FROM HEAP
            for v in self.graph[u]:
                if self.status[v] == UNSEEN:
                    self.status[v] = FRINGE         # INSERT TO HEAP
                    self.bw[v] = min(self.bw[u],self.graph[u][v])
                    self.dad[v] = u
                elif self.status[v] == FRINGE and (self.bw[v] < min(self.bw[u],self.graph[u][v])):
                    self.bw[v] = min(self.bw[u],self.graph[u][v])    # UPDATE IN HEAP
                    self.dad[v] = u

        end_time = time.clock()
        time_elapsed = end_time - start_time
        res_bw, res_path = self.bw[self.dest], self.buildPath()
        src_dest = "source: " + str(self.source) + " Dest: " + str(self.dest)
        report = ["Dijkstra without heap", str(float('{0:.4f}'.format(time_elapsed))) + " secs", src_dest, "max_bw: " + str(res_bw), res_path]
        return report
       
    def buildPath(self):
        path = []
        curr = self.dest
        while(curr != self.source):
            path.append(curr)
            curr = self.dad[curr]
        path.append(curr)
        return " --> ".join(reversed(map(str,path)))
     

        


#graph, vertex = generate_graph.generate()
#dij = Dijkstra(graph,vertex,2,100)
#print dij.dijkstra()
