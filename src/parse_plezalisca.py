import os
import re
import orodja
import os
# mal se igram
korenina =  os.path.dirname(__file__)
mapa_s_podatki = os.path.join(korenina, '../data')
datoteka_balvani = os.path.join(mapa_s_podatki, 'plezalisca_balvani.html')
datoteka_strik = os.path.join(mapa_s_podatki, 'plezalisca_strik.html')

def strik_v_json():
    '''
    Iz html-ja v plezalisca_strik.html pridobi podatke o plezaliscih (ime, regija?, url) in jih zapise v JSON
    '''
    # passed
    vzorec = (
        r'<td class="col-name"'
        r'.*class="name-link" data.*?<a href='
        r'"(?P<url>.+?)"' # dobi url plezalisca
        r'.data.*?>\n\s+(.+?/)?' #zignorira? potencialno regijo (Osp/Mišja Peč)
        r'(?P<ime>.*)\n' # ime plezališča
        r'\s*.*\n[\S\s\n]*?</a></span></p></td>\s?<td.*?>\n\s*(?P<stevilo_vzponov>.*)'
    )
    with open(datoteka_strik, 'r') as txt:
        besedilo = txt.read()
    
    seznam_plezalisc = []
    for zadetek in re.finditer(pattern=vzorec, string=besedilo):
        slovar_skupine = zadetek.groupdict()
        slovar = {
            'ime' : slovar_skupine.get('ime'),
            'url' : 'https://www.8a.nu' + slovar_skupine.get('url')[:-6], # hočem cel url, ampak ne med routes
            'stevilo_vzponov' : slovar_skupine.get('stevilo_vzponov')
        }
        seznam_plezalisc.append(slovar)
    orodja.zapisi_json(seznam_plezalisc, os.path.join(mapa_s_podatki, 'plezalisca.json'))

def balvani_v_json():
    '''
    Iz html-ja v plezalisca_balvani.html pridobi podatke o plezaliscih (ime, regija?, url) in jih zapise v JSON
    '''
    # passed
    vzorec = (
        r'<td class="col-name"'
        r'.*class="name-link" data.*?<a href='
        r'"(?P<url>.+?)"' # dobi url plezalisca
        r'.data.*?>\n\s+(.+?/)?' #zignorira? potencialno regijo (Osp/Mišja Peč)
        r'(?P<ime>.*)\n' # ime plezališča
        r'\s*.*\n[\S\s\n]*?</a></span></p></td>\s?<td.*?>\n\s*(?P<stevilo_vzponov>.*)'
    )
    with open(datoteka_balvani, 'r') as txt:
        besedilo = txt.read()
    
    seznam_plezalisc = []
    for zadetek in re.finditer(pattern=vzorec, string=besedilo):
        slovar_skupine = zadetek.groupdict()
        slovar = {
            'ime' : slovar_skupine.get('ime'),
            'url' : 'https://www.8a.nu' + slovar_skupine.get('url')[:-6], # hočem cel url, ampak ne med routes
            'stevilo_vzponov' : slovar_skupine.get('stevilo_vzponov')
        }
        seznam_plezalisc.append(slovar)
    orodja.zapisi_json(seznam_plezalisc, os.path.join(mapa_s_podatki, 'balvani.json'))