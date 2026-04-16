import heapq

class SubwayMap:                                                               # map class
    def __init__(self):
        self.stations = {}                                                     # store stations

    def add_station(self, station):                                            # add station to dict                                                                               
        self.stations[station.get_name()] = station                            # Use getter

    def add_edge(self, station1_name, station2_name, weight):                  # add edge to graph
        if station1_name in self.stations and station2_name in self.stations:
            self.stations[station1_name].add_connection(station2_name, weight) # add edge 1
            self.stations[station2_name].add_connection(station1_name, weight) # add edge 2

    def bfs(self, start_name, end_name):                                       # bfs algorithm
        if start_name not in self.stations or end_name not in self.stations:
            return None
        queue = [[start_name]]                                                # queue
        visited = set([start_name])                                           # visited set

        while queue:
            path = queue.pop(0)                                               # pop first
            current = path[-1]
            if current == end_name:
                return path                                                   # found
            for neighbor in self.stations[current].connections:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return None                                                           # not found

    def dijkstra(self, start_name, end_name):                                 # dijkstra algorithm
        if start_name not in self.stations or end_name not in self.stations:
            return None, 999999
        distances = {station: 999999 for station in self.stations}            # init distances
        distances[start_name] = 0
        pq = [(0, start_name)]                                                # priority queue
        predecessors = {station: None for station in self.stations}

        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if current_dist > distances[current_node]:
                continue
            if current_node == end_name:
                break
            for neighbor, weight in self.stations[current_node].connections.items():
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node                    # update predecessor
                    heapq.heappush(pq, (distance, neighbor))
        path = []
        current = end_name
        while current is not None:
            path.insert(0, current)
            current = predecessors[current]        
        if distances[end_name] == 999999:                                    # check if reached
            return None, 999999
        return path, distances[end_name]