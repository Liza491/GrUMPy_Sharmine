numVars = 3
#points = [[2.5, 4.5], [6.5, 0.5],
#          [7, 5.7], [7.7, 5], [-2, -2]]
#rays = []
c = [1, 9, 7]

A = [[1.05,   5,   1],   
     [1.05,    10,     10],
     [1.05,    11,   5],
     #c
     ]
     
b = [0,
     0,
     0,
     #-1
     ]

sense = ('<=', 'Max')
