# TP 2 Automatique
# Méthode de Strejc
from scipy import signal
import matplotlib.pyplot as plt
import control.matlab as cm
import numpy as np

# Initialisation des valeurs dénominateur et numérateur
num = np.array([100])
den = np.array([1, 10, 29, 20])
# Definition du système H(p)
systeme = (num, den)
print(f"Le système est : {systeme}")
# Definition du système avec control.matlab
H = cm.tf(num, den)
print(f"Le système linéaire = {H}")
# Defintion de la réponse impulsionnelle de notre système
Yout, T = signal.impulse(systeme)
# Représentation d'un filtre linéaire ?
z, p, k = cm.tf2zpk(num, den)
# Definition de la réponse impulsionnelle de notre filtre
Pout, P = signal.impulse(p)
# Réponse indicielle du système
Sout, S = cm.step(H)

print(f"Les zeros sont : {z}")
print(f"Les poles sont : {p}")
print(f"Le gain du système est : {k}")

# Le graphe de la réponse impulsionnelle de notre système
# plt.figure(1)
# plt.title("La réponse impulsionnelle de notre système")
# plt.plot(Yout.T, T.T)
# plt.grid(True)
# # Le graphe de la réponse impulsionnelle de notre filtre
# plt.figure(2)
# plt.title("La réponse impulsionnelle de notre filtre")
# plt.plot(Pout, P)
# plt.grid(True)
# # Les pôles de notre système
# plt.figure(3)
# # plt.title("Les pôles de notre système")
# plt.polar(p)
# # Réponse indicielle du système
# plt.figure(4)
# plt.title("Réponse indicielle du système")
# plt.plot(S, Sout)
# plt.grid(True)
# plt.show()

# Calcul de la dérivée de la réponse indicielle (réponse impulsionnelle)
# Cela nous donnera la pente de la tangente au point d'inflexion
dy_dt = np.diff(Sout) / np.diff(S)

# Trouver l'indice du point d'inflexion (où la dérivée est maximale)
index_of_inflexion_point = np.argmax(dy_dt)

# Coordonnées du point d'inflexion
inflexion_point_x = S[index_of_inflexion_point]
inflexion_point_y = Sout[index_of_inflexion_point]

# Pente de la tangente au point d'inflexion
tangent_slope = dy_dt[index_of_inflexion_point]

# Équation de la tangente
# y = f'(x)(x - a) + f(a)
# où a est le point d'inflexion (inflexion_point_x, inflexion_point_y)
tangent_intercept = inflexion_point_y - tangent_slope * inflexion_point_x

# # Calcul des valeurs de Strejc
# n = len(den) - 1
# tau = inflexion_point_x
# r = 1  # On peut choisir r de manière arbitraire

# Calcul de T(p) avec les valeurs de Strejc trouvées
# T_p = num[0] * np.exp(-r * S) / (1 + tau * S)**n


# Affichage des valeurs de Strejc
# print("Les valeurs de Strejc sont :")
# print("n =", n)
# print("τ =", tau)
# print("r =", r)

print("Coordonnées du point d'inflexion de la tangente par rapport à la réponse indicielle :")
print("x =", inflexion_point_x)
print("y =", inflexion_point_y)

# Calculate X value where Y = 5 on the tangent line
x_val_for_y_5 = (5 - tangent_intercept) / tangent_slope

# Calculate X value where Y = 5 on the tangent line
x_val_for_y_0 = (0 - tangent_intercept) / tangent_slope

# Ta
Ta = x_val_for_y_5 - x_val_for_y_0
# Tu
Tu = x_val_for_y_0 - 0
# Calcul du rapport
rapport = Tu / Ta
# Afficher Tu, Ta et le rapport
print(f"Tu = {Tu}  \t Ta = {Ta} \t Rapport = {rapport}")
print(f"donc n = 2 \t Ta / τ = 2.7183")
# Calcul de τ
Tadivτ = 2.7183
τ = Ta / Tadivτ
# Afficher τ
print(f"τ = {τ}")
# Calcul du retard
Tudivτ = 0.2817
Tuprime = Tudivτ * τ
# Afficher Tu'
print(f"Tu' = {Tuprime}")
# Calcul et affichage du retard r
r = Tu - Tuprime
print(f"Le retard est donc de : r = Tu - Tu' = {r}")

# Affichage de la réponse indicielle et de la tangente au point d'inflexion
# plt.plot(S, Sout, label='Réponse indicielle')
# plt.plot(S, tangent_slope * S + tangent_intercept, '--', label='Tangente au point d\'inflexion')
# plt.plot(inflexion_point_x, inflexion_point_y, 'o')
# plt.plot(x_val_for_y_5, 0, 'ro')
# plt.plot(x_val_for_y_0, 0, 'ro')
# # Plot Tu et Ta
# plt.plot([0, x_val_for_y_0], [1, 1], color='g', linestyle='-', label='Tu')
# plt.plot([x_val_for_y_0, x_val_for_y_5], [1, 1], color='b', linestyle='-', label='Ta')
# # Plot les limites de Tu et Ta
# plt.plot([x_val_for_y_5, x_val_for_y_5], [0, 1.2], color='black', linestyle='--')
# plt.plot([x_val_for_y_0, x_val_for_y_0], [0, 1.2], color='black', linestyle='--')
# plt.ylim(0, 5.1)
# plt.title('Réponse indicielle avec tangente au point d\'inflexion')
# plt.xlabel('Temps')
# plt.ylabel('Réponse')
# plt.xlim(0)
# plt.ylim(0)
# plt.legend()
# plt.grid(True)
# plt.show()


# Méthode de Broida
print("==================")
print("Méthode de Broida")
print("==================")
# Calcul de la valeur finale de la réponse indicielle
S_infini = Sout[-1]

# Calcul de T1
# Trouver l'indice où la réponse indicielle atteint 28% de sa valeur finale
index_t1 = np.argmax(Sout >= 0.28 * S_infini)

# Temps t1 où la réponse indicielle atteint 28% de sa valeur finale
t1 = S[index_t1]

print("Temps t1 où la réponse indicielle atteint 28 % de sa valeur finale:", t1)

# Calcul de T2
# Trouver l'indice où la réponse indicielle atteint 40% de sa valeur finale
index_t2 = np.argmax(Sout >= 0.4 * S_infini)

# Temps t2 où la réponse indicielle atteint 40% de sa valeur finale
t2 = S[index_t2]

print("Temps t2 où la réponse indicielle atteint 40 % de sa valeur finale:", t2)

# Calcul de τ par la méthode de Broida
τBroida = 5.5 * (t2 - t1)
# Calcul de r par la méthode de Broida
rBroida = 2.8 * t1 - 1.8 * t2

print(f"τBroida = {τBroida} \t rBroida = {rBroida}")

plt.title("Réponse indicielle du système")
plt.plot(S, Sout)
plt.plot(t1, Sout[index_t1], 'ro')
plt.plot(t2, Sout[index_t2], 'go')
plt.show()


# Méthode de Ziegler Nichols
print("==================")
print("Méthode de Ziegler Nichols")
# Hello world
# ZID
print("==================")

