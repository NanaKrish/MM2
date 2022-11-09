
import math
import scipy.stats as st

"""The type of question concerns the relationship between risk and expected return with only one
 risky asset, where the returns on some k different assets are given along with the probability in the 
n different scenarios

Let us say that Scenario Probability Return K1 Return K2 Return K3
                    ω1      0.25         12%     11%         2%
                    ω2      0.75         12%     13%        22%
"""


p_n = [.25, .75]
k = [[.12, .12], [.11, .13], [.02, .22]]
k1 = [.12, .12]
k2 = [.11, .13]
k3 = [.02, .22]
#Create everything as a discrete random variable with consistent probability of risk
x1 = st.rv_discrete(values=(k1, p_n))
x2 = st.rv_discrete(values=(k2, p_n))
x3 = st.rv_discrete(values=(k3, p_n))
#The variance or standard deviation may more commonly be considered as the risk. More often not,
#standard deviation is considered a convenient indicator.
print(math.pow(x1.var(),0.5))
print(math.pow(x2.var(),0.5))
print(math.pow(x3.var(),0.5))




