import dijkstra
import dijkstra_heap
import kruskals
import random
import generate_graph


def compute():
    no_graphs = 5
    no_src_dest = 5
    
    # Sparse Graph
    computeUtil(no_graphs, no_src_dest, 5000,8)
    # Dense Graph
    #computeUtil(no_graphs, no_src_dest, 5000,1000)
    



def computeUtil(no_graphs, no_src_dest,no_verts,degree):
    
    dij_times = []
    dij_heap_times = []
    kruskal_times = []
    
    for i in range(no_graphs):
        print "="*25 + " Graph "+str(i+1)+" "+"="*25
        print "============= Vertices = "+str(no_verts)+ " Degree = "+str(degree)+" =============="
        print "="*59+"\n"
        graph, vertex = generate_graph.generate(no_verts,degree)
        for j in range(no_src_dest):
            src = random.randint(1,no_verts-1)
            dest = random.randint(1,no_verts-1)
            print "="*40
            while(dest == src or dest == src + 1 or dest == src-1):
                dest = random.randint(1,no_verts-1)

            dij = dijkstra.Dijkstra(graph,vertex,src,dest)
            report1 = dij.dijkstra()
            dij_times.append(float(report1[1].split(' ')[0]))
            del dij

            print report1[:-1],"\n"

            dij_heap = dijkstra_heap.DijkstraHeap(graph,vertex,src,dest)
            report2 = dij_heap.dijkstra()
            dij_heap_times.append(float(report2[1].split(' ')[0]))
            del dij_heap
            print report2[:-1],"\n"
        
            krus = kruskals.Kruskals(graph,vertex,src,dest)
            report3 = krus.findPath()
            kruskal_times.append(float(report3[1].split(' ')[0]))
            del krus
            print report3[:-1],"\n"
        
    print "====== Average Times ======"
    print "Dijkstra without heap: ",sum(dij_times)/len(dij_times), " seconds"
    print "Dijkstra with heap   : ",sum(dij_heap_times)/len(dij_heap_times), " seconds"
    print "Kruskals             : ",sum(kruskal_times)/len(kruskal_times), " seconds"

        
            
        
compute()          
        

