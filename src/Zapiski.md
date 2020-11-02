_Mogoče to zbrišem pred finalno verzijo?_

## Opazki pri vlečenju podatkov

- Navidezna stran je [tole](https://www.8a.nu/ascents), vendar v resnici vlečeš JSON iz 	
https://www.8a.nu/api/follows/global?pageIndex=0&pageSize=20&countrySlug=slovenia

- pageSIze=10000 ga še ne sesuje
- ne morem dobiti več kot 10 000 zadnjih vzponov v sloveniji. (Niti 1000 več, <1000 vzponov pa itak ne koristi več>)
# nek približni TODO
- grem še po najboljših 100 rangiranih userjih in zlovdam njihove vzpone? / 
ali pa po vseh userjih iz prvega dataseta, pa pri vsakem dobim vse vzpone. Tk res lahko razlikujem userje*

*10 000 vzponov ni tako veliko. Priden skalaš jih sigurno lahko naklofa 10 na teden (~500 na leto), tk da 10 000 vzponov zapolni 20 plezalcev v enem letu... Tia približna ocena je očitno prevelika, vendar pa vseeno podatki o vzponih segajo nazaj le do leta 2018, zanimivo pa bi bilo gledat vsaj desetletje vzponov, da opazujemo potencialen dvig ravni
**Plan za naprej:** iz trenutne baze lepo dobim plezana slovenska plezališča, in grem po njihovih vzponih. Imajo lepo berljivo html tabelo, za kar tud poberem točke najs

Pa vsa plezališča dobim na:
https://www.8a.nu/crags/sportclimbing/slovenia

# pridobivanje podatkov
S prva sem podatke dobil preko strani 8a.nu/ascents (lepo v jsonih)
Vendar sem dobil le 10 000 vzponov (rad bi jih več)
Zato sem zregexiral vsa plezališča, in grem za vsakega dobit vse vzpone.
Žal me 8a.nu pusti le to zadnjih 10 000 vzponov za plezališče. Vseeno ok, iz 2018 sem porišel na 2015, 5 let pa že mneki je.