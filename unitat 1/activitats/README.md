# Activitats Unitat 1 - Introducció a Python
Activitats de Python de la primera unitat
---

## Activitat 8
Fes una aplicació que imprimisca els primers 100 números imparells.

## Activitat 9
Fes una aplicació que donada la següent llista, imprimisca els seus membres: aficions = ['esports', 'cine', 'teatre']

## Activitat 10
Definix una llista i utilitzant filter, que la separe en dues llistes, una amb els elements parells i l'altra amb els senars.

## Activitat 11
Crea una aplicació que vaja llegint operacions d'un fitxer "operacions.txt" (una operació per línia). Per exemple: 4 + 4

Haurà de guardar els resultats en un altre arxiu "resultats.txt". Per exemple: 4 + 4 = 8

Utilitza funcions anònimes per a implementar les operacions.

## Activitat 12
Modifica el codi de l'activitat 11 per a que no es produïsquen errors en l'execució, ja siga per introdïur valor no definits per a les funcions, valors que no són numèrics o operacions desconegudes. Controla també que no es produïsquen errors en la lectura/escriptura dels arxius.

## Activitat 13
Anem a implementar un xicotet joc per consola. El programa generarà un número aleatori entre 0 i 100 (utilitzeu randint() del mòdul random) i demanarà a l'usuari que introduïsca un número.

Mentre el número siga massa menut, llançarà una excepció ErrorEnterMassaMenut indicant-li-ho. Si per contra és massa gran llançarà ErrorEnterMassaGran.

Si s'introdueix un valor no numèric, es llançarà una excepció de tipus ErrorNoEsEnter.

El joc acabarà quan s'introduïsca l'enter buscat, felicitant a l'usuari.

## Activitat 14
Defineix una jerarquia de figures amb les classes Figura, Cercle, Triangle, Rectangle i Quadrat.

- La clase Figura tindrá dos métodes abstractes area i perimetre, que implementarán la resta de classes. La classe figura serà el que s'anomena una interfície informal, ja que tots els seus mètodes són abstractes. Per a definir que són abstractes, simplement utilitzeu la instrucció pass al bloc de la funció.

```py
def area() -> int:
    """Torna l'àrea d'una Figura"""
    pass
```

- El Cercle rebrá el radi com a argument al seu constructor, el Triangle el costat i el Rectangle la base i l'altura.
- Cercle, Triangle i Rectangle heredarán de Figura directament.
Quadrat heredará de Rectangle, però al constructor sols rebrá un argument, el costat.
- Crea un objecte de cada tipus i imprimeix les seues característiques.