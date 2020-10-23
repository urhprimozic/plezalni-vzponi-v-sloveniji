# iz 8a.nu/ascents povleče JSON s podatki
import orodja
# import argparse
# import sys
import os
import logging
velikost_strani = 1000
alpha = 10
omega = 20
korenina =  os.path.dirname(__file__)

def plezalisca():
    '''
    Shrani htmlje iz https://www.8a.nu/crags/sportclimbing/slovenia?page=1
    '''    
    logging.info('Nalagam htmlje s tabelami vseh plezališč...')
    stevilo_strani_strik = 20
    stevilo_strani_balvani = 9
    # štrik je lajf
    datoteka = os.path.join('../','data', 'plezalisca_strik.html')
    for i in range(1, 1 + stevilo_strani_strik):
        url = f'https://www.8a.nu/crags/sportclimbing/slovenia?page={i}'
        orodja.shrani_spletno_stran_v_datoteko(url, datoteka)
    # bolderji so tud lajf
    datoteka = os.path.join('../','data', 'plezalisca_balvani.html')
    for i in range(1, 1 + stevilo_strani_balvani):
        url = f'https://www.8a.nu/crags/bouldering/slovenia?page={i}'
        orodja.shrani_spletno_stran_v_datoteko(url, datoteka)



# pomojem bo 50 000 vnosov čez glavo
# for stran in range(alpha, omega):
#     url = f'https://www.8a.nu/api/follows/global?pageIndex={stran}&pageSize={velikost_strani}&countrySlug=slovenia'
#     orodja.shrani_spletno_stran(url, f'data/vzponi_{stran}_{velikost_strani}.json')

# fancy shit
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-s", "--url")
#     parser.add_argument("-w", "--file_name", default="")
#     # pobere argumente
#     args = sys.argv[1:]
#     parsed = parser.parse_args(args)
#     step = parsed.url
#     file_name = parsed.file_name
#     # shrani spletno stran
#     pot_v_x = os.path.join('data', file_name)
#     orodja.shrani_spletno_stran(step, pot_v_x)
