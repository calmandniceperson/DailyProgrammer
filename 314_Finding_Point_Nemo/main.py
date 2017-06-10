# Author(s); Michael Koeppl
#
# Implemention of the DailyProgrammer challenge found at:
# https://www.reddit.com/r/dailyprogrammer/comments/6arlw4/20170512_chalenge_314_hard_finding_point_nemo/

import sys
import os
import numpy
import math
from recordclass import recordclass

def get_map_array():
    """
    Reads the input file and puts its content into
    a string array
    """

    # Open the input file in read mode
    file = open("input.txt", "r")

    # Read the first line to determine the width and length of the map
    firstline = file.readline()
    width = int(firstline.split(" ")[0])
    height = int(firstline.split(" ")[1])

    # Create an empty array of strings with the size of the map
    input_map = numpy.empty(shape=(height, width), dtype=str)

    for y in range(0, height):
        line = file.readline() # Read the next line
        for x in range(0, width):
            # Check if the index is still within the bounds
            # of the line. Since the line's length is only counted
            # to the point of the last '#', we need to check whether
            # we are above that length.
            if x < len(line):
                input_map[y][x] = line[x]
    file.close()
    return input_map

def find_nemo(input_map):
    MapPoint = recordclass("MapPoint", "x y")
    absolute_longest_distance = 0

    for y in range(0, len(input_map)):
        for x in range(0, len(input_map[y])):
            if input_map[y][x] == "#":
                # If the current point is not ocean, we skip.
                continue
            
            # Define the start and end point of the area to
            # check around the current map point.
            start_point = MapPoint(x=x-1, y=y-1)
            end_point = MapPoint(x=x+1, y=y+1)
            nearest_distance = 0

            # Repeat until the first occurrence of '#' around the current
            # map point has been found.
            # Within this loop, we check whether any of the points within the
            # square defined by 'start_point_ and 'end_point' is a '#' character.
            # If none is found, the size of the square is increased and the process
            # is repeated until a '#' character has been found.
            while nearest_distance == 0:
                for search_y in range(start_point.y, end_point.y + 1):
                    for search_x in range(start_point.x, end_point.x + 1):
                        if nearest_distance > 0:
                            break
                        if (search_y < 0 or search_y >= len(input_map)) or (search_x < 0 or search_x >= len(input_map[search_y])):
                            # If the current search index is not within the bounds of
                            # the map, we skip.
                            continue
                        if input_map[search_y][search_x] == '#':
                            nearest_distance = math.sqrt((math.fabs(search_y - y)**2 + math.fabs(search_x - x)**2))
                            # If the nearest "coast" to this point is farther away
                            # than the absolute longest distance, then set the absolute
                            # longest distance to this point's shortest distance to the
                            # next coast.
                            if nearest_distance > absolute_longest_distance:
                                absolute_longest_distance = nearest_distance
                                nemo_point = MapPoint(x = x, y = y)
                # Increase the size of the area around the current map point
                # that is searched.
                start_point.x -= 1
                start_point.y -= 1
                end_point.x += 1
                end_point.y += 1
    return nemo_point

def print_map(input_map):
    for y in range(0, len(input_map)):
        for x in range(0, len(input_map[y])):
            sys.stdout.write(input_map[y][x])
    print()

def main():
    """ main function """

    os.system("cls" if os.name == "nt" else "clear")

    input_map = get_map_array()
    print_map(input_map)

    nemo_point = find_nemo(input_map)

    print("Nemo point coordinates: {} {}".format(nemo_point.x, nemo_point.y))

if __name__ == "__main__":
    main()
