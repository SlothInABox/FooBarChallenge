class Image:
    def __init__(self, b_is_guard, position, source_position):
        self.is_guard = b_is_guard
        self.position = position

        # Calculate distance from source
        x = position[0] - source_position[0]
        y = position[1] - source_position[1]
        distance = (x ** 2 + y ** 2) ** 0.5
        self.distance = distance

        # Calculate unit vector from source
        self.unit_vector = (0.0, 0.0)
        if distance != 0:
            # Round values to avoid floating point precision errors
            self.unit_vector = (round(x / distance, 10),
                                round(y / distance, 10))

    def __eq__(self, other):
        # For use with the hashing
        return self.unit_vector == other.unit_vector

    def __lt__(self, other):
        return self.distance < other.distance

    def __hash__(self):
        # For assigned to dictionaries
        return hash(self.unit_vector)

    def is_in_range(self, distance):
        return self.distance <= distance


def make_images(dimensions, original_you, original_guard, distance):
    # Calculate the minimum number of reflections to make in an axis
    def max_reflections(axis): return - (-distance // dimensions[axis])

    yous = []
    guards = []
    # Iterate over x reflections
    for i in range(-max_reflections(0), max_reflections(0) + 1):
        you_image_x = reflect_coordinate(
            original_you.position[0], dimensions[0], i)
        guard_image_x = reflect_coordinate(
            original_guard.position[0], dimensions[0], i)
        # Iterate over y coordinates
        for j in range(-max_reflections(1), max_reflections(1) + 1):
            you_image_y = reflect_coordinate(
                original_you.position[1], dimensions[1], j)
            guard_image_y = reflect_coordinate(
                original_guard.position[1], dimensions[1], j)

            # Make new you and add to list
            new_you = Image(
                False, [you_image_x, you_image_y], original_you.position)
            yous.append(new_you)

            # Make new guard and add to list
            new_guard = Image(
                True, [guard_image_x, guard_image_y], original_you.position)
            guards.append(new_guard)
    return yous, guards


def reflect_coordinate(coordinate, dimension, reflect_num):
    reflected_coordinate = 0
    # Is it an even reflection?
    if reflect_num % 2 == 0:
        reflected_coordinate = dimension * reflect_num + coordinate
    else:
        reflected_coordinate = dimension * (reflect_num + 1) - coordinate
    return reflected_coordinate


def solution(dimensions, your_position, guard_position, distance):
    # Instantiate you and guard
    you = Image(False, your_position, your_position)
    guard = Image(True, guard_position, your_position)

    # Make lists of all yous and all guards
    you_images, guard_images = make_images(
        dimensions, you, guard, distance)

    images = dict()
    valid_guards = dict()

    # Iterate over you and guard images (you first)
    for image_list in (you_images, guard_images):
        for image in image_list:
            if image.is_in_range(distance):
                # Use unit vector as key
                if image not in images or image < images[image]:
                    images[image] = image
                    if image.is_guard:
                        valid_guards[image] = image

    return len(valid_guards)


if __name__ == "__main__":

    # test1 = solution([3, 2], [1, 1], [2, 1], 4)
    # print(test1)

    # test2 = solution([300, 275], [150, 150], [185, 100], 500)
    # print(test2)

    test3 = solution([2, 5], [1, 2], [1, 4], 11)
    print(test3)
