# Plezalni vzponi v Sloveniji

Analiziral bom plezalske vzpone v slovenskih plezališčih iz spletne strani [8a.nu](https://www.8a.nu).
## Zajemanje podatkov
Javascript na strani 8a.nu/ascents glede na zahtevane parametre vrne urejen JSON zadnjih 10.000 vzponov v Sloveniji. Žal to ni dovolj za dobro analizo, saj podatki ne sežejo dlje od leta 2018. Zato sem podatke dobil na nasilen način.

### Zajete spletne strani in [regex](https://en.wikipedia.org/wiki/Inferno_(Dante)#Ninth_Circle_(Treachery))

- [Seznam plezališč](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/data/plezalisca.json) sem pridobil s funkcijama [`vsa_slovenska_plezalisca_in_balvanisca()`](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/src/nalozi_podatke.py#L13) in [`strik_v_json`](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/src/parse_plezalisca.py#L13).
- Za vsako plezališče sem pridobil [html datoteko](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/data/vzponi_bohinjska-bela.html) z uporabo funkcije [`vsi_vzponi_v_plezaliscih()`](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/src/nalozi_podatke.py#L34) in izluščil podatke s pomočjo demonov, ki jih prikliče [`vzponi_strik_v_json_csv()`](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/src/parse_plezalisca.py#L72).

~~Urejeni podatki so shranjeni v datoteki [vzponi_strik.csv](https://github.com/urhprimozic/plezalni-vzponi-v-sloveniji/blob/main/data/vzponi_strik.csv).~~

Urejeni podatki so shranjeni v .json in v spondjih tabelah:
- vzponi.csv - vsi vzponi in vsi podatki (plezalec, plezalisce, datum, ...)
- plezalci.csv - plezalci, uporabniška imena in id
- plezalisca.csv
- smeri.csv


## Delovne hipoteze TODO
- Ob delovnih dneh je vzponov občutno manj
- Ob delovnih dneh se več pleza v lokalnih plezališčih (imajo malo vzponov na sploh), kot pa v popularnih (veliko vzponov).
- Ali obstaja povezava med številom vzponov na pogled (=v prvo) in posameznim plezališčem? 
(V miški je lažje sajtaj kot v Dovžanki..?)
- Ali obstaja povezava med razliko (*plezalčeva povprečna ocena - plezalčeva popvrečna ocena v določenem plezališču*) in plezališčem? 
(V glencah so že 6cji težki)
- Ali obstaja korelacija med dolžino komentarja in krajen uporabnika? 
(Ljubljančani filozofirajo).
