import numpy as np

x = int(input("Enter the number of dice: "))
dc = int(input("Enter the DC: "))
modifier = int(input("Enter the Modifier: "))
crit_range = int(input("Enter the Crit Range: "))
true_dc = (dc - modifier)
#print(true_dc)
adv_successes = 0
adv_crit = 0
dis_successes = 0
dis_crit = 0

i=0
while i<x:
    rng = np.random.default_rng()
    rd20 = rng.integers(low=1, high=20, size=2)
    #print(rd20)
    if rd20[0] >= true_dc or rd20[1] >= true_dc:
        adv_successes += 1
    if rd20[0] >= crit_range or rd20[1] >= crit_range:
        adv_crit += 1
    i+=1

i=0
while i<x:
    rng = np.random.default_rng()
    rd20 = rng.integers(low=1, high=20, size=2)
    if rd20[0] >= true_dc and rd20[1] >= true_dc:
        dis_successes += 1
    if rd20[0] >= crit_range and rd20[1] >= crit_range:
        dis_crit += 1
    i+=1

print("Advantage Successes: ", adv_successes)
print("Advantage Criticals: ", adv_crit)
print("Disadvantage Successes: ", dis_successes)
print("Disadvantage Criticals: ", dis_crit)
