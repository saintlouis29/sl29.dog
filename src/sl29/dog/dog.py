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
        _race (str): La race du chien.
        _sex (str): Le sexe du chien ('M' ou 'F').
        name (str): Le nom du chien.
    """

    def __init__(self, race: str, sex: str, name: str = "") -> None:
        """
        Initialise un chien avec une race, un sexe et un nom.

        Args:
            race (str): La race du chien.
            sex (str): Le sexe du chien ('M' ou 'F').
            name (str, optional): Le nom du chien. Par défaut, une chaîne vide.
        """
        self._race = race
        self._sex = sex
        self.name = name
        self._mother = None
        self._father = None
        self._puppies = []

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
        Retourne le sex du chien.

        Returns:
            str: Le sex du chien.
        """
        return self._sex

    class MatingError(Exception):
        pass

    @property
    def mother(self) -> Optional['Dog']:
        """Retourne la mère du chien ou None."""
        return self._mother

    @property
    def father(self) -> Optional['Dog']:
        """Retourne le père du chien ou None."""
        return self._father

    @property
    def puppies(self) -> list:
        """Retourne la liste des chiots."""
        return self._puppies

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
        if self._sex == other._sex:
            raise MatingError("Les chiens ne peuvent pas s'accoupler car ils sont du même sexe.")
        
        race = self._race if self._race == other._race else "bâtard"
        
        sex = random.choice(['M', 'F'])
        
        # Créer le chiot
        puppy = Dog(race=race, sex=sex)
        puppy.name = "" 
        puppy._mother = self if self._sex == 'F' else other
        puppy._father = self if self._sex == 'M' else other

    
        self._puppies.append(puppy)
        other._puppies.append(puppy)

        return puppy

    def __str__(self) -> str:
        """
        DOCSTRINGS A COMPLETER
        """
        return f"Chien: {self.name}, Race: {self._race}, Sexe: {self._sex}"

    def bark(self, n: int = 1) -> str:
        return "Woff" * n

    def chew(self, stuff: str) -> str:
        """Retire la dernière lettre d'une chaîne de caractères.
        
        Args:
            stuff (str): La chaîne à modifier.
            
        Returns:
            str: La chaîne sans sa dernière lettre.
        """
        if len(stuff) > 0:
            return stuff[:-1]
        return stuff

if __name__ == "__main__":
    pass


