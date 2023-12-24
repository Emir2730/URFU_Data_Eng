import numpy as np
import json

datafile = "/test/1/matrix_63.npy"

matrix = np.load(datafile)

size = len(matrix)
msd2 = dict()

# wtihout int cast got exteption
# TypeError: Object of type int64 is not JSON serializable

msd2['sum'] = int(matrix.sum())
msd2['avr'] = msd2['sum'] / (size * size)
msd2['sumMD'] = int(np.trace(matrix, offset = 0))
msd2['avrMD'] = msd2['sumMD'] / size
msd2['sumSD'] = int(np.trace(matrix[::-1], offset = 0))
msd2['avrSD'] = msd2['sumSD'] / size
msd2['max'] = int(matrix.max())
msd2['min'] = int(matrix.min())
norm_matrix2 = matrix / msd2['sum']

np.save(datafile+"_norm", norm_matrix2)

with open(datafile + "_json_out", mode="w") as f:
    f.write(json.dumps(msd2))



