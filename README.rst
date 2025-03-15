sl29.dog
========

Un projet pour enseigner la Programmation Orientée Objet (POO) en Python avec une classe `Dog`.

.. image:: https://upload.wikimedia.org/wikipedia/en/5/53/Scooby-Doo.png
   :alt: Scooby-Doo
   :width: 200
   :align: center

Description
-----------

Ce projet implémente une classe `Dog` qui représente un chien. La classe inclut des fonctionnalités telles que :

- La gestion des attributs d'un chien (race, sexe, nom).
- Des méthodes pour simuler des comportements comme aboyer (`bark`) ou mâcher (`chew`).
- Une méthode `mate` pour simuler l'accouplement entre deux chiens et produire un chiot.

Installation
------------

Pour installer le projet, utilisez la commande suivante :

.. code-block:: bash

   pip install .

Installation(dev)
-----------------

Pour installer le projet en mode développeur :

.. code-block:: bash


   pip install . -e[dev]


Cas d'usage
-----------

Voici quelques exemples d'utilisation de la classe `Dog` :

1. **Création d'un chien** :

   .. code-block:: python

      from sl29.dog import Dog

      rintintin = Dog(race="Berger allemand", sex="M", name="Rintintin")
      print(rintintin)  # Output: Chien: Rintintin, Race: Berger allemand, Sexe: M

2. **Faire aboyer un chien** :

   .. code-block:: python

      print(rintintin.bark(3))  # Output: WoffWoffWoff

3. **Faire mâcher un objet** :

   .. code-block:: python

      print(rintintin.chew("os"))  # Output: o

4. **Accouplement de deux chiens** :

   .. code-block:: python

      laika = Dog(race="bâtard", sex="F", name="Laïka")
      puppy = rintintin.mate(laika)
      print(puppy)  # Output: Chien: , Race: bâtard, Sexe: M ou F (aléatoire)

5. **Gestion des erreurs lors de l'accouplement** :

   .. code-block:: python

      scoobydoo = Dog(race="Grand danois", sex="M", name="Scooby-Doo")
      try:
          rintintin.mate(scoobydoo)  # Les deux chiens sont de même sexe
      except MatingError as e:
          print(e)  # Output: Les deux chiens sont de même sexe. L'accouplement est impossible.

Documentation
-------------

Pour générer la documentation, utilisez Sphinx :

.. code-block:: bash


   pip install . -e[doc]


.. code-block:: bash

   sphinx-build doc/source doc/build

La documentation sera générée dans le dossier `doc/build`.


Tests unitaires
---------------

Pour lancer les tests :

.. code-block:: bash


   pip install . -e[test]


.. code-block:: bash

   pytest --cov=sl29.dog tests/

ou pour avoir un rapport détaillé au format html

.. code-block:: bash

   pytest --cov=sl29.dog --cov-report=html tests/




