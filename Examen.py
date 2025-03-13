# %%
        #EXo 1
import csv
import matplotlib.pyplot as plt

                            #Lecture du fichier CSV
def lire_csv(ebola_guinea):
    
                    #Lit un fichier CSV et retourne une liste de dictionnaires.
    donnees = []
    with open(ebola_guinea, mode='r', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier, delimiter=',')
        for ligne in lecteur:
                     # Conversion des nombres en entiers
            ligne['Cas'] = int(ligne['Cas'])
            ligne['Dèces'] = int(ligne['Dèces'])
            donnees.append(ligne)
    return donnees

                                #Calculs statistiques
def calculer_statistiques(donnees):

                #Calcule les totaux et taux de mortalité par préfecture.
                #Retourne un dictionnaire {préfecture: {cas, deces, taux}}.

    stats = {}
    for entree in donnees:
        pref = entree['Préfecture']
        if pref not in stats:
            stats[pref] = {'cas': 0, 'deces': 0}
        stats[pref]['cas'] += entree['Cas']
        stats[pref]['deces'] += entree['Dèces']
    
                        # Calcul du taux de mortalité
    for pref in stats:
        cas = stats[pref]['cas']
        deces = stats[pref]['deces']
        stats[pref]['taux'] = deces / cas if cas > 0 else 0.0
    return stats

                        #Visualisation
def visualiser_donnees(stats):
  
                #Génère deux diagrammes à barres : cas totaux et taux de mortalité.
   
    prefectures = list(stats.keys())
    cas = [stats[pref]['cas'] for pref in prefectures]
    taux = [stats[pref]['taux'] for pref in prefectures]

                        # Diagramme des cas
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, cas, color='skyblue')
    plt.title('Nombre total de cas par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Cas')

                        # Diagramme du taux de mortalité
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, taux, color='salmon')
    plt.title('Taux de mortalité par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Taux (Décès/Cas)')
    plt.ylim(0, 1)  
            # Limite pour une meilleure lisibilité
    plt.show()

                    #Exécution principale
if __name__ == "__main__":
    donnees = lire_csv('ebola_guinea.csv')
    stats = calculer_statistiques(donnees)
    visualiser_donnees(stats)
# %%
            #Exo2
import random

class Personne:
    def __init__(self, nom, sante="saine", proba_infection=0.3):
        self.nom = nom
        self.sante = sante
        self.proba_infection = proba_infection

    def contact(self, autre_personne):
       
        #Simule un contact avec une autre personne.
        #Si l'autre est infectée, possibilité de transmission.
        
        if autre_personne.sante == "infectee" and self.sante == "saine":
            if random.random() < self.proba_infection:
                self.sante = "infectee"

class Population:
    def __init__(self, personnes):
        self.personnes = personnes

    def simuler_jour(self):
    
        #Simule une journée de contacts aléatoires. 
        # Sélection aléatoire de paires de personnes
        for personne in self.personnes:
            if personne.sante == "infectee":
                # Choisir une personne aléatoire à infecter
                autre = random.choice(self.personnes)
                autre.contact(personne)
    
    def statut_epidemie(self):
        
        #Retourne le nombre de personnes dans chaque état.
        
        stats = {"saine": 0, "infectee": 0, "immunisée": 0}
        for p in self.personnes:
            stats[p.sante] += 1
        return stats

# Exemple d'utilisation
if __name__ == "__main__":
    # Créer une population de 10 personnes
    personnes = [Personne(f"Personne_{i}") for i in range(10)]
    # Infecter une personne au hasard
    personnes[0].sante = "infectee"
    population = Population(personnes)

    # Simulation sur 10 jours
    for jour in range(10):
        taille_population = 1000
        population.simuler_jour()
        print(f"Jour {jour + 1}: {population.statut_epidemie()}","/",taille_population)
# %%
