class Graph:
    EDGE_SIZE = 6

    def __init__(self, number_of_nodes):
        self.connections = {}
        self.shortest_distancies = {}

        nodes_range = number_of_nodes +1
        for node in range(1, nodes_range):
            self.shortest_distancies[node] = -1

    def connect(self, node_a, node_b):
        self.connections.setdefault(node_a, []).append(node_b)
        self.connections[node_a] = list(set(self.connections[node_a]))
        self.connections.setdefault(node_b, []).append(node_a)
        self.connections[node_b] = list(set(self.connections[node_b]))
    
    def calc_distancies_from(self, starter_node):
        del self.shortest_distancies[starter_node]
        self.calc_neighborhood([starter_node], 0)
        
    def calc_neighborhood(self, path, initial_distance):
        current_node = path[-1]
        node_connections = self.connections[current_node]
        neighborhood = list(set(node_connections) - set(path))
        
        for neighbor in neighborhood:
            calc_distance = self.find_shortest_distance_to_node(neighbor, initial_distance)
            
            if len(self.connections[neighbor]):
                new_path = path[:]
                new_path.append(neighbor)
                self.calc_neighborhood(new_path, calc_distance)
            else:
                continue

    def find_shortest_distance_to_node(self, node, path_distance):
        calc_distance = path_distance + self.EDGE_SIZE
            
        current_distance = self.shortest_distancies[node]
        
        if current_distance == -1 or current_distance > calc_distance:
            self.shortest_distancies[node] = calc_distance
        
        return calc_distance

    def print_distancies_from(self, starter_node):
        distancies_in_string = map(str, self.shortest_distancies.values())
        print(' '.join(distancies_in_string))

number_of_queries = input()
for i in range(number_of_queries):
    main_graph_info = raw_input().split()
    number_of_nodes = int(main_graph_info[0])
    number_of_edges = int(main_graph_info[1])

    graph = Graph(number_of_nodes)

    for j in range(number_of_edges):
        edge_info = raw_input().split()
        graph.connect(int(edge_info[0]), int(edge_info[1]))
    
    starter_node = input()
    graph.calc_distancies_from(starter_node)
    graph.print_distancies_from(starter_node)