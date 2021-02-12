import os
import re
import orodja
import os
import logging
import tqdm
import json

# mal se igram
korenina = os.path.dirname(__file__)
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
        r'"(?P<url>.+?)"'  # dobi url plezalisca
        # zignorira? potencialno regijo (Osp/Mišja Peč)
        r'.data.*?>\n\s+(.+?/)?'
        r'(?P<ime>.*)\n'  # ime plezališča
        r'\s*.*\n[\S\s\n]*?</a></span></p></td>\s?<td.*?>\n\s*(?P<stevilo_vzponov>.*)'
    )
    with open(datoteka_strik, 'r') as txt:
        besedilo = txt.read()

    seznam_plezalisc = []
    for zadetek in re.finditer(pattern=vzorec, string=besedilo):
        slovar_skupine = zadetek.groupdict()
        slovar = {
            'ime': slovar_skupine.get('ime'),
            # hočem cel url, ampak ne med routes
            'url': 'https://www.8a.nu' + slovar_skupine.get('url')[:-6],
            'stevilo_vzponov': slovar_skupine.get('stevilo_vzponov')
        }
        seznam_plezalisc.append(slovar)
    orodja.zapisi_json(seznam_plezalisc, os.path.join(
        mapa_s_podatki, 'plezalisca.json'))


def balvani_v_json():
    '''
    Iz html-ja v plezalisca_balvani.html pridobi podatke o plezaliscih (ime, regija?, url) in jih zapise v JSON
    '''
    # passed
    vzorec = (
        r'<td class="col-name"'
        r'.*class="name-link" data.*?<a href='
        r'"(?P<url>.+?)"'  # dobi url plezalisca
        # zignorira? potencialno regijo (Osp/Mišja Peč)
        r'.data.*?>\n\s+(.+?/)?'
        r'(?P<ime>.*)\n'  # ime plezališča
        r'\s*.*\n[\S\s\n]*?</a></span></p></td>\s?<td.*?>\n\s*(?P<stevilo_vzponov>.*)'
    )
    with open(datoteka_balvani, 'r') as txt:
        besedilo = txt.read()

    seznam_plezalisc = []
    for zadetek in re.finditer(pattern=vzorec, string=besedilo):
        slovar_skupine = zadetek.groupdict()
        slovar = {
            'ime': slovar_skupine.get('ime'),
            # hočem cel url, ampak ne med routes
            'url': 'https://www.8a.nu' + slovar_skupine.get('url')[:-6],
            'stevilo_vzponov': slovar_skupine.get('stevilo_vzponov')
        }
        seznam_plezalisc.append(slovar)
    orodja.zapisi_json(seznam_plezalisc, os.path.join(
        mapa_s_podatki, 'balvani.json'))


