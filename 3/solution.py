import ast
import sys

# Intersections only occur on opposing plane lines (horizontal and vertical)
# Find nearest horizontal and vertical lines (that does not start at the central port)
# Side by side Same X = Horizontal
# Side by side Same Y = Vertical

# For Horizontal lines, find the Vertical line that the Y value falls in range
# For Vertical lines, find the Horizontal line that the X value falls in range
# If these 2 conditions meet, then they intersect at the X,Y coordinate
# MH distance is simply X + Y

# Example
# V1 contains list of vertical lines for wire 1
# H1 contains list of horizontal lines for wire 2
# V1	[(8,0) (8,5), (3,5) (3,2)]
# H1 	[(0,0) (8,0), (8,5) (3,5)]
# V2	[(0,0), (0,7), (6,7) (6,3)]
# H2 	[(0,7), (6,7), (6,3) (2,3)]

# Intersection occurs between these 2 Horizontal an Vertical lines
# Wire 1 Horizontal [(8,5) (3,5)], Wire 2 Vertical [(6,7) (6,3)]
# Wire 1 Vertical [(3,5) (3,2)], Wire 2 Horizontal [(6,3) (2,3)]

# Range of X for Wire 1 Horizontal 8-3, X value of Wire 2 = 6
# Range of Y for Wire 2 Vertical 7-3, Y value of Wire 1 = 5
# Intersection = 6,5
# MH = 6 + 5 = 11

# Range of X for Wire 2 Horizontal 6-2, X value of Wire 2 = 3
# Range of Y for Wire 1 Vertical 5-2, Y value of Wire 1 = 3
# Intersection = 3,3
# MH = 3 + 3 = 6 (Answer)


def line_generator(w):
    wh = []
    wv = []

    list_holder = []

    if w[0][0] == 'R' or w[0][0] == 'L':
        list_holder = [wh, wv]

    elif w[0][0] == 'U' or w[0][0] == 'D':
        list_holder = [wv, wh]

    coords = [0,0]

    for d in w:
        command = d[0]
        value = ast.literal_eval(d[1:])
        new_coords = coords.copy()

        if command == 'R':
            new_coords[0] = coords[0] + value
        elif command == 'L':
            new_coords[0] = coords[0] - value
        elif command == 'U':
            new_coords[1] = coords[1] + value
        elif command == 'D':
            new_coords[1] = coords[1] - value

        list_holder[0].append([coords, new_coords])

        coords = new_coords

        list_holder.reverse()

    return wh, wv

if __name__=='__main__':
    test = 1 

    # Inputs
    if test:
        #w1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
        #w2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
        w1 = ['R8','U5','L5','D3']
        w2 = ['U7','R6','D4','L4']
    else:
        with open('input.txt', 'r') as f:
            opcode_str = f.readline()

        opcode = list(ast.literal_eval(opcode_str))

    w1h, w1v = line_generator(w1)
    w2h, w2v = line_generator(w2)

    print(w1h)
    print(w2v)
    print(w2h)
    print(w1v)

