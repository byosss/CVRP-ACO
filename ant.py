import numpy as np

class Ant:
    def __init__(self, graph, truck_capacity, pheromones, alpha, beta):
        self.graph = graph
        self.pheromones = pheromones

        self.truck_capacity = truck_capacity
        self.city_liv_weight = 3

        self.alpha = alpha
        self.beta = beta

        self.path = []
    

    def construire_chemin(self):
        self.path = [self.graph.depot]  # Commence par le dépôt centralisé
        not_visited = [i for i in range(self.graph.nbr_villes) if i != self.graph.depot]
        current_city = self.graph.depot

        truck_capacity_left = self.truck_capacity
        

        while len(not_visited) != 0:                                              # tant que toutes les villes n'ont pas été visité  

            prochaine_ville = self.selectionner_prochaine_ville(not_visited, current_city)    # on cherche la prochaine ville
            self.path.append(prochaine_ville)                                                 # on l'ajoute au path
            current_city = prochaine_ville
            not_visited.remove(prochaine_ville)

            truck_capacity_left -= self.graph.package_per_city[prochaine_ville]

            if truck_capacity_left <= 0:
                self.path.append(self.graph.depot) 
                truck_capacity_left = self.truck_capacity

        # Retourne au dépôt centralisé
        self.path.append(self.graph.depot)

    def selectionner_prochaine_ville(self, not_visited, current_city):

        probabilites = self.calculer_probabilites(not_visited, current_city)

        prochaine_ville = np.random.choice(not_visited, p=probabilites)

        return prochaine_ville

    def calculer_probabilites(self, not_visited, current_city):
        probabilites = []
        total = 0

        for ville in not_visited:

            pheromone = self.pheromones[current_city][ville]
            distance = self.graph.distances[current_city][ville]
            proba = (pheromone ** self.alpha) * ((1.0 / distance) ** self.beta)
            probabilites.append(proba)
            total += proba




        probabilites = [proba / total for proba in probabilites]
        
        return probabilites