# te plezališča sem dal ven ker so nepomembna (ni vzponov zadnje 5 let)
#'dov',  'florjan', 'sezana', 'mislinja', 'pri-pavru', 'kot-nad-prevaljami', 'boe', 'erni-kal', 'za-goro', 'pec-pri-bohinju', 'brdce', 'pri-zvikarju', 'predil', 'slap-ob-idrijci', 'claret', 'oder-graben', 'hrastnik', 'pod-skalo-hrastnik', 'dvigrad', 'lavorcek', 'postojna', 'koroica', 'ereta', 'mlinska-pec', 'bele-stene', 'zevt', 'igla', 'zadnjiki-ozebnik', 'dark-point', 'porezen', 'kanjon', 'secret', 'bohinj-pod-skalco', 'nova-creta', 'kotepercentu010dnik', 'planina-pri-s', 'sumberg', 'pir-plajerju', 'plezalisce-pod-golico', 'blaceva-skala', 'osp-babna', 'bohinj-bellevue', 'steiner-alpen', 'kanin', 'osp-babna-zhzih-verrev', 'dol-pri-hrastniku', 'seana', 'radlje-ob-dravi', 'bled', 'kratova-skala', 'crnotice', 'stara-creta', 'stenge', 'no-name', 'okreselj', 'kotecnik-oboki', 'matjaeve-kamre', 'bela-pec', 'slovenija', 'kompanj', 'koteenik', 'kamniska-bistrica', 'nadia', 'koprivnik', 'luknja-novo-mesto', 'sevnica', 'klemenca-pec', 'mitnica', 'urbasova-pec', 'pee', 'marela', 'kovaeevec', 'puscavnikove-skale', 'matjazeve-kamre', 'bodeee', 'skdnj', 'deskle', 'zelenc', 'vrie', 'p', 'liboje', 'vranske-peci-kot', 'mangart', 'planina-nad-s', 'jereka-zevt', 'pod-suo', '7b+', 'kogel', 'triglav', 'ksa', 'pri-skalarju-zminec', 'vezica', 'sidarta', 'verd', 'ospo-grottone', 'bohinjska-bela-nova', 'vranske-peci', 'pri-skalarju-zminec-bhnbo-verrev', 'pc-ljubljana', 'buzetski-kanjon', 'nad-sitom-glava', 'pisano-celo', 'roc', 'predil-wandl', 'podpec', 'osp-sektor-babna', 'postumia', 'luknja-b', 'kotecnik-luska', 'poglejska-cerkev', 'perovo', 'kizevaska-vas', 'velika-baba', 'krvavica', 'ops', 'triglav-valley', 'poglejska-cerkev', 'veliki-vrh', '7a', '7b', 'secret-slovene-crag', 'straznik', 'triglav-north-face', 'lavoreek', 'gromberg', 'blaeeva-skala', 'robanov-kot', 'the-place', 'null', 'mrzla-gora', 'taborska-stena', 'napoleonica', 'planina-nas-s', 'napolejonica', 'predil-wand', 'kotecnik-kolomon', 'misja-pec-5b29a-verrev', 'osb', 'lucki-dedec', 'skuta', 'mica-pec', 'kote', 'dov-d1z86-verrev', 'skg', 'sulov', 'site', 'pod-skalo-hrastnik-iwafi-verrev', 'misja-pec-b-osp-misja-pec', 'babna-osp-misja-pec', 'osapska-luknja', 'ss', 'nova-gorica', 'babna', 'besnica', 'blazceva-skala', 'veica', 'bella-slo', 'vinkuran', 'x', 'miska', 'banje', 'iski-vingar', 'fontanella', '8a', '7b+-c', 'rudnica', 'truca', 'oso', 'ojstrica', 'roc-de-gorb', 'bohnjska-bela', 'velika-koroska-baba', 'bugs-bunny', 'leteci-dolent', 'os', 'mija-jama', 'eerjan', 'baratro', 'costiliera', 'kanal', 'kanfanar', 'belvie', 'how-bizar', 'okn-mojstrana', 'bela-pee', 'crnikal', 'za-savo', 'kurtatsch', 'krievnik', 'costiera', 'julske-alpy', 'maple-canyon', 'pernice', 'miija-pec', 'palestra-masso-pirona-laghi-di-fusine', 'zelena-dolina', 'misja', 'tolmin', 'kobarid', 'raspadalica', 'bele-vode-sostanj', 'precin', 'la-moreria', 'luska', 'vrbovsko', 'kamnniska-bistrica', 'misja-pec-a-osp-misja-pec', 'aurisina', 'mangat', 'hubelj', 'blaziceva-skala', 'dp', 'sumberk-slovenia', 'julische-alpen', 'trentarski-ozebnik', 'planja', 'faklove-spary', 'la-atalaya', 'pajkova-streha', 'radlje', 'bela', 'ulassai', 'lutne', 'prepihova-dolina', 'misja-pec-a6580-verrev', 'misja-46819-verrev', 'babna-512e6-verrev', 'julische-alpen-debela-pec', 'kotecnik-00rv1', 'veica', 'mija-pec-8nms9-verrev', 'bella-slo', 'vinkuran', 'x', 'miska', 'slo-osp', '7c+', 'sahnhoff', 'luminy-le-virage', 'kotecniktaventaa', 'kotcnik', 'bellevue', 'alpe', 'travnik-n-face', 'piccolo-mangart', 'ciginj', 'mar', 'crni-kal-osp-lpocu-verrev', 'bad-eisenkappel', 'mallorca', 'warm', 'buzet', 'krubove-peci', 'mija-pee', 'mali-koritniki-mangart', 'drnulk-cepovan', 'piccolo-mangart', 'bohnjska-bela', 'ciginj', 'mar', 'velika-koroska-baba', 'bugs-bunny', 'leteci-dolent', 'os', 'mija-jama', 'eerjan', 'baratro', 'costiliera', 'kanal', 'kanfanar', 'belvie', 'how-bizar', 'okn-mojstrana', 'bela-pee', 'crnikal', 'za-savo', 'kurtatsch', 'krievnik', 'costiera', 'julske-alpy', 'maple-canyon', 'pernice', 'miija-pec', 'palestra-masso-pirona-laghi-di-fusine', 'zelena-dolina', 'puscavnikove-skale-y3efi', 'treinta'
seznam_strik = ['osp-misja-pec', 'kotecnik', 'crni-kal', 'creta', 'bohinjska-bela', 'kupljenik', 'ter', 'retovje', 'vipavska-bela', 'bitnje', 'skedenj', 'preddvor', 'pod-reko-planino', 'osp', 'bohinj', 'kamnitnik', 'pod-skalo', 'gornji-ig', 'krievska-vas', 'golobove-pecine', 'vipava', 'vransko', 'armesko', 'snovik', 'burjakove-peci', 'kozja-jama', 'iki-vintgar', 'senica', 'lutne-skale', 'trenta', 'slomnik', 'bitenj-potok', 'kamnik', 'dolanova-soteska', 'pec', 'sivnica', 'vranja-pec', 'nad-savo', 'buncove-skale', 'gorje', 'dolge-njive', 'boc', 'lijak', 'misja-pec', 'zatrata', 'zminec', 'turnc', 'sopota', 'cerjan', 'zavrnica', 'strug',
                'pri-ciginju', 'logarska-dolina', 'risnik', 'prtovc', 'kotec', 'colnisce', 'colnice', 'luknja', 'seginov-potok', 'korosica', 'sumberk', 'renke', 'gore', 'jereka', 'kal-koritnica', 'skedenca', 'marof', 'male-bele-stene', 'radovna', 'krvavec', 'mija-pec', 'drnulk', 'predloka', 'nadiza', 'bodece', 'c', 'bodesce', 'pri-plajerju', 'pod-golico', 'kamnika-bistrica', 'umberk', 'nomenj', 'boben', 'unknown-crag', 'kamniti-grad', 'mlinarjeva-pec', 'kegl', 'lipje', 'vric', 'soder-graben', 'urbasova-skala', 'zvanov-rob', 'armeko', 'pod-suso', 'velbanca', 'sele', 'matvoz', 'gabrska-pec', 'ospo', 'pod-kopitcem', 'darkpoint', 'crni-kal-osp', 'vrsic']


