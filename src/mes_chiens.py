from sl29.dog import Dog

# Exemple d'utilisation
my_dog = Dog(race="Berger allemand", sex="M", name="Rintintin")
print(my_dog)

# Accès aux attributs
print(my_dog.race)
print(my_dog.sex)
print(my_dog.name)

# Modification du nom
my_dog.name = "Rex"
print(my_dog.name)

# Tentative de modification de la race ou du sexe (générera une erreur)
my_dog.race = "Labrador"  # Erreur: AttributeError