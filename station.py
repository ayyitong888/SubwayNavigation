class Station:
    """Base class representing a subway station."""
    def __init__(self, name):
        self.name = name                                     # set the name
        self.connections = {}                                # Dictionary for connections
                                                             
    def get_name(self):                                      # Getter
        return self.name
                                                          
    def set_name(self, new_name):                            # Setter
        if new_name:
            self.name = new_name

    def add_connection(self, neighbor_name, time_cost):      # Add neighbor edge
        self.connections[neighbor_name] = time_cost

    def get_info(self):                                      # Method to be overridden (Polymorphism)
        return f"[Station] {self.get_name()}"


class TransferStation(Station):
    """Subclass representing a transfer station (Inheritance)."""
    def __init__(self, name, lines):
        super().__init__(name)                               # Call parent constructor
        self.lines = lines                                   # lines list
                                                            
    def get_lines(self):                                     # Getter
        return self.lines
                                       
    def set_lines(self, new_lines):                          # Setter
        if new_lines:
            self.lines = new_lines

    def get_info(self):                                      # Override method (Polymorphism)
        lines_str = ", ".join(self.get_lines())
        return f"[!] [Transfer Station] {self.get_name()} (Lines: {lines_str})"