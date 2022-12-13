import networkx as nx
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, inputs, is_wheited):
        self.inputs = inputs
        self.is_wheited = is_wheited
        self.even_nodes = []
        self.related_list = {}
        self.incidence_matrix = []
        self.adj_list = {}
        self.nodes = []
        self.arcs = []

    def create_arcs(self):
        # Arcs Implementation
        if self.is_wheited:
            self.arcs = [arc[0] for arc in self.inputs]
        else:
            self.arcs = [arc for arc in self.inputs]
        return self.arcs

    def create_nodes(self):
        # Nodes Implementation
        # Nodes Filling
        for arc in self.inputs:
            for node in arc[0]:
                if node not in self.nodes:
                    self.nodes.append(node)

        self.nodes.sort()
        return self.nodes

    def create_adjacency_list(self):

        # Adjacency List Implementation
        for node in self.nodes:
            self.adj_list[node] = []

        # Adj_List Filling

        for arc in self.arcs:
            if arc[0] not in self.adj_list[arc[1]]:
                self.adj_list[arc[1]].append(arc[0])
                if arc[1] not in self.adj_list[arc[0]]:
                    self.adj_list[arc[0]].append(arc[1])

        return self.adj_list

    def create_incidence_matrix(self):
        # matrix Implementation

        # Matrix Initialisation

        self.incidence_matrix = []
        for node in self.nodes:
            self.incidence_matrix.append([])
        for j in range(len(self.nodes)):
            for i in range(len(self.nodes)):
                self.incidence_matrix[i].append(0)

        # Matrix Filling .

        for i in range(len(self.incidence_matrix)):
            current_row = self.incidence_matrix[i]
            current_node = self.nodes[i]
            current_node_adj_list = self.adj_list[current_node]
            for element in current_node_adj_list:
                current_row[self.nodes.index(element)] = 1

        return self.incidence_matrix

    def is_simple(self):
        for arc in self.arcs:
            if arc[0] == arc[1]:
                return False
        for i in range(len(self.arcs)):
            current_arc = self.arcs[i]
            for j in range(len(self.arcs)):
                current_compared_arc = self.arcs[j]
                if current_arc == current_compared_arc:
                    pass
                elif current_arc[0] == current_compared_arc[1] and current_arc[1] == current_compared_arc[0]:
                    return False
                else:
                    pass
            return True

    def is_complete(self):
        if self.is_simple():
            for node in self.nodes:
                if len(self.adj_list[node]) == len(self.nodes) - 1:
                    pass
                elif len(self.adj_list[node]) != len(self.nodes) - 1:
                    return False

            return True
        else:
            return False

    def is_related(self):

        def fill_related_list():

            for node in self.nodes:
                self.related_list[node] = []
                for element in self.adj_list[node]:
                    if element == node:
                        pass
                    elif element not in self.related_list[node]:
                        self.related_list[node].append(element)
                        for member in self.adj_list[element]:
                            if member == node:
                                pass
                            elif member not in self.adj_list[node]:
                                self.adj_list[node].append(member)
                            else:
                                pass
                    else:
                        pass

            return self.related_list

        fill_related_list()
        for node in self.nodes:
            if len(self.related_list[node]) == len(self.nodes) - 1:
                pass
            elif len(self.related_list[node]) != len(self.nodes) - 1:
                return False
            return True

    def is_eulerian(self):
        if self.is_related():
            self.even_nodes = []
            for node in self.nodes:
                if len(self.adj_list[node]) % 2:
                    self.even_nodes.append(node)
                else:
                    pass
            if len(self.even_nodes) >= len(node) - 2:
                return True
            else:
                return False

    def display_graph(self):
        my_graph = nx.Graph()
        for item in self.inputs:
            if self.is_wheited:
                my_graph.add_edge(item[0][0], item[0][1], weight=item[1])
            else:
                my_graph.add_edge(item[0], item[1])
        pos = nx.circular_layout(my_graph)

        nx.draw(my_graph, pos=pos, with_labels=True, node_size=1500, node_color='#7D1E6A', edge_color='#6A67CE',
                font_color='#FFF')
        nx.draw_networkx_edge_labels(my_graph, pos, font_size=15, font_color='#242F9B',
                                     edge_labels=nx.get_edge_attributes(my_graph, 'weight'))
        plt.show()

    def display_digraph(self):
        # edge_list = [(item[0][0], item[0][1], {'weight': item[1]}) for item in self.inputs]
        my_graph = nx.DiGraph()
        for item in self.inputs:
            if self.is_wheited:
                my_graph.add_edge(item[0][0], item[0][1], weight=item[1])
            else:
                my_graph.add_edge(item[0], item[1])
        pos = nx.circular_layout(my_graph)

        nx.draw(my_graph, pos=pos, with_labels=True, node_size=1500, node_color='#7D1E6A', edge_color='#6A67CE',
                font_color='#FFF')
        nx.draw_networkx_edge_labels(my_graph, pos, font_size=15, font_color='#242F9B',
                                     edge_labels=nx.get_edge_attributes(my_graph, 'weight'))
        plt.show()

    def kruskal(self):
        kruskal_list = []
        # sorting the inputs by their arc's weight
        initial_list = self.inputs
        initial_list.sort(key=lambda item: item[1])
        childhood_list = {}
        parent_list = []
        # transferring inputs to tuples (source, weight, destination)
        kruskal_edges = []
        for item in initial_list:
            kruskal_edges.append((item[0][0], item[1], item[0][1]))

        # filling kruskal list.
        def is_child(item):

            for char in parent_list:
                if item in childhood_list[char]:
                    return True
                else:
                    return False

        def is_parent(item):
            for char in parent_list:
                if item != char:
                    pass
                else:
                    return True
            return False

        def get_parent(item):
            for char in parent_list:
                if item in childhood_list[char]:
                    return char
                else:
                    return None

        for couple in kruskal_edges:
            element0 = couple[0]
            element2 = couple[2]
            parent0 = get_parent(couple[0])
            parent2 = get_parent(couple[2])
            isChild0 = is_child(couple[0])
            isChild2 = is_child(couple[2])
            isParent0 = is_parent(couple[0])
            isParent2 = is_parent(couple[2])
            if len(kruskal_list) == 0:
                kruskal_list.append(couple)
                childhood_list[couple[0]] = [couple[2]]
                parent_list.append(couple[0])
            else:
                if (not isChild0 and not isParent0) and (not isChild2 and not isParent2):
                    kruskal_list.append(couple)
                    parent_list.append(element0)
                    childhood_list[element0] = [element2]
                elif (not isChild0 and not isParent0) and isChild2:
                    kruskal_list.append(couple)
                    childhood_list[parent2].append(element0)
                elif (not isChild0 and not isParent0) and isParent2:
                    kruskal_list.append(couple)
                    childhood_list[element2].append(element0)
                elif (not isChild2 and not isParent2) and isParent0:
                    kruskal_list.append(couple)
                    childhood_list[element0].append(element2)
                elif (not isChild2 and not isParent2) and isChild0:
                    kruskal_list.append(couple)
                    childhood_list[parent0].append(element2)
                elif isChild0 and isChild2:
                    if parent0 == parent2:
                        pass
                    else:
                        kruskal_list.append(couple)
                        for cha in childhood_list[parent0]:
                            childhood_list[parent2].append(cha)
                        childhood_list[parent2].append(parent0)
                        parent_list.remove(parent0)
                        childhood_list.pop(parent0)
                elif isChild0 and isParent2:
                    if parent0 == element2:
                        pass
                    else:
                        kruskal_list.append(couple)

                        for el in childhood_list[parent0]:
                            childhood_list[element2].append(el)
                        childhood_list[element2].append(parent0)
                        childhood_list.pop(parent0)
                        parent_list.remove(parent0)
                elif isChild2 and isParent0:
                    if parent2 == element0:
                        pass
                    else:
                        kruskal_list.append(couple)
                        for char in childhood_list[parent2]:
                            childhood_list[element0].append(char)
                        childhood_list[element0].append(parent2)
                        childhood_list.pop(parent2)
                        parent_list.remove(parent2)
                else:
                    if element0 == element2:
                        pass
                    else:
                        kruskal_list.append(couple)
                        for ch in childhood_list[element0]:
                            childhood_list[element2].append(ch)
                        childhood_list[element2].append(element0)
                        childhood_list.pop(element0)
                        parent_list.remove(element0)
        return kruskal_list

    visited_dfs = set()  # Set to keep track of visited nodes of the graph.

    def dfs(self, visited_dfs, graph, node):  # graph is the adj_list || visited is the set that will be
        if node not in visited_dfs:  # returned || node is the node to start from
            visited_dfs.add(node)
            for neighbour in graph[node]:
                self.dfs(visited_dfs, graph, neighbour)
        return visited_dfs

    visited_bfs = []  # List for visited nodes.

    def bfs(self, visited_bfs, graph, node):  # function for BFS
        queue = []  # Initialize a queue
        visited_bfs.append(node)
        queue.append(node)

        while queue:  # Creating loop to visit each node
            m = queue.pop(0)
            print(m, end=" ")

            for neighbour in graph[m]:
                if neighbour not in visited_bfs:
                    visited_bfs.append(neighbour)
                    queue.append(neighbour)
        return visited_bfs

    # Prime's Algorithme:

    def prime(self, start):
        self.create_nodes()
        prime_final_list = []
        prim_book = {}
        for node in self.nodes:
            prim_book[node] = []
            for item in self.inputs:
                if item[0][0] != node and item[0][1] != node:
                    pass
                else:
                    prim_book[node].append(item)

        for node in self.nodes:
            prim_book[node].sort(key=lambda item: item[1])

        if start not in self.nodes:
            return "The Given node does not exist in this Graph"
        else:
            pass

        checked_nodes = []

        def fill_prime():
            while len(prim_book) != 1:
                if len(checked_nodes) == 0:
                    checked_nodes.append(start)
                next_edge = prim_book[start][0]
                next_node = next_edge[0][1] if (next_edge[0][1] not in checked_nodes) else next_edge[0][0]
                prime_final_list.append(next_edge)
                checked_nodes.append(next_node)
                prim_book[start].remove(next_edge)
                prim_book[next_node].remove(next_edge)
                for lis in prim_book[next_node]:
                    prim_book[start].append(lis)
                del prim_book[next_node]
                prim_book[start].sort(key=lambda ite: ite[1])

        fill_prime()

        return prime_final_list

    # Dijkstra's Algorithm

    def dijkstra(self, start):

        self.create_nodes()
        # ===================================Initialisation======================================
        if start not in self.nodes:
            return "Le Point de départ n'appartient pas a ce graphe. Verifiez vos données"
        for item in self.inputs:
            if int(item[1]) < 0:
                return "L'algorithme de Dijkstra ne peut pas être exécuté en raison de l'existence d'un bord négatif, " \
                       "choisissez Bellman-Ford à la place "
        checked_nodes = [start]
        non_checked_nodes = [node for node in self.nodes if node not in checked_nodes]
        current_source = checked_nodes[-1]
        distances_list = {}
        predecessors_list = {}
        for item in self.inputs:
            if current_source in item[0]:
                distances_list[item[0][1]] = item[1]
                predecessors_list[item[0][1]] = current_source
            else:
                for char in item[0]:
                    if char in distances_list:
                        pass
                    else:
                        distances_list[char] = 9999999999999999999999999999
                    if char in predecessors_list:
                        pass
                    else:
                        predecessors_list[char] = "N"
        # ================================= Algorithme Start ====================================
        while len(non_checked_nodes) != 0:

            # Get The Smallest item in the distances list.

            smallest_one_value = 99999999999999
            smallest_one_key = None
            for dis in distances_list:
                if int(distances_list[dis]) < int(smallest_one_value) and dis not in checked_nodes:
                    smallest_one_value = distances_list[dis]
                    smallest_one_key = dis
                else:
                    pass
            checked_nodes.append(smallest_one_key)
            non_checked_nodes.remove(smallest_one_key)
            # Get The none checked Neighbors of The Smallest One

            smallest_one_neighbors = []
            for element in self.inputs:
                if smallest_one_key == element[0][0] and element[0][1] not in checked_nodes:
                    smallest_one_neighbors.append((element[0][1], element[1]))
                elif smallest_one_key == element[0][1] and element[0][0] not in checked_nodes:
                    smallest_one_neighbors.append((element[0][0], element[1]))
                else:
                    pass

            # Calculate and Update The distances:

            for neighbor in smallest_one_neighbors:
                minimum = min(int(distances_list[neighbor[0]]),
                              int(distances_list[smallest_one_key]) + int(neighbor[1]))
                if int(minimum) < int(distances_list[neighbor[0]]):
                    distances_list[neighbor[0]] = int(minimum)
                    predecessors_list[neighbor[0]] = smallest_one_key
                else:
                    pass
            smallest_one_neighbors.clear()
        return f' Distances : {distances_list}, Predecesseurs: {predecessors_list}'

    # Bellman Ford's Algorithme

    def bellman_ford(self, start):
        # ===================================Initialisation======================================
        # Filling Edges List
        self.create_nodes()

        edges_list = []
        for item in self.inputs:
            source = item[0][0]
            destination = item[0][1]
            weight = item[1]
            edges_list.append((source, destination, weight))

        # Filling Distances List

        distances_list = {}
        for node in self.nodes:
            distances_list[node] = float('infinity') if node != start else 0
        # Filling Predecessors List
        bf_list = []
        predecessors_list = {}
        for node in self.nodes:
            predecessors_list[node] = 'N' if node != start else '-'
        # ================================= Algorithme Start ====================================
        # Bellman-Ford Algorithme Running
        for i in range(len(self.nodes)):
            for edge in edges_list:
                if distances_list[edge[1]] > distances_list[edge[0]] + int(edge[2]):
                    distances_list[edge[1]] = distances_list[edge[0]] + int(edge[2])
                    predecessors_list[edge[1]] = edge[0]
        return f' Distances : {distances_list}, Predecesseurs: {predecessors_list}'
