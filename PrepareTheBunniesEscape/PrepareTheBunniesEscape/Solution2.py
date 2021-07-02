class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_wall(self):
        global matrix
        return bool(matrix[self.y][self.x])

    def distance(self):
        global end_node
        return abs(self.x - end_node.x) + abs(self.y - end_node.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __str__(self):
        return str([self.x, self.y])

    def get_neighbours(self):
        global matrix
        for i in range(-1,2):
            for j in range(-1,2):
                if abs(i) != abs(j):
                    x = self.x + i
                    y = self.y + j
                    if  not (x < 0 or y < 0 or x >= len(matrix[0]) or y >= len(matrix)):
                        yield Node(x, y)

class Path:
    def __init__(self, node, parent=None, length=1):
        self.node = node
        self.parent = parent
        self.length = length

        self.heuristic = self.length + self.node.distance()
        
        if self.parent is not None:
            self.gone_through_wall = self.parent.gone_through_wall or node.is_wall()
        else:
            self.gone_through_wall = False

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __eq__(self, other):
        return self.node == other.node and self.gone_through_wall == other.gone_through_wall

    def __str__(self):
        history = []
        current_node = self
        while current_node is not None:
            history.append(str(current_node.node))
            current_node = current_node.parent
        return "\n".join(history)

    def similar(self, other):
        return self.node == other.node

def solution(map):
    # Set the global map variable
    global matrix
    matrix = map

    # Instantiate start node
    start_node = Node(0, 0)
    # Instantiate end node
    global end_node
    end_node = Node(len(map[0])-1, len(map)-1)

    # Make open and closed lists
    closed_list = []
    open_list = [Path(start_node)]

    while len(open_list) > 0:
        current_node = open_list[0]
        for node in open_list:
            if node < current_node:
                current_node = node

        if current_node.node == end_node:
            return current_node.length
            
        # Add to closed list
        closed_list.append(current_node)
        # Remove from open list
        open_list.remove(current_node)

        for node in current_node.node.get_neighbours():
            current_neighbour = Path(node, current_node, current_node.length + 1)
            # May only remove one wall
            if current_node.gone_through_wall == True and current_neighbour.node.is_wall():
                continue

            # Already in the closed list?
            if current_neighbour in closed_list:
                continue

            # Were we already there?
            previous_node = current_node.parent
            if previous_node and previous_node.similar(current_neighbour):
                continue

            # Is there a better path?
            if current_neighbour in open_list:
                for node in open_list:
                    if current_neighbour == node and current_neighbour.length < node.length:
                        open_list.remove(node)
                        open_list.append(current_neighbour)
            else:
                open_list.append(current_neighbour)

    return "NO PATH FOUND"

if __name__ == "__main__":
    print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
