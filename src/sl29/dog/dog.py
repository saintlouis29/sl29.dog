"""Module providing an implementation of a dog"""
from typing import Optional
import random

# Définition de l'exception personnalisée MatingError
class MatingError(Exception):
    """Exception levée lorsque deux chiens de même sexe tentent de s'accoupler."""
    pass

class Dog:
    """
    Une classe représentant un chien.

    Attributes:
        _race (str): La race du chien (privée).
        _sex (str): Le sexe du chien (privé).
        name (str): Le nom du chien (public).
    """

    def __init__(self, race: str, sex: str, name: str = "") -> None:
        """
        Initialise un chien avec une race, un sexe et un nom.

        Args:
            race (str): La race du chien.
            sex (str): Le sexe du chien ('M' ou 'F').
            name (str, optional): Le nom du chien. Par défaut, une chaîne vide.
        """
        self._race = race  # Attribut privé pour la race
        self._sex = sex    # Attribut privé pour le sexe
        self.name = name   # Attribut public pour le nom
        self._mother: Optional['Dog'] = None  # Attribut privé pour la mère
        self._father: Optional['Dog'] = None  # Attribut privé pour le père
        self._puppies: list['Dog'] = []       # Attribut privé pour les chiots

    @property
    def race(self) -> str:
        """
        Retourne la race du chien.

        Returns:
            str: La race du chien.
        """
        return self._race

    @property
    def sex(self) -> str:
        """
        Retourne le sexe du chien.

        Returns:
            str: Le sexe du chien.
        """
        return self._sex

    @property
    def mother(self) -> Optional['Dog']:
        """
        Retourne la mère du chien ou None.

        Returns:
            Optional[Dog]: La mère du chien ou None.
        """
        return self._mother

    @property
    def father(self) -> Optional['Dog']:
        """
        Retourne le père du chien ou None.

        Returns:
            Optional[Dog]: Le père du chien ou None.
        """
        return self._father
    
    @property
    def puppies(self) -> list['Dog']:
        """
        Retourne la liste de ses chiots.

        Returns:
            List[Dog]: La liste des chiots.
        """
        return self._puppies
    
    def __str__(self) -> str:
        """
        Retourne une représentation en chaîne de caractères du chien.

        Returns:
            str: Une chaîne décrivant le chien.
        """
        return f"Chien: {self.name}, Race: {self._race}, Sexe: {self._sex}"
    
    def bark(self, n:int = 1) -> str:
        """
        Retourne la chaine de caractère 'Woff' concaténée n fois
        
        Args:
            n (int, optionnal): Le nombre d'aboiements.
        Returns:
            str: 'Woff' concaténée n fois
        """
        return n*'Woff'

    def chew(self, stuff:str) -> str:
        """
        Retourne la chaîne de caractère stuff sans sa dernière lettre
        
        Args:
            stuff (str): Une chaîne de caractère
        Returns:
            str: la chaine de caractère sans sa dernière lettre
        """
        return stuff[:-1]
    
    def mate(self, other: 'Dog') -> 'Dog':
        """
        Fait s'accoupler deux chiens et retourne un chiot.

        Args:
            other (Dog): L'autre chien avec lequel s'accoupler.

        Returns:
            Dog: Le chiot issu de l'accouplement.

        Raises:
            MatingError: Si les deux chiens sont de même sexe.
        """
        # Vérification des sexes
        if self._sex == other._sex:
            raise MatingError("Les deux chiens sont de même sexe. L'accouplement est impossible.")

        # Détermination du père et de la mère
        if self._sex == 'M':
            father = self
            mother = other
        else:
            father = other
            mother = self

        # Détermination de la race du chiot
        if father.race == mother.race:
            puppy_race = father.race
        else:
            puppy_race = "bâtard"

        # Détermination du sexe du chiot (aléatoire)
        puppy_sex = random.choice(['M', 'F'])

        # Création du chiot
        puppy = Dog(race=puppy_race, sex=puppy_sex, name="")

        # Assignation des parents
        puppy._father = father
        puppy._mother = mother

        # Ajout du chiot à la liste des chiots des parents
        father._puppies.append(puppy)
        mother._puppies.append(puppy)

        return puppy
