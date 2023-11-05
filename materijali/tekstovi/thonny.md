# Thonny - Python IDE za pocetnike

[↩️ Vratiti se na glavnu stranu](../README.md)

**IDE** je skracenica **Integrated Development Environment** (razvojno okruzenje), a ako prevedemo na ljudski jezik - program za pisanje programa 🙂

## Skidanje Thonny-ja (1/5)

Sa sajta [thonny.org](https://thonny.org/) skinite **Portable variant 64-bit** kao sto je prikazano na slikama:

![](slike/thonny/download_1.png)
![](slike/thonny/download_2.png)
![](slike/thonny/download_3.png)

Ovim ste skinuli portabilnu verziju ovog programa. Sta to znaci? TO znaci da nije potrebno nista da instalirate, vec mozete samo da ga pokrenete.

## Instalacija (2/5)

Posto ste skinuli folder u **ZIP** formatu, da biste mogli da ga koristite, potrebno ga je "raspakovati" (extract). Pratite uputstva sa slika:

![](slike/thonny/extract_1.png)
![](slike/thonny/extract_2.png)

Nakon sto ste usli u *Downloads* datoteku/folder, kliknite desnim klikom na zip koj ste upravo skinuli sa sajta, i dobicete brdo opcija:

![](slike/thonny/extract_3.png)
![](slike/thonny/extract_4.png)
![](slike/thonny/extract_5.png)

To je to! Sada imate folder u kome se nalazi Thonny i Python, i spremni ste da pisete programe!

Moj savet je da prevucete taj folder na neko drugo mesto, na primer na **Desktop** kako se ne bi zagubio kada budete skidali nove stvari, ali nista ne fali da ostane tu gde jeste.

![](slike/thonny/move_to_desktop.png)
![](slike/thonny/open_folder.png)

## Pokretanje Thonny-ja (3/5)

Unutar foldera cete naci **Thonny.exe**, duplim klikom na to pokrecete sam program. Prvi put ce vas pitati za jezik, samo kliknite **"Let's go!"** i terajte dalje.

![](slike/thonny/run_thonny.png)
![](slike/thonny/intitial_setup.png)
![](slike/thonny/thonny.png)

## Instalacija biblioteka Pygame i Pygamebg (4/5)

Sledeci (predposlednji) korak jeste da insatlirate biblioteke Pygame i Pygamebg. 

Najpre je potrebno da izaberete **Tools** dugme na gornjoj strani prozora, i tu kliknete na **Manage Packages**. Iskocice prozor za instalaciju biblioteka za Python.

![](slike/thonny/tools.png)

U pretrazi pri vrhu novog prozora, ukucajte Pygame, i stisnite **Enter** (ili klinkite dugme pored, **Search on PyPl**):

![](slike/thonny/manage_packages.png)

U skeciji **Search results** stisnite **pygame**, i dole **install**.

![](slike/thonny/install_pygame_1.png)
![](slike/thonny/install_pygame_2.png)

Nakon toga treba da vidite sledece, sto znaci da ste uspesno instalurali Pygame:

![](slike/thonny/install_pygame_3.png)

Isti proces ponovite i za **Pygamebg**. Kada zavrsite, mozete da testirate biblioteke tako sto ukucate 

```python
import pygame
import pygamebg
```

u gornji prozor, i stisnite **zeleno** dugme (run). Ukoliko se nista ne crveni, i ako dole ispise poruku "Hello from the pygame community", znaci da ste sve uradili kako treba! 

![](slike/thonny/test_pygame.png)

## Namestanje automplete (5/5)

Poslednji korak nije obavezan, ali ce vam **olaksati zivot**. Zelimo da ukljucimo autocmplete, da vam Thonny pomaze dok kucate vase kodove.

Prattie uputstva sa slika, i u **Tools -> Options -> Editor Tab** upalite sve naznacene opcije, i stisnite **OK**:

![](slike/thonny/options.png)
![](slike/thonny/editor_tab_1.png)
![](slike/thonny/editor_tab_2.png)

Sada kada budete nesto kucali, Thonny ce prikazivate koje opcije imate:

![](slike/thonny/autocomplete.png)

[↩️ Vratiti se na glavnu stranu](../README.md)
