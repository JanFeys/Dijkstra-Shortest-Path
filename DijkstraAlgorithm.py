#!/usr/bin/env python3

import time
from collections import defaultdict
import sys
import heapq

class WeightedDirectedGraph():
    def __init__(self, nr_vs):
        self.nr_vs = nr_vs #number of vertices
        self.es = defaultdict(set) #dictionary of sets that, for every vertex, stores heads of edges leaving it
        self.ws = dict() #dictionary that stores weight of each edge

    def show_nr_vs(self):
        return self.nr_vs

    def add_edge(self, t, h, w):
        (self.es[t]).add(h)
        self.ws[(t,h)] = w

    def get_edges(self, t):
        return self.es[t]
    
    def get_weight(self,t,h):
        return self.ws[(t,h)]

    def removeEdge(self, t, h):
        (self.es[t]).remove(h)
        del self.ws[(t,h)]

    def display(self):
        nr_es_present = 0
        for t in self.es:
            for h in self.es[t]:
                print("edge from %s to %s with weight %s" % (t, h, self.ws[(t,h)]))
                nr_es_present += 1
        print("there are %s edges in total" % nr_es_present)

    def run_Dijkstra(self,s,f):
        self.ps = [None for v in range(self.nr_vs)] #list of parent of each vertex
        self.ds = [sys.maxsize for v in range(self.nr_vs)] #list of distances of each vertex
        q = [] #priority queue for Dijkstra
        
        heapq.heappush(q,[0,s]) #distance and vertex are paired, queue will sort by distance
        self.ds[s] = 0

        while q:
            dv = heapq.heappop(q)
            v = dv[1]
            
            if (v == f):
                break
        
            for h in self.es[v]:
                new_d = self.ds[v] + self.ws[(v,h)]
                if new_d < self.ds[h]:
                    self.ds[h] = new_d
                    self.ps[h] = v
                    heapq.heappush(q,[new_d,h])
    
        path = []
        end = f
        while end is not None:
            path.append(end)
            end = self.ps[end]

        path.reverse()

        return path, [self.ds[v] for v in path]

if __name__ == "__main__":
    file_name =  'Dijkstrasimpletest1.txt'

    start_time = time.time()

    with open(file_name, 'r') as f:
        nr_vs, _ = f.readline().strip().split()
        nr_vs = int(nr_vs)
        graph = WeightedDirectedGraph(nr_vs)

        for line in f:
            t, h, w = line.strip().split()
            t, h, w = int(t)-1, int(h)-1, int(w)
            graph.add_edge(t,h,w)

    start = 0
    finish = 4

    path, distances = graph.run_Dijkstra(start,finish)
    print(path, distances)
    
    end_time = time.time()
    print(end_time - start_time)


