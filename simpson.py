import numpy as np

a = 0 //limit a
b = np.pi //lim b
n = 11 //no of intervals
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x) //function

I_simp = (h/3) * (f[0] + 2*sum(f[:n-2:2]) \
            + 4*sum(f[1:n-1:2]) + f[n-1])
err_simp = 2 - I_simp

print(I_simp)
print(err_simp)
