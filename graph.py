import math
import numpy as np
import random

import tsplib95

import networkx as nx
import matplotlib.pyplot as plt

class Graph:

    def __init__(self):
        self.nbr_villes = None
        self.depot = None

        self.distances = []
        self.node_positions = []
        self.package_per_city = []
    
    def load_tsp(self, path, depot):

        problem = tsplib95.load(path)

        self.nbr_villes = problem.dimension
        self.depot = depot - 1

        # Création de la liste 'node_positions'  
        self.node_positions = np.array(tuple(problem.node_coords.values()))

        # Création de la liste 'package_per_city'  
        self.package_per_city = [ random.randint(1, 3) for city in range(self.nbr_villes) ]

        # Création de la matrice 'distances'
        matrix = []
        for i in range(self.nbr_villes):

            row = []

            for j in range(self.nbr_villes):

                if i == j:
                    row.append(0.0)
                
                else:
                    u = self.node_positions[i]
                    v = self.node_positions[j]

                    distance = math.sqrt((v[0] - u[0])**2 + (v[1] - u[1])**2)
                    if distance == 0:
                        distance = 0.1

                    row.append(distance)
                
            matrix.append(row)

        self.distances = np.array(matrix)

    def generate_graph(self, nbr_ville, depot):

        self.nbr_villes = nbr_ville

        self.depot = depot - 1


        

        positions_temps = []
        for _ in range(nbr_ville):
            positions_temps.append((random.uniform(49000, 51000), random.uniform(5500, 6500)))
        

        self.node_positions = np.array(positions_temps)

        # Création de la liste 'package_per_city'  
        self.package_per_city = [ random.randint(1, 3) for city in range(self.nbr_villes) ]

        # Création de la matrice 'distances'
        matrix = []
        for i in range(self.nbr_villes):

            row = []

            for j in range(self.nbr_villes):

                if i == j:
                    row.append(0.0)
                
                else:
                    u = self.node_positions[i]
                    v = self.node_positions[j]

                    distance = math.sqrt((v[0] - u[0])**2 + (v[1] - u[1])**2)
                    if distance == 0:
                        distance = 0.1

                    row.append(distance)
                
            matrix.append(row)

        self.distances = np.array(matrix)
    





    def draw_graph(self, paths):

        G = nx.Graph()

        colors = ['red', 'orange', 'purple', 'cyan', 'magenta', 'blue', 'brown', 'gray', 'black', 'yellow']

        colors = [ '#{:06x}'.format(random.randint(0, 0xFFFFFF)) for _ in range(len(paths)) ]



        G.add_node(self.depot+1, pos=self.node_positions[self.depot], color='green', shape='s')

        depot_node_added = False

        for node, coords in enumerate(self.node_positions):
            
            
            for path_index in range(len(paths)):
                
                if node in paths[path_index] and node != self.depot:

                    G.add_node(node+1, pos=coords, color=colors[path_index], shape='o')

                    

        
        for path_index, path in enumerate(paths):
            for i in range(len(path) - 1):
                G.add_edge(path[i]+1,path[i+1]+1, color=colors[path_index])



        pos = nx.get_node_attributes(G, 'pos')
        colors = nx.get_node_attributes(G, 'color')
        shapes = nx.get_node_attributes(G, 'shape')

        nx.draw_networkx_edges(G, pos)

        # Dessiner les nœuds avec les labels (étiquettes)
        node_labels = {node: str(node) for node in G.nodes() if node != self.depot+1}
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='black')

        for node, shape in shapes.items():
            nx.draw_networkx_nodes(G, pos, node_size=100, nodelist=[node], node_color=colors[node], node_shape=shape)

        # Afficher le graphe
        plt.axis('off')
        plt.show()

    def get_distance(self, ville_depart, ville_arrivee):
        return self.distances[ville_depart][ville_arrivee]
