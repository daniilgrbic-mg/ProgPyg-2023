# Napredniji `import`, biblioteka `random`

[↩️ Vratiti se na glavnu stranu](../README.md)

## Konstrukcija `import X as Y`

Za sada smo koristili dve biblioteke, `pygame` i `pygamebg`, tako sto smo ih "ukljucivali" na pocetku programa naredbama:

```python
import pygame
import pygamebg
```

Funkcijama i objektima tih biblioteka smo pristuali uz pomoc tacke, na primer:

```python
prozor = pygamebg.open_window(600, 400, "Primer")
```

```python
bela = pygame.Color('white')
pygame.draw.line(prozor, ...)
```

Svaki put smo morali da pisemo pun naziv biblioteke, sto ne bi bilo problem za nesto poput `pygamebg`, jer ga srecemo svega dvaput u svakom programu. Ali zato `pygame.*` napisemo mnogo vise puta, pa imamo i do desetina ponavljanja.

Ukljucivanje biblioteke na sledeci nacin nam pomaze da skratimo zapis funkcija u kodu

```python
import pygame as pg
```

Sada umesto 

```python
bela = pygame.Color('white')
pygame.draw.line(prozor, ...)
```

pisemo:

```python
bela = pg.Color('white')
pg.draw.line(prozor, ...)
```

## Bilioteka `random`

Biblioteka radnom sluzi za odredjivanje slucajnih brojeva, na primer za bacanje kockice. Ova biblioteka ima gomilu funkcija, ali za sada cemo se zadrazti na samo jednoj - funkciji `randint`:

```python
import random as rnd

kockica = rnd.randint(1, 6) 

print(kockica)  # ispisuje bilo koji broj izmedju 1 i 6
```

## Konstrukcija `from X import Y`

Ponekad nije potrebno importovati celu biblioteku, vec samo jedan ili par njenih delova. Primer za to je funkcija `randint`. Potrebna nam je samo ona, a bas nas briga za sve ostalo (a ima puno).

```python
from random import randint

kockica = randint(1, 6)

print(kockica)  # ispisuje bilo koji broj izmedju 1 i 6
```

Kao sto vidimo sada mozemo direktno da koristimo funkciju `randint`, ni ne moramo d anavedemo biblioteku!

