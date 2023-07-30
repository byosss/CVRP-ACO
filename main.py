from graph import Graph
from ACOalgo import ACOalgo

#----------------------------------------------------------#

# Paramètres du problème et de l'algorithme
nbr_iterations = 100
nbr_fourmis = 20

alpha = 1
beta = 2
rho = 0.5
q = 100

city_depot = 1
truck_capacity = 20

#----------------------------------------------------------#

# Création du graphe
print("loading graph...")
graph = Graph()
graph.load_tsp('files/dj38.tsp', city_depot)
#graph.generate_graph(100, city_depot)
print("done !")

# Création de l'algorithme ACO
print("ACO algorithm initialization...")
aco = ACOalgo(graph, truck_capacity, nbr_fourmis, alpha, beta, rho, q)
print("done !")

#----------------------------------------------------------#

# Exécution de l'algorithme
aco.lancer_algorithme(nbr_iterations)

# Print de la meilleure solution
aco.afficher_meilleure_solution()

# Affichage du graphe avec le chemin trouvé
graph.draw_graph(aco.meilleure_solution)

#----------------------------------------------------------#