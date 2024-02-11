# ProgPyg-2023

```python
Nastava se odvija nedeljom u 9 casova, u ucionici 311 (gornji sprat)
```
```python
Termini nastave u drugom semestru:
    28. Januar
    11, 25. Februar
    3, 10, 17, 31. Mart
    7, 14. April
```

## Materijali

<!-- > Prvi cas posle raspusta - obnavljanje:  
> [Petlja zbirka iz Pygame](https://petlja.org/biblioteka/r/lekcije/pygame-prirucnik/crtanje-cas1) -->

### Dogadjaji - `event_loop`
- [Semafor pisan an casu](/materijali/dogadjaji/primer.py)
- [Semafor - lepsa verzija](/materijali/dogadjaji/semafor.py)
- [Matrice u Python-u](/materijali/dogadjaji/matrice.py)
- [Lavirint bez grafike, samo konzolni ispis](/materijali/dogadjaji/lavirint.py)

### Kretanje vise objekata, razlike vektora, funkcije `normalize` i `length`
- [Jedan protivnik juri igraca](/materijali/vise_objekata/jurenje.py)
- [Vise protivnika jure igraca](/materijali/vise_objekata/jurenje_vise.py)

### Kolizije - preseci tacaka i pravougaonika, ili vise pravougaonika
- [Detekcija preklapanja **tacke i pravougaonika**, funkcija `collidepoint`](/materijali/kolizije/rect_i_tacka.py)
- [Detekcija preseka **dva pravougaonika**](/materijali/kolizije/dva_pravougaonika.py)

### Korisnicka interakcija - dohvatanje stanja tastature i misa
- [Dohvatanje stanja tastature - promena pozicije lopte na strelice](/materijali/interaktivni_programi/kretanje_strelicama.py)
- [Powering up bar](/materijali/interaktivni_programi/powering_up.py) (radi na dugme *space*, [ovako nesto ali bez novcica](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fassets.hongkiat.com%2Fuploads%2Fanimated-progress-bar%2F13.gif%3Fnewedit%3Fnewedit&f=1&nofb=1&ipt=6b247fbe5d9e9f09b3ae6c041bc48b6f2d5ad3eae5992a17676dbfa09afa520a&ipo=images))
- [Kretanje u svemiru](/materijali/interaktivni_programi/kretanje_u_svemiru.py) (u ovoj varijanti na strelice menjamo brzinu tela, a ne poziciju)
- [Dohvatanje pozicije misa](/materijali/interaktivni_programi/pozicija_misa.py)

### Ucitavanje slika i animacije promenom slika
- Funkcije `pg.image.load` i `blit`
- Primer: [Samuraj u napadu](/materijali/ucitavanje_slika/samurai_napada.py)

### Animacije - kretanje objekata i promene slika, ali bez korisnicke interakcije
- Funkcija `update`, [novi skelet programa](/materijali/animacije/skelet_frame.py)
- Obicno kretanje i odbijanje od zidova
  - [Odbijanje lopte (levo-desno)](/materijali/animacije/odbijanje_lopte_levo_desno.py)
  - [Odbijanje lopte (4 zida)](/materijali/animacije/odbijanje_lopte_4_zida.py)
- Vektori: sabiranje i rotacija
  - [Suncev sistem: kretanje planete oko Sunca](/materijali/animacije/planeta.py)

### Osnove iscrtavanja
- Tekst: [uvod u Pygame](/materijali/osnovno_iscrtavanje/pygame_uvod.md)
- [RGB sistem boja (Petlja)](https://petlja.org/kurs/352/3/6074)
- [Osnovni "skelet" programa - deo programa koji je uvek isti](/materijali/osnovno_iscrtavanje/skelet_uvod.py)
- Primeri: 
  - [Crtanje trougla](/materijali/osnovno_iscrtavanje/trougao.py)
  - [Crtanje sume (vise jelki na raznim pozicijama)](/materijali/osnovno_iscrtavanje/suma.py)

<!--
## Materijali 
- [ ] 17. Decembar - kolizije
  - [Bojimo prvougaonik kad ga sece mis](materijali/kodovi/kolizije.py)
- [ ] 10. Decembar - rad sa tastaturom
  - [Upravljanje loptom na ekranu](materijali/kodovi/tastatura.py)
  - [Spisak kodova za tastere](https://www.pygame.org/docs/ref/key.html)
  - [Dohvatanje poziicje misa](materijali/kodovi/mis.py)
- [x] 3. Decembar - nastavak proslog casa
- [x] 26. Novembar - ucitavanje i prikazivanje slika (sprite-ova)
  - [Iscrtavanje spriteova (tezi nacin)](materijali/kodovi/sprite.py)
  - [Iscrtavanje spriteova (laksi nacin, sa listom)](materijali/kodovi/sprite2.py)
  - [Slike samuraj](materijali/kodovi/Samurai/), [slike shinobi](materijali/kodovi/Shinobi/)
  - [LibreSprite](https://libresprite.github.io/)
- [x] 19. Novembar - uvod u animacije, kretanje - vezbanje
  - [Zadaci sa resenjima](materijali/zadaci/05_05_nov.md)
- [x] 5. Novembar - **pisanje funkcija** u Python-u, uvod u animacije, **simulacija kretanja**
  - Funkcije u matematici i programiranju:
    - [Primeri funkcija: apsolutna vrednost, povrsina pravougaonika, maksimum dva broja](materijali/kodovi/funkcije_primeri.py)
    - [Globalni i lokalni opseg promeljivih, komanda `global`](materijali/kodovi/global_primer.py)
    - [Funkcija za crtanje jelke i sume jelki](materijali/kodovi/suma.py)
  - [Struktura Pygame koda za dinamicke programe](materijali/kodovi/skelet_frame.py)
    - [Primer: animacija planete](materijali/kodovi/planeta.py)
- [x] 29. Oktobar - ugdjezdene petlje, *vezbanje*
  - [Zadaci sa resenjima](materijali/zadaci/04_29_okt.md)
- [x] 22. Oktobar - **grananje** (`if..else`), **petlje** (`for`, `while`)
  - [Zadaci sa resenjima](materijali/zadaci/03_22_okt.md)
- [x] 8. Oktobar - crtanje kompleksnijih oblika, *vezbanje*
  - [Zadaci sa resenjima](materijali/zadaci/02_08_okt.md)
- [x] 1. Oktobar - uvodni cas, koordinatni sistem u racunarstvu, crtanje osnovnih oblika
  - [Razvojno okruzenje Thonny](materijali/tekstovi/thonny.md)
  - [RGB sistem boja (Petlja)](https://petlja.org/kurs/352/3/6074)
  - [Uvod u Pygame](materijali/tekstovi/pygame_uvod.md)
  - [Struktura Pygame programa](materijali/kodovi/skelet_uvod.py)
  - [Domaci zadatak: cica glisa](materijali/domaci/01_01_okt.md)
-->

<!-- ## Plan rada
Tempo cemo prilagoditi nasim potrebama, nista iz gore navedenog nije zakon, samo okviran plan.
- [x] [Instalacija okruzenja Thonny i potrebnih biblioteka](materijali/tekstovi/thonny.md)
- [x] *Uvod u Python, promenljive, osnovni tipovi*
- [x] Uvod u 2D grafiku, FPS, pikseli, [RGB boje](https://petlja.org/kurs/352/3/6074)
- [x] Koriscenje biblioteke Pygame, `wait_loop`, [skelet za kodove](materijali/kodovi/skelet_uvod.py)
- [x] [Crtanje osnovnih oblika: boje, koordinate, duzi, pravougaonici, krugovi](materijali/tekstovi/pygame_uvod.md)
- [x] [*Liste i torke u Python-u*](materijali/kodovi/lista.py)
- [x] Crtanje osnovnih oblika: [mnogouglovi](materijali/kodovi/trougao.py)
- [x] *Logika u Python-u: `if...else` naredba, bool vrednosti*
- [x] [*Petlje u Python-u: `for` i `while`*](materijali/kodovi/petlje.py)
- [x] Crtanje pravilnih oblika uz pomoc petlji
- [ ] Ugnjezdene petlje (petlje u vise nivoa)
- [ ] [Napredniji `import`; biblioteka `random`](materijali/tekstovi/importovi.md)
- [ ] *Pisanje funkcija u Python-u, globalne i lokalne promenljive*
- [ ] Animacije, simulacije kretanja, `frame_loop`
- [ ] Ucitavanje i prikazivanje slika, transformacije slika, alat LibreSprite
- [ ] Vektori u 2D, sabiranje i oduzmianje vektora, rotacija
- [ ] Fizicke simulacije: ubrzano kretanje, kosi hitac
- [ ] Programiranje rekacije programa na koriscenje misa i tastature 
- [ ] *Recnici (mape) u Python-u, kljucevi, pristup po kljucu*
- [ ] Dogadjaji, `event_loop`
- [ ] Kolizije, hitbox, malo geometrije
- [ ] Prikazivanje teksta, fontovi, aliasing
- [ ] ...
- [ ] Veliki projekat na kraju kursa -->
