# RoboCar project P1A 2021

Robotické auto by mělo zvládat "semi-autonomní" řízení. Po *bílé* nebo *černé* čáře se bude pohybovat převážně samostatně, ideálně bez nutnosti zásahů do řízení.

Je vhodné si pomoci zasíláním "instrukcí" prostřednictvím aplikace [**Mbit**](https://play.google.com/store/apps/details?id=com.yahboom.mbit&hl=cs&gl=US) z Google Play nebo App Store.

- Pro splnění algoritmické úlohy nesmí vozidlo opustit svým obrysem vytyčenou čáru. 
- Druhým faktorem hodnocení je čas potřebný na úspěšné zdolání tratě. 
- Počet nutných korekcí (manuálních zásahů do řízení) také ovlivní výsledek.
- Čitelnost a dekompozice kódu **je** předmětem hodnocení

## Požadavky na schopnosti vozidla

- [x] autonomní jízda po bílé / černé čáře bez nutných zásahů do řízení
- [ ] překonání křižovatek ve tvaru písmene **+**
- [ ] schopnost na "vyžádání" odbočit na křižovatce vlevo nebo vpravo
- [ ] možnost obrátit se do protisměru

### Volitelně (bonusové hodnocení)

- [ ] schopnost najet do křižovatky jiného tvaru než **+**, typicky **Y**
- [ ] čára končící u mechanické překážky = otočení se do protisměru
- [ ] čára končící mechanickou překážkou = pokus o objetí a pokračování v autonomní jízdě
(překážka nebude nikdy větší jak 20 × 20 × 20 cm)

## Omezení v hodnocení práce
Algoritmicky totožná řešení napříč skupinami budou snižovat procento maximálního hodnocení. A to o 10 % za každý duplicitní výskyt.
Například pokud u 3 vozidel bude signifikantní část funkcionality totožná, odečítá se 30 % (z maxima) od celkového hodnocení.

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>


> Open this page at [https://lukypop.github.io/pxt-robocar-mertovic_x_popovic/](https://lukypop.github.io/pxt-robocar-mertovic_x_popovic/)

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/lukypop/pxt-robocar-mertovic_x_popovic** and import

## Edit this project ![Build status badge](https://github.com/lukypop/pxt-robocar-mertovic_x_popovic/workflows/MakeCode/badge.svg)

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/lukypop/pxt-robocar-mertovic_x_popovic** and click import

## Blocks preview

This image shows the blocks code from the last commit in master.
This image may take a few minutes to refresh.

![A rendered view of the blocks](https://github.com/lukypop/pxt-robocar-mertovic_x_popovic/raw/master/.github/makecode/blocks.png)

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
