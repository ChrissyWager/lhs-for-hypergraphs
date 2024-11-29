import numpy as np
import p_stable_lsh.pstable as psl

dim = 100 # vector dimension
data = [np.random.random(dim) for _ in range(2)] # generate two vectors

r = 50.0 # the parameter $r$ in paper

m1 = psl.pstable(r, dim, metric_dim=1)
m1.lsh(data[0])
m2 = psl.pstable(r, dim, metric_dim=1)
m2.lsh(data[1])
print(m1.md(m2)) # estimate value
print(m1.p(np.average(sum(np.abs(data[0]-data[1]))))) # theoretical(true) value

m1 = psl.pstable(r, dim, metric_dim=2)
m1.lsh(data[0])
m2 = psl.pstable(r, dim, metric_dim=2)
m2.lsh(data[1])
print(m1.md(m2)) # estimate value
print(m1.p(np.sqrt(sum([i**2 for i in data[0]-data[1]])))) # theoretical(true) value
