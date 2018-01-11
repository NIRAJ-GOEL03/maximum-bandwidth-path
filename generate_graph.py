import random
import scipy.stats as stats

class GraphGenerator():
    
    def __init__(self,vertices = 5000):
        self.vertices = vertices
        self.vertex = range(1,self.vertices+1)
        self.graph = {}
        for i in range(1,self.vertices+1):
            self.graph[i] = {}


    def createEdges(self, avg_degree=8):
        self.connectAllEdges()
        self.connectVertices(avg_degree)
        pass 

    def connectAllEdges(self):
        for v in self.graph:
            weight = random.randint(10,2000)
            #self.graph[v].append((v+1,weight) if (v+1 == self.vertices) else ((v+1)%self.vertices,weight))
            if v+1 == self.vertices:
                self.graph[v][v+1] = weight
                self.graph[v+1][v] = weight
            else:
                self.graph[v][(v+1)%self.vertices] = weight
                self.graph[(v+1)%self.vertices][v] = weight


    def connectVertices(self,avg_degree):
        a, b = avg_degree-5, avg_degree + 5
        #a, b = 1, avg_degree + 1
        mu, sigma = avg_degree, 2
        dist = stats.truncnorm((a - mu) / sigma, (b - mu) / sigma, loc=mu, scale=sigma)
        values = dist.rvs(self.vertices)
        #print values

        #exit(0)
        for v in self.graph:
            for j in range(0,int(values[v-1])):
                weight = random.randint(10,2000)
                ad_v = random.randint(1,self.vertices)
                while(ad_v in self.graph[v] or ad_v == v):               # to avoid back edge
                    ad_v = random.randint(1,self.vertices)
                #self.graph[v].append((ad_v, weight))
                self.graph[v][ad_v] = weight
                self.graph[ad_v][v] = weight


    def printGraph(self):
        print self.graph
        pass

    def getAverageDegree(self):
        sum1 = reduce((lambda a,b:a+b), [len(self.graph[x]) for x in self.graph])
        return sum1/len(self.graph)

    def getNeighbours(self,v):
        pass



def generate(no_vertices = 500, avg_degree = 8):
    print "Generating Graph..."
    try:
        gen = GraphGenerator(no_vertices)
        gen.createEdges(avg_degree)
    except:
        print "generate_graph.py: Problem in graph generation. Exiting"
        exit(0)
    else:
        #gen.printGraph()
        #gen1 = GraphGenerator(vertices=1500)
        #gen1.createEdges(avg_degree=1100)
        #gen1.printGraph()
        #print gen1.getAverageDegree()
        print "Graph Generated."
        return gen.graph, gen.vertex
    

if __name__ == '__main__':
    generate()
