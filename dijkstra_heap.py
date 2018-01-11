import heap
import sys
import time

UNSEEN = 0
FRINGE = 1
INTREE = 2


class DijkstraHeap:
    def __init__(self, graph, vertex, source, dest):

        self.graph = graph
        self.vertex = vertex
        self.source = source
        self.dest = dest        
        self.status = {}
        self.dad = {}
        self.bw = {}
        self.heap = heap.Heap()
        for v in vertex:
            self.status[v] = UNSEEN
            self.bw[v] = sys.maxint
            self.dad[v] = None

        if (source not in graph or dest not in graph):
            print "dijkstra.py: Invalid source or destination. Exiting."
            exit(0)
 
        self.status[source] = INTREE
        for v in graph[source]:
            self.dad[v] = source
            self.status[v] = FRINGE             # INSERT INTO HEAP
            self.bw[v] = graph[source][v]       # UPDATE TO HEAP
            (self.heap).insert(v,graph[source][v])
        

    def maxBwFringe(self):
        return self.heap.maximum()

    def dijkstra(self):

        start_time = time.clock()
        del_time = 0
        del_count = 0
        ins_time = 0
        ins_count = 0
        update_time = 0
        update_count = 0
        while(self.status[self.dest] != INTREE):
            #u = self.maxBwFringe()
            u = self.heap.maximum()
            self.status[u] = INTREE         # DELETE FROM HEAP

            
            del_start = time.clock()
            self.heap.delete(u)
            del_end = time.clock()
            del_count = del_count + 1
            del_time = del_time + (del_end - del_start)
            for v in self.graph[u]:
                if self.status[v] == UNSEEN:
                    self.status[v] = FRINGE         # INSERT TO HEAP
                    self.bw[v] = min(self.bw[u],self.graph[u][v])
                    ins_start = time.clock()
                    self.heap.insert(v,self.bw[v])
                    ins_end = time.clock()
                    ins_count = ins_count + 1
                    ins_time = ins_time + (ins_end - ins_start)
                    self.dad[v] = u
                elif self.status[v] == FRINGE and (self.bw[v] < min(self.bw[u],self.graph[u][v])):
                    self.bw[v] = min(self.bw[u],self.graph[u][v])    # UPDATE IN HEAP

                    update_start = time.clock()

                    self.heap.update(v,self.bw[v])
                    update_end = time.clock()
                    update_time = update_time + (update_end - update_start)
                    update_count = update_count + 1


                    self.dad[v] = u
        end_time = time.clock()
        time_elapsed = end_time - start_time
        res_bw, res_path = self.bw[self.dest], self.buildPath()
        src_dest = "source: " + str(self.source) + " Dest: " + str(self.dest)
        report = ["Dijkstra with heap   ", str(float('{0:.4f}'.format(time_elapsed))) + " secs", src_dest,"max_bw: " + str(res_bw), res_path]
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
    print "Generating Graph..."
    
    graph, vertex = generate_graph.generate(5000,1000)
    print "Graph generated !!"
    
    
    print "\n\nw/o heap\n\n"
    dij = dijkstra.Dijkstra(graph,vertex,2,5)
    dij_bw, dij_path = dij.dijkstra()
    print dij_path
    print "\n"
    print dij_bw
    
    print "\n\nwith heap\n\n"
    dij_heap = DijkstraHeap(graph,vertex,2,5)
    dij_heap_bw, dij_heap_path = dij_heap.dijkstra()
    print dij_heap_path
    print "\n"
    print dij_heap_bw
    
    
    print "\n\nwith Kruskals\n\n"
    krus = kruskals.Kruskals(graph,vertex,2,5)
    krus_bw, krus_path = krus.findPath()
    print krus_path
    print "\n"
    print krus_bw