def vzponi_strik_v_json_csv(seznam_imen=seznam_strik):
    '''
    Iz datotek vzponi_.*.html pobere ven podatke o vseh vzponih
    '''
    vzorec = r'<td class=\"col-user show-for-tablet\" data-v-3102a057(=\".*?\")?><a href=\".*?user/(?P<uporabnik>.*?)/.*\n\s*(?P<plezalec>.+)\n.*\n\s*(?P<datum>.*)\n.*?<i title=\"(?P<poskusi>.*?)\".*\n.*\n.*\n\s*(?P<smer>.*?)\((?P<tezavnost>.*?)\)[\S\s\n]*?<span data-v-3102a057>(?P<komentar>.*?)</span>'
    seznam_vzponov = []
    count = 0
    # for plezalisce in seznam_imen:
    for plezalisce in tqdm.tqdm(seznam_imen, total=len(seznam_imen)):
        datoteka = os.path.join(mapa_s_podatki, f'vzponi_{plezalisce}.html')
        #datoteka = os.path.join(mapa_s_podatki, f'demo.html')
        #datoteka = os.path.join(mapa_s_podatki, f'vzponi_bodece.html')

        with open(datoteka, 'r') as txt:
            besedilo = txt.read()

        for zadetek in re.finditer(pattern=vzorec, string=besedilo):
            count += 1
            slovar_skupine = zadetek.groupdict()
            slovar = {
                'uporabnik': slovar_skupine.get('uporabnik'),   #
                'plezalec': slovar_skupine.get('plezalec'),
                'plezalisce': plezalisce,
                'smer': slovar_skupine.get('smer'),
                'tezavnost': slovar_skupine.get('tezavnost'),
                # redpoint vs flash vs onsight #
                'poskusi': slovar_skupine.get('poskusi'),
                'datum': slovar_skupine.get('datum'),
                # 'opomba' : slovar_skupine.get('opomba'),
                'komentar': slovar_skupine.get('komentar')
            }
            print(slovar_skupine.get('smer'))
            seznam_vzponov.append(slovar)
        print(len(seznam_vzponov))
        logging.info(f'Našel {count} zadetkov.')
    # return seznam_vzponov

    orodja.zapisi_json(seznam_vzponov, os.path.join(
        mapa_s_podatki, 'vzponi_strik.json'))
    imena_polj = ['uporabnik', 'plezalec', 'plezalisce', 'smer',
                  'tezavnost', 'poskusi', 'datum', 'opomba', 'komentar']
    orodja.zapisi_csv(seznam_vzponov, imena_polj, os.path.join(
        mapa_s_podatki, 'vzponi_strik.csv'))

    return count


