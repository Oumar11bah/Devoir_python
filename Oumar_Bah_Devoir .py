
#%%
                #Exercice 1
def fibo_sup(n):
    premier, second = 1, 1
    while second <= n:
        premier, second = second, premier + second
    return second

# Affichage 
print("Fibonacci de 75 est:", fibo_sup(75))
print("Fibonacci de 50 est:", fibo_sup(50))
print("Fibonacci de 100 est:", fibo_sup(100))

# %%
                 #Exercice 2
import numpy as np

boston = [2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93]
seattle = [6.83, 3.63, 7.20, 2.68, 2.05, 2.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.85]

# Calcul des précipitations totales et moyennes
total_boston = round(sum(boston), 2)
moyenne_boston = round(np.mean(boston), 2)
total_seattle = round(sum(seattle), 2)
moyenne_seattle = round(np.mean(seattle), 2)

# Mois avec précipitations supérieures à la moyenne
mois_sup_moyenne_boston = [i + 1 for i, valeur in enumerate(boston) if valeur > moyenne_boston]
mois_sup_moyenne_seattle = [i + 1 for i, valeur in enumerate(seattle) if valeur > moyenne_seattle]

# Mois où Boston a eu moins de précipitations que Seattle
mois_boston_inf_seattle = [i + 1 for i, (b, s) in enumerate(zip(boston, seattle)) if b < s]

print(f"Total Boston: {total_boston}, Moyenne Boston: {moyenne_boston}")
print(f"Total Seattle: {total_seattle}, Moyenne Seattle: {moyenne_seattle}")
print(f"Mois > Moyenne Boston: {mois_sup_moyenne_boston}")
print(f"Mois > Moyenne Seattle: {mois_sup_moyenne_seattle}")
print(f"Mois où Boston < Seattle: {mois_boston_inf_seattle}")

# %%
                     #Exercice 3
import numpy as np
from scipy.stats import norm

def test_correlation(X, Y, r0):
    n = len(X)
    correlation = round(np.corrcoef(X, Y)[0, 1], 2)
    Z = round(0.5 * np.log((1 + correlation) / (1 - correlation)), 2)
    Z0 = round(0.5 * np.log((1 + r0) / (1 - r0)), 2)
    T = round((Z - Z0) * np.sqrt(n - 3), 2)
    p_valeur = round(2 * (1 - norm.cdf(abs(T))), 2)
    return correlation, p_valeur

# Exemple de données
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]

# Tests
correlation_0, p_0 = test_correlation(X, Y, 0)
print(f"Corrélation: {correlation_0}, p-valeur pour r0=0: {p_0}")
correlation_6, p_6 = test_correlation(X, Y, 0.6)
print(f"Corrélation: {correlation_6}, p-valeur pour r0=0.6: {p_6}")

#%%
                         #Exercice 4
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
r = 2
a = 0.05
beta = 1
generations = 30
host_pop = [20]
parasitoid_pop = [2]

# Modèle
for t in range(generations):
    H_next = host_pop[-1] * np.exp(-a * parasitoid_pop[-1]) * r
    P_next = host_pop[-1] * (1 - np.exp(-a * parasitoid_pop[-1])) * beta
    host_pop.append(H_next)
    parasitoid_pop.append(P_next)

# Graphique
time = range(generations + 1)
plt.plot(time, host_pop, label="Hôtes")
plt.plot(time, parasitoid_pop, label="Parasitoïdes")
plt.xlabel("Temps (générations)")
plt.ylabel("Population")
plt.legend()
plt.title("Modèle de Nicholson-Bailey")
plt.show()
# %%