#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdb


class Graph:
    def __init__(self, nodeList = []):
        
        #mapping of node names to nodes
        self.__nodes__ = {}
          
        for node in nodeList:
            self.__nodes__[node.id] = node
        
        
    def add(self, node):
        self.__nodes__[node.id] = node
        
        
    def getNode(self, id):
        return self.__nodes__.get(id, None)
        
class Node:
    def __init__(self, id, edges = []):
        
        self.id = id
        
        #list of node ids that can be reached from this node
        self.edges = edges


    def addEdge(self, nodeId):
        self.edges.append(nodeId)

    def __repr__(self):
        return self.id





def node_path(graph, nodeID1, nodeID2):
    # return list with single nodeID, if start is same as end location
    # return None if there is no path between the nodes
    # otherwise, return a list of nodeIDs corresponding to the shortest path from nodeID1 to nodeID2
    # nodeID1 should be first element, nodeID2 should be the last

    if nodeID1 == nodeID2:
        return nodeID1


          seen = () #nodes you've seen and inventory
          to_visit =() #nodes you've know how get to get there and want to visit.  




    

    return None
    
if __name__ == "__main__":

    #defines the variable "testGraph"
    exec(open("testData.py").read())
    pdb.set_trace()
    print(node_path(testGraph, "Monty", "Angie"))
    
        
        
