import os
import re
import orodja
import os
import logging
import tqdm
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


seznam_strik = ['osp-misja-pec', 'kotecnik', 'crni-kal', 'creta', 'bohinjska-bela', 'kupljenik', 'ter', 'retovje', 'vipavska-bela', 'bitnje', 'skedenj', 'preddvor', 'pod-reko-planino', 'osp', 'bohinj', 'kamnitnik', 'pod-skalo', 'gornji-ig', 'krievska-vas', 'golobove-pecine', 'vipava', 'vransko', 'armesko', 'snovik', 'burjakove-peci', 'kozja-jama', 'iki-vintgar', 'senica', 'lutne-skale', 'trenta', 'slomnik', 'bitenj-potok', 'kamnik', 'dolanova-soteska', 'pec', 'sivnica', 'vranja-pec', 'nad-savo', 'buncove-skale', 'gorje', 'dolge-njive', 'boc', 'lijak', 'misja-pec', 'zatrata', 'zminec', 'turnc', 'sopota', 'cerjan', 'zavrnica', 'strug', 'pri-ciginju', 'logarska-dolina', 'risnik', 'prtovc', 'kotec', 'colnisce', 'colnice', 'luknja', 'seginov-potok', 'korosica', 'sumberk', 'renke', 'gore', 'jereka', 'kal-koritnica', 'skedenca', 'marof', 'male-bele-stene', 'radovna', 'krvavec', 'mija-pec', 'drnulk', 'predloka', 'nadiza', 'bodece', 'c', 'bodesce', 'pri-plajerju', 'pod-golico', 'kamnika-bistrica', 'umberk', 'nomenj', 'boben', 'unknown-crag', 'kamniti-grad', 'mlinarjeva-pec', 'kegl', 'lipje', 'vric', 'soder-graben', 'urbasova-skala', 'zvanov-rob', 'armeko', 'pod-suso', 'velbanca', 'sele', 'matvoz', 'gabrska-pec', 'ospo', 'pod-kopitcem', 'darkpoint', 'crni-kal-osp', 'vrsic', 'dov', 'florjan', 'sezana', 'mislinja', 'pri-pavru', 'kot-nad-prevaljami', 'boe', 'erni-kal', 'za-goro', 'pec-pri-bohinju', 'brdce', 'pri-zvikarju', 'predil', 'slap-ob-idrijci', 'claret', 'oder-graben', 'hrastnik', 'pod-skalo-hrastnik', 'dvigrad', 'lavorcek', 'postojna', 'koroica', 'ereta', 'mlinska-pec', 'bele-stene', 'zevt', 'igla', 'zadnjiki-ozebnik', 'dark-point', 'porezen', 'kanjon', 'secret', 'bohinj-pod-skalco', 'nova-creta', 'kotepercentu010dnik', 'planina-pri-s', 'sumberg', 'pir-plajerju', 'plezalisce-pod-golico', 'blaceva-skala', 'osp-babna', 'bohinj-bellevue', 'steiner-alpen', 'kanin', 'osp-babna-zhzih-verrev', 'dol-pri-hrastniku', 'seana', 'radlje-ob-dravi', 'bled', 'kratova-skala', 'crnotice', 'stara-creta', 'stenge', 'no-name', 'okreselj', 'kotecnik-oboki', 'matjaeve-kamre', 'bela-pec', 'slovenija', 'kompanj', 'koteenik', 'kamniska-bistrica', 'nadia', 'koprivnik', 'luknja-novo-mesto', 'sevnica', 'klemenca-pec', 'mitnica', 'urbasova-pec', 'pee', 'marela', 'kovaeevec', 'puscavnikove-skale', 'matjazeve-kamre', 'bodeee', 'skdnj', 'deskle', 'zelenc', 'vrie', 'p', 'liboje', 'vranske-peci-kot', 'mangart', 'planina-nad-s', 'jereka-zevt', 'pod-suo', '7b+', 'kogel', 'triglav', 'ksa', 'pri-skalarju-zminec', 'vezica', 'sidarta', 'verd', 'ospo-grottone', 'bohinjska-bela-nova', 'vranske-peci', 'pri-skalarju-zminec-bhnbo-verrev', 'pc-ljubljana', 'buzetski-kanjon', 'nad-sitom-glava', 'pisano-celo', 'roc', 'predil-wandl', 'podpec', 'osp-sektor-babna', 'postumia', 'luknja-b', 'kotecnik-luska', 'poglejska-cerkev', 'perovo', 'kizevaska-vas', 'velika-baba', 'krvavica', 'ops', 'triglav-valley', 'poglejska-cerkev', 'veliki-vrh', '7a', '7b', 'secret-slovene-crag', 'straznik', 'triglav-north-face', 'lavoreek', 'gromberg', 'blaeeva-skala', 'robanov-kot', 'the-place', 'null', 'mrzla-gora', 'taborska-stena', 'napoleonica', 'planina-nas-s', 'napolejonica', 'predil-wand', 'kotecnik-kolomon', 'misja-pec-5b29a-verrev', 'osb', 'lucki-dedec', 'skuta', 'mica-pec', 'kote', 'dov-d1z86-verrev', 'skg', 'sulov', 'site', 'pod-skalo-hrastnik-iwafi-verrev', 'misja-pec-b-osp-misja-pec', 'babna-osp-misja-pec', 'osapska-luknja', 'ss', 'nova-gorica', 'babna', 'besnica', 'blazceva-skala', 'veica', 'bella-slo', 'vinkuran', 'x', 'miska', 'banje', 'iski-vingar', 'fontanella', '8a', '7b+-c', 'rudnica', 'truca', 'oso', 'ojstrica', 'roc-de-gorb', 'bohnjska-bela', 'velika-koroska-baba', 'bugs-bunny', 'leteci-dolent', 'os', 'mija-jama', 'eerjan', 'baratro', 'costiliera', 'kanal', 'kanfanar', 'belvie', 'how-bizar', 'okn-mojstrana', 'bela-pee', 'crnikal', 'za-savo', 'kurtatsch', 'krievnik', 'costiera', 'julske-alpy', 'maple-canyon', 'pernice', 'miija-pec', 'palestra-masso-pirona-laghi-di-fusine', 'zelena-dolina', 'misja', 'tolmin', 'kobarid', 'raspadalica', 'bele-vode-sostanj', 'precin', 'la-moreria', 'luska', 'vrbovsko', 'kamnniska-bistrica', 'misja-pec-a-osp-misja-pec', 'aurisina', 'mangat', 'hubelj', 'blaziceva-skala', 'dp', 'sumberk-slovenia', 'julische-alpen', 'trentarski-ozebnik', 'planja', 'faklove-spary', 'la-atalaya', 'pajkova-streha', 'radlje', 'bela', 'ulassai', 'lutne', 'prepihova-dolina', 'misja-pec-a6580-verrev', 'misja-46819-verrev', 'babna-512e6-verrev', 'julische-alpen-debela-pec', 'kotecnik-00rv1', 'veica', 'mija-pec-8nms9-verrev', 'bella-slo', 'vinkuran', 'x', 'miska', 'slo-osp', '7c+', 'sahnhoff', 'luminy-le-virage', 'kotecniktaventaa', 'kotcnik', 'bellevue', 'alpe', 'travnik-n-face', 'piccolo-mangart', 'ciginj', 'mar', 'crni-kal-osp-lpocu-verrev', 'bad-eisenkappel', 'mallorca', 'warm', 'buzet', 'krubove-peci', 'mija-pee', 'mali-koritniki-mangart', 'drnulk-cepovan', 'piccolo-mangart', 'bohnjska-bela', 'ciginj', 'mar', 'velika-koroska-baba', 'bugs-bunny', 'leteci-dolent', 'os', 'mija-jama', 'eerjan', 'baratro', 'costiliera', 'kanal', 'kanfanar', 'belvie', 'how-bizar', 'okn-mojstrana', 'bela-pee', 'crnikal', 'za-savo', 'kurtatsch', 'krievnik', 'costiera', 'julske-alpy', 'maple-canyon', 'pernice', 'miija-pec', 'palestra-masso-pirona-laghi-di-fusine', 'zelena-dolina', 'puscavnikove-skale-y3efi', 'treinta']

