# Subway Navigation System (COMP 8090SEF Project)
**Topic:** Real-life problem solving using OOP
**Data Structure:** Graph (Not covered in class)
**Algorithm:** Dijkstra's Algorithm for Shortest Path (Not covered in class)

## Modules (Meeting the 3-module requirement):
1. station.py: Station and Route classes (Entity objects)
2. subway_map.py: SubwayMap class (Graph logic and Dijkstra implementation)
3. main.py: CLI User Interface and System initialization

## 🚀 User Guide (How to Run the Code)

This program is a command-line application written in pure Python. No external or third-party libraries (like pandas or networkx) are required.

### Prerequisites
- Ensure you have **Python 3.x** installed on your system.

### How to Run
1. Open your terminal or command prompt.
2. Navigate to the project directory where the source code is located.
3. Execute the following command to start the Subway Navigation System:
   ```bash
   python main.py
   ```
   *(Note: If you are using macOS/Linux, you might need to use `python3 main.py`)*

### Interacting with the System
Once the program is running, you will see a main menu. You can interact with the system by typing the corresponding option numbers:
- **Enter `1`**: View all available subway stations (Transfer stations will be highlighted with a `*`).
- **Enter `2`**: View all subway lines and their connected stations.
- **Enter `3`**: Use the Dijkstra algorithm to find the shortest travel time between two stations. (You will be prompted to input the 'Start Station' and 'End Station' names, e.g., `A` and `D`).
- **Enter `4`**: Exit the program safely.

If you input an invalid option or station name, the system will catch the error and prompt you to try again.
```
