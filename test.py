line1 = """4,60
(11 commentaires)
·
Cannes, Provence-Alpes-Côte d'Azur, France
Partager
Enregistrer
"""

line2 = """4,84
(104 commentaires)
·
󰀃
Superhost
·
Plérin, Bretagne, France
Partager
Enregistrer
"""
line1 = line1.replace("\n", " ")
line2 = line2.replace("\n", " ")
print(line1.split('·')[-1].replace(" Partager Enregistrer", ''))
print(line2.split('·')[-1].replace(" Partager Enregistrer", ''))