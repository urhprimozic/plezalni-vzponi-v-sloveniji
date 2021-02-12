# funcije so iz predavanj, z rahlimi predelavami
# spisal jih je prof. Matija Pretnar
import csv
import json
import os
import requests
import sys
# TODO naredi
# lepše dela takole:
korenina =  os.path.dirname(__file__)


def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)

def shrani_spletno_stran_v_datoteko(url, ime_datoteke):
    '''Vsebino strani na danem naslovu shrani na konec datoteke z danim imenom.'''
    try:
        print(f'Shranjujem {url} v {ime_datoteke}...', end='')
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
    else:
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'a', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')

def shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False):
    '''Vsebino strani na danem naslovu shrani v datoteko z danim imenom.'''
    try:
        print(f'Shranjujem {url} v {ime_datoteke}...', end='')
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke) and not vsili_prenos:
            print('shranjeno že od prej!')
            return
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
    else:
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')


def vsebina_datoteke(ime_datoteke):
    '''Vrne niz z vsebino datoteke z danim imenom.'''
    with open(ime_datoteke, encoding='utf-8') as datoteka:
        return datoteka.read()


def zapisi_csv(slovarji, imena_polj, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)


def zapisi_json(objekt, ime_datoteke):
    '''Iz danega objekta ustvari JSON datoteko.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as json_datoteka:
        json.dump(objekt, json_datoteka, indent=4, ensure_ascii=False)

def ocene():
    '''
    Vrne tabelo veljavnih stringov ocen
    '''
    ans = []
    for i in range(1, 10):
        for j in ['a', 'a+', 'b', 'b+', 'c', 'c+']:
            ans.append(str(i)+j)
    return ans

# nekatera plezalisca nastpoajo pod različnimi imeni
def popravi_ime(ime):
    '''
    Vrne pravo ime plezalisca.
    '''
    if ime=='mija-pec' or ime=='misja-pec':
        return 'osp-misja-pec'
    if ime=='dolanova-soteska':
        return 'dovzanova-soteska'
    return ime

def popravi_ime_smeri(ime):
    '''
    Zbriše whitespace iz konca
    '''
    return ime.rstrip()


ocene = ['1a', '1a+', '1b', '1b+', '1c', '1c+', '2a', '2a+', '2b', '2b+', '2c', '2c+', '3a', '3a+', '3b', '3b+', '3c', '3c+', '4a', '4a+', '4b', '4b+', '4c', '4c+', '5a', '5a+', '5b', '5b+', '5c', '5c+', '6a', '6a+', '6b', '6b+', '6c', '6c+', '7a', '7a+', '7b', '7b+', '7c', '7c+', '8a', '8a+', '8b', '8b+', '8c', '8c+', '9a', '9a+'] #, '9b', '9b+', '9c', '9c+']

#Funckija za vrednotenje ocen:
def ocena_v_int(ocena):
    if ocena in ocene:
        return ocene.index(ocena)
    # Lahke smeri nas ne zanimajo (in smeri z oceno 1a v resnici ne obstajajo)
    # Zato lahko vse napake v podatkih slikam v '1a'
    return 0
        
def int_v_oceno(x):
    return ocene[x]