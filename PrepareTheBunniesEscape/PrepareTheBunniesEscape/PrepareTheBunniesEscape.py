
class Node:
    def __init__(self, position, wall=False, score=0, parent=None, gone_through_wall=False):
        self.position = position
        # Is a wall?
        self.wall = wall
        self.score = score
        self.parent = parent
        self.gone_through_wall = gone_through_wall

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return "%s: %s, %s" % (str(self.position), str(int(self.wall)), str(self.score))

    def distance(self, end_node):
        return abs(self.position[0] - end_node.position[0]) + abs(self.position[1] - end_node.position[1])

    def heuristic(self, end_node):
        return abs(end_node.position[0] - self.position[0])**2 + abs(end_node.position[1] - self.position[1])**2

def solution(map):
    # A* path finding algorithm again

    # Instantiate start and end nodes
    start_node = Node([0,0])
    end_node = Node([len(map[0])-1, len(map)-1])

    # initialise open and closed lists
    open_list = [start_node]
    closed_list = []

    # Loop while nodes exist on the open list
    while len(open_list) > 0:
        lowest = 99
        idx = 0

        # Get the lowest scoring node
        for i, node in enumerate(open_list):
            if node.score < lowest:
                lowest = node.score
                idx = i
        # Remove node from open list
        current_node = open_list.pop(idx)
        # Add node to closed list
        closed_list.append(current_node)

        # At the end?
        if current_node == end_node:
            path = 0
            while current_node is not None:
                path += 1
                current_node = current_node.parent
            return path

        # Get neighbour nodes
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Make sure not a diagonal and not stationary
                if i == j:
                    continue
                position = [current_node.position[0] + i, current_node.position[1] + j]
                # Check move is legal
                if position[0] < 0 or position[1] < 0 or position[0] >= len(map[0]) or position[1] >= len(map):
                    continue

                # Is this position a wall?
                is_wall = bool(map[position[1]][position[0]])
                # Instantiate new node, increment score and set parent and gone_through_wall to current node values
                new_node = Node(position, wall=is_wall, score=1, parent=current_node, gone_through_wall=current_node.gone_through_wall)
                new_node.score = new_node.distance(end_node) + new_node.heuristic(end_node)

                # Does this node already exist?
                in_closed_list = False
                for node in closed_list:
                    if new_node == node and new_node.score == node.score:
                        in_closed_list = True
                        continue
                if in_closed_list == True:
                    continue

                # Have we already gone through a wall?
                if (is_wall == True and current_node.gone_through_wall == False):
                    new_node.gone_through_wall = True
                elif is_wall == True:
                    continue

                # On open list?
                exists = None
                for node in open_list:
                    if new_node == node:
                        exists = node
                        continue
                if not exists:
                    open_list.append(new_node)
                elif new_node.score < exists.score:
                    exists.score = new_node.score
                    exists.parent = new_node.parent

    return "NO POSSIBLE PATH"

if __name__ == "__main__":
    print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))