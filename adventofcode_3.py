#!/usr/bin/python

import numpy
from scipy.spatial.distance import cdist
from collections import defaultdict, Counter

INTERSECTIONS = {}
SHORTEST_STEPS = defaultdict(list)
GLOBAL_COUNTER = 0

POSITIONING = Counter()
  

def wire_translate(matrix, op, start, spaces, wire):
    spaces = int(spaces)+1
    if wire ==3 or wire==4:
      global GLOBAL_COUNTER
    for i in range(spaces):
        if i:
            if wire ==3 or wire==4:
              POSITIONING['wire' + str(wire)] += 1
            if op == "plusrow":
                X,Y = start[0], start[1]+i
            if op == "minusrow":
                X,Y = start[0], start[1]-i
            if op == "pluscolumn":
                X,Y = start[0]+i, start[1]
            if op == "minuscolumn":
                X,Y = start[0]-i, start[1]
            if matrix[X][Y] == 8:
                SHORTEST_STEPS[str(wire)+ '@' +str(X) + str(Y)] = POSITIONING['wire' + str(wire)]
                #continue
            if matrix[X][Y] > 0:
                INTERSECTIONS[wire + i] = (X,Y)
                matrix[X][Y] = 8
            else:
              matrix[X][Y] = wire
    return matrix, (X,Y)


def matrix_travel(matrix, start, instruction, wire):
    instructionmap = {"R": "plusrow",
                      "L": "minusrow",
                      "U": "minuscolumn",
                      "D": "pluscolumn",
                    }
    direction, spaces = instruction[0], instruction[1:]
    matrix, endposition = wire_translate(matrix, 
                               instructionmap[direction],
                               start, 
                               spaces,
                               wire,)
    return matrix, endposition

def matrix_loop(matrix,start,iterable,identifier):
    counter = 0
    endposition = (0,0)
    for position in iterable:
          if counter == 0:
              matrix, endposition = matrix_travel(matrix, 
                                                  start, 
                                                  position, 
                                                  wire=identifier)
              counter += 1
          else:
              matrix, endposition = matrix_travel(matrix, 
                                                  endposition, 
                                                  position, 
                                                  wire=identifier)
    return endposition

def main():
    #matrix = numpy.zeros( (10,11) )
    #matrix = numpy.zeros( (1000,1100) )
    matrix = numpy.zeros( (20000,20000) )
    #matrix[8][1] = 0
    #start = (8,1)
    matrix[10000][10000] = 0
    start = (10000,10000)
    #wire1 = ["R8","U5","L5","D3"]
    #wire2 = ["U7","R6","D4","L4"]
    #wire1 = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
    #wire2 = ["U62","R66","U55","R34","D71","R55","D58","R83"]
    #wire1 = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
    #wire2 = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]
    with open('input.log') as f:
      wire1 = f.readline()
      wire2 = f.readline()
    wire1 = wire1.split(',')
    wire2 = wire2.split(',')

    matrix_loop(matrix,start,wire1,1)
    matrix_loop(matrix,start,wire2,2)

    #end1, end2 = numpy.where(matrix == 8)
    #print(start,end1,end2,INTERSECTIONS)
    outlist = []
    for k,v in INTERSECTIONS.items():
      if v[0] < 0 or v[1] < 0:
        continue
      p_a = numpy.array(v)
      p_b = numpy.array(start)
      p_a = p_a.reshape(1, -1)
      p_b = p_b.reshape(1, -1)
      out = cdist(p_a, p_b, metric='cityblock')
      outlist.append(out)
    print("manhattan distance closest to starting point:", sorted(outlist)[0])

    matrix_loop(matrix,start,wire1,3)
    matrix_loop(matrix,start,wire2,4)
    totalsum = 0
    hash_1 = {k:v for k,v in SHORTEST_STEPS.items() if k.startswith('3')}
    hash_2 = {k:v for k,v in SHORTEST_STEPS.items() if k.startswith('4')}
    hash_1 = (sorted(hash_1.items(), key=lambda item: item[1]))
    results = []
    for k,v in hash_1:
      try:
        results.append(v+hash_2['4@' + k.split('@')[1]])
      except:
        pass
    print('shortest route to first intersection,',sorted(results)[0])

if __name__ == "__main__":
    main()
