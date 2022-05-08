
import random

e = 0
f = 0
g = 0
ef = 0
fg = 0
ge = 0

x = 10 ** 3
for i in range(x):
    coins = [random.choice((0, 1)), random.choice((0, 1)), random.choice((0, 1))]
    cn = coins.count(1)
    if cn == 0:
        e += 1 / x
        g += 1 / x
        ge += 1 / x
    if cn == 1:
        g += 1 / x
    if cn == 2:
        f += 1 / x
        g += 1 / x
        fg += 1 / x
    if cn == 3:
        e += 1 / x
        f += 1 / x
        ef += 1 / x
        
print("E : {:.3f} \nF : {:.3f} \nG : {:.3f} \nEF : {:.3f} \nFG : {:.3f} \nGE : {:.3f}".format(e, f, g, ef, fg, ge))
    
print("Deviation from independence, measured as the difference P(A) * P(B) - P(AB) :")
print("EF : {:.3f}, FG : {:.3f}, GE : {:.3f}".format(e * f - ef, f * g - fg, g * e - ge))
