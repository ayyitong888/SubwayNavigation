from subway_map import SubwayMap
from station import Station, TransferStation

def build_map():
    m = SubwayMap()                                                                           
                                                                                       
    m.add_station(Station('A'))                                       # Add normal stations and transfer stations to demonstrate Inheritance and Polymorphism
    m.add_station(TransferStation('B', ['Line 1', 'Line 2']))  
    m.add_station(Station('C'))
    m.add_station(Station('D'))
    m.add_station(TransferStation('E', ['Line 2', 'Line 3']))  

    m.add_edge('A', 'B', 5)
    m.add_edge('B', 'C', 3)
    m.add_edge('A', 'C', 10)
    m.add_edge('C', 'D', 2)
    m.add_edge('B', 'E', 8)
    m.add_edge('E', 'D', 4)
    
    return m

def main():
    subway = build_map()
    
    while True:                                                                              
        print("\n=== Subway Navigation System ===")
        print("1. View all stations (Demonstrates Polymorphism)")
        print("2. Find shortest path by minimum stops (BFS)")
        print("3. Find shortest path by minimum time (Dijkstra)")
        print("4. Exit program")
        
        try:
            choice = int(input("Enter your choice (1-4): "))                                 
        except ValueError:
            print("\nInvalid input, please enter a number between 1 and 4.")
            continue

        if choice == 1:
            print("\nCurrent stations in system:")                                                                                
            for station_obj in subway.stations.values():               # Demonstrating Polymorphism: calling get_info() on different object types
                print("  " + station_obj.get_info())
        elif choice == 2:
            start = input("Enter start station: ").upper()
            end = input("Enter end station: ").upper()                                               
            path = subway.bfs(start, end)
            if path:
                print(f"\nPath with minimum stops: {' -> '.join(path)} (Total {len(path)-1} stops)")
            else:
                print("\nPath not found or invalid station name.")     
        elif choice == 3:
            start = input("Enter start station: ").upper()
            end = input("Enter end station: ").upper()                                               
            path, time = subway.dijkstra(start, end)
            if path:
                print(f"\nPath with minimum time: {' -> '.join(path)} (Estimated time: {time} minutes)")
            else:
                print("\nPath not found or invalid station name.")
        elif choice == 4:
            print("\nExiting program...")
            break
        else:
            print("\nInvalid input, please try again.")

if __name__ == '__main__':
    main()