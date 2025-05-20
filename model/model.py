import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMapRetailer = {}



    def getAllNazioni(self):
        return DAO.getAllNazioni()

    def AddAllArchi(self, anno, nazione):
        allEdges = DAO.getAllArchi(anno,nazione, self._idMapRetailer)
        for edge in allEdges:
            r1 = edge[0]
            r2 = edge[1]
            self._graph.add_edge(r1,r2,weight=edge[2])


    def buildGraph(self, nazione, anno):
        self._graph.clear()
        nodes = DAO.getAllNodes(nazione)
        for r in nodes:
            self._idMapRetailer[r.Retailer_code] = r
        self._graph.add_nodes_from(nodes)
        self.AddAllArchi(anno, nazione)


    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return self._graph.number_of_edges()

    def getVolumi(self):
        lista_volumi = []
        for node in self._graph.nodes:
            vicini = self._graph.neighbors(node)
            peso = 0
            for v in vicini:
                peso += self._graph[node][v]["weight"]
            lista_volumi.append((node, peso))



