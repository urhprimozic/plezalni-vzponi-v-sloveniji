# Plezalni vzponi v Sloveniji

Analiziral bom plezalske vzpone v slovenskih plezališčih iz spletne strani [8a.nu](https://www.8a.nu).


[Analiza (link)](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/analiza.ipynb)

## Zajemanje podatkov
Javascript na strani 8a.nu/ascents glede na zahtevane parametre vrne urejen JSON zadnjih 10.000 vzponov v Sloveniji. Žal to ni dovolj za dobro analizo, saj podatki ne sežejo dlje od leta 2018. Zato sem podatke dobil na silo.

Vse uporabljene skripte so v mapi `src`. 
- `nalozi_podatke.py` — nalaganje surovih datotek iz 8a.nu
- `orodja.py` 
- `parse_plezalisca.py` — priprava tabel
### Zajete spletne strani:

- [Seznam plezališč](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/data/plezalisca.json) sem pridobil s funkcijama [`vsa_slovenska_plezalisca_in_balvanisca()`](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/src/nalozi_podatke.py#L13) in [`strik_v_json`](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/src/parse_plezalisca.py#L13).
- Za vsako plezališče sem pridobil [html datoteko](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/data/vzponi_bohinjska-bela.html) z uporabo funkcije [`vsi_vzponi_v_plezaliscih()`](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/src/nalozi_podatke.py#L34) in izluščil podatke s pomočjo demonov, ki jih prikliče [`vzponi_strik_v_json_csv()`](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/src/parse_plezalisca.py#L72).

Urejeni podatki so shranjeni v tabelah v mapi `data`:
- `vzponi.csv`
- `plezalci.csv `
- `plezalisca.csv`
- `smeri.csv `

Nekateri izračunani rezultati so shranjeni v mapi `memo` zavoljo hitrejšega delovanja.
## [Analiza](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/analiza.ipynb)
- Velikosti plezališč
- Najbolj obiskana plezališča in največkra preplezane mseri
- Pisci najdaljših komentarjev
- Najtežje smei in plezališča v sloveniji
- Primernost plezališč za trening
- Formula za določanje cene smerem
- Katera plezališča so soft
- Časovna obremenjenost plezališč
- Odvisnost števila vzponov od ocene smeri