def vzponi_strik_v_json_csv(seznam_imen=seznam_strik):
    '''
    Iz datotek vzponi_.*.html pobere ven podatke o vseh vzponih
    '''
    #<td class="col-user show-for-tablet" data-v-3102a057=".*?"><a href=".*?user/(?P<uporabnik>.*?)/.*\n\s*(?P<plezalec>.+)\n.*\n\s*(?P<datum>.*)\n.*?<i title="(?P<poskusi>.*?)".*\n.*\n.*\n\s*(?P<smer>.*?)\((?P<tezavnost>.*?)\)
    vzorec= (
        r'<td class="col-user show-for-tablet" data-v-3102a057=".*?"><a href=".*?user/(?P<uporabnik>.*?)/' #uporabniško ime
        r'.*\n\s*(?P<plezalec>.+)' #ime plezalca
        r'\n.*\n\s*(?P<datum>.*)' # datum
        r'\n.*?<i title="(?P<poskusi>.*?)"'
        r'.*\n.*\n.*\n\s*' #smo tik pred imenom smeri
        r'(?P<smer>.*?)\((?P<tezavnost>.*?)\)' #ime in tezavnost smeri
      #  r'' #tik pred prvim možnik lkomentarjem
        r'([\S\s\n]*?<!----> <!---->(\s*<b data-v-3102a057="">\n\s*(?P<opomba>.*))?)?'
       # r'' # karkoli je že vmes
        r'[\S\s\n]*?<span data-v-3102a057="">'#začetek komentarja
        r'(?P<komentar>[\S\s\n]*?)'
        r'</span>'

    )
    seznam_vzponov = []
    # for plezalisce in seznam_imen:
    for plezalisce in tqdm.tqdm(seznam_strik, total=len(seznam_strik)):
        datoteka = os.path.join(mapa_s_podatki, f'vzponi_{plezalisce}.html')
        # datoteka = os.path.join(mapa_s_podatki, f'demo.html')
        with open(datoteka, 'r') as txt:
            besedilo = txt.read()
        
        count = 0
        for zadetek in re.finditer(pattern=vzorec, string=besedilo):
            count += 1
            slovar_skupine = zadetek.groupdict()
            slovar = {
            'uporabnik' : slovar_skupine.get('uporabnik'),   
            'plezalec' : slovar_skupine.get('plezalec'),
            'plezalisce' : plezalisce,
            'smer' : slovar_skupine.get('smer'),
            'tezavnost' : slovar_skupine.get('tezavnost'),
            'poskusi' : slovar_skupine.get('poskusi'), # redpoint vs flash vs onsight
            'datum' : slovar_skupine.get('datum'),
            'opomba' : slovar_skupine.get('opomba'),
            'komentar' : slovar_skupine.get('komentar')
            }
            seznam_vzponov.append(slovar)
        logging.info(f'Našel {count} zadetkov.')
        return count
    orodja.zapisi_json(seznam_vzponov, os.path.join(mapa_s_podatki, 'vzponi_strik.json'))
    imena_polj =['uporabnik', 'plezalec', 'plezalisce', 'smer', 'tezavnost', 'poskusi', 'datum', 'komentar']
    orodja.zapisi_csv(seznam_vzponov, imena_polj, os.path.join(mapa_s_podatki, 'vzponi_strik.csv'))
    


