import numpy as np
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None) # same as np.recfromcsv(file), which has delimiter, names and dtype by default
np.shape(data)
data['Survived'][-4 :]