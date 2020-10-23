# iz 8a.nu/ascents povleče JSON s podatki
import orodja
velikost_strani = 10000
# pomojem bo 50 000 vnosov čez glavo
for stran in range(5):
    url = f'https://www.8a.nu/api/follows/global?pageIndex={stran}&pageSize={velikost_strani}&countrySlug=slovenia'
    orodja.shrani_spletno_stran(url, f'data/vzponi_{stran}_{velikost_strani}.json')