def povezovalne_vzponi_strik(filename='vzponi_strik.json'):
    '''
    Iz jsona pobere podatke in naredi lepše tabele.
    '''
    datoteka = os.path.join(mapa_s_podatki, filename)
    with open(datoteka) as f:
        vzponi = json.load(f)
    
    povprecne = {}

    vzponi_z_indeksom = []
    plezalci = []
    plezalisca = []
    smeri_plezalisca = []
    smeri = []
    # povprecne
    for id, vzpon in enumerate(vzponi):
         # popravki
        vzpon['plezalisce'] = orodja.popravi_ime(vzpon['plezalisce'])
        vzpon['smer'] = orodja.popravi_ime_smeri(vzpon['smer'])

        tmp_ime = vzpon['smer'] + '§'+ vzpon['plezalisce']
        if povprecne.get(tmp_ime) is None:
            povprecne[tmp_ime] = [orodja.ocena_v_int(vzpon['tezavnost'])]
        else:
            povprecne[tmp_ime] = povprecne[tmp_ime] + [orodja.ocena_v_int(vzpon['tezavnost'])]

    for k, v in povprecne.items():
        vse = povprecne[k]
        povprecne[k] = orodja.int_v_oceno(int(round(sum(vse)/len(vse))))
    #print(povprecne)

    for id, vzpon in enumerate(vzponi):
        # v podatkih se pojavlja napaka, kjer je ime smeri "N.N." . 
        # Take ignoriramo. 
        # (je jih ~300, kar je manj kot 1%)
        # večinoma so to lahke smeri)
        if vzpon['smer'] == 'N.N.':
            # print("Napaka. ime smeri je N.N.")
            continue

        # povprecne
        # tezanost - kako težko je blo pelzalcu
        # ocena - resnica (povprečje ;) )
        vzpon['ocena'] = '1a'
        s = vzpon['smer']
        p = vzpon['plezalisce']
        if not povprecne.get(s + '§' + p) is None:
            vzpon['ocena'] = povprecne[s + '§' + p]
        

        cel_vzpon = vzpon
        cel_vzpon['id'] = id
        vzponi_z_indeksom.append(cel_vzpon)
        plezalci.append(
            {'uporabnik': vzpon['uporabnik'], 'plezalec': vzpon['plezalec'], 'id': id})
        plezalisca.append({'plezalisce': vzpon['plezalisce'], 'id': id})
        smeri.append( {'smer': vzpon['smer'], 'id': id})
        smeri_plezalisca.append(
            {'smer-plezalisce': vzpon['smer'] + vzpon['plezalisce'], 'id': id})

    orodja.zapisi_json(vzponi_z_indeksom, os.path.join(
        mapa_s_podatki, 'vzponi.json'))
    orodja.zapisi_csv(vzponi_z_indeksom, ['id', 'uporabnik', 'plezalec', 'plezalisce', 'smer', 'tezavnost','ocena',
                                          'poskusi', 'datum', 'opomba', 'komentar'], os.path.join(mapa_s_podatki, 'vzponi.csv'))
    
    orodja.zapisi_json(plezalci, os.path.join(mapa_s_podatki, 'plezalci.json'))
    orodja.zapisi_csv(plezalci, ['uporabnik', 'plezalec', 'id'], os.path.join(mapa_s_podatki, 'plezalci.csv'))

    orodja.zapisi_json(plezalisca, os.path.join(mapa_s_podatki, 'plezalisca.json'))
    orodja.zapisi_csv(plezalisca, ['plezalisce', 'id'], os.path.join(mapa_s_podatki, 'plezalisca.csv'))

    orodja.zapisi_json(smeri_plezalisca, os.path.join(mapa_s_podatki, 'smeri_plezalisca.json'))
    orodja.zapisi_csv(smeri_plezalisca, ['smer-plezalisce', 'id'], os.path.join(mapa_s_podatki, 'smeri_plezalisca.csv'))

    orodja.zapisi_json(smeri, os.path.join(mapa_s_podatki, 'smeri.json'))
    orodja.zapisi_csv(smeri, ['smer', 'id'], os.path.join(mapa_s_podatki, 'smeri.csv'))
    

