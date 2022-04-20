import numpy as np
from datetime import datetime
start_time = datetime.now()

x = np.random.randint(10, size=(128,128))
y = np.random.randint(10, size=(128,128))

r = [[0 for x in range(128)] for y in range(128)]


for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
 
            r[i][j] += x[i][k] * y[k][j]

print(r) 
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
