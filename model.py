import random
import json

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = '0'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'Z'
DATOTEKA_S_STANJEM = 'stanje.json'
DATOTEKA_Z_BESEDAMI = 'besede.txt'


class Igra:
    def __init__(self, niz, seznam=None):
        self.geslo = niz
        self.crke = [] if seznam == None else seznam

    def napacne_crke(self):
        seznam_napacnih = []
        for crka in self.crke:
            if crka not in self.geslo:
                seznam_napacnih.append(crka)
        return seznam_napacnih         

    def pravilne_crke(self):
        seznam_pravilnih = []
        for crka in self.crke:
            if crka in self.geslo:
                seznam_pravilnih.append(crka)
        return seznam_pravilnih

    def stevilo_napacnih(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napacnih() >= STEVILO_DOVOLJENIH_NAPAK
            
    
    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.pravilne_crke():
                return False
        else:
            return True

    def pravilni_del_gesla(self):
        niz1 = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz1+= crka + ' '
            else:
                niz1+= '_ '
        return niz1


    def nepravilni_del_gesla(self):
        niz2 = ''
        for crka in self.crke:
            if crka not in self.geslo:
                niz2+= crka + ' '
        return niz2

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else: 
            self.crke.append(crka)
            if crka in self.pravilne_crke():
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

bazen_besed = []

with open('besede.txt', 'r') as nabor_besed:
    for vrstica in nabor_besed:
        bazen_besed.append(vrstica.strip().upper())

def nova_igra():
    return Igra(random.choice(bazen_besed))
    
class Vislice:
    def __init__(self, datoteka_s_stanjem, datoteka_z_besedami="besede.txt"):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.datoteka_z_besedami = datoteka_z_besedami
    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        with open(self.datoteka_z_besedami, encoding='utf-8') as f:
            bazen_besed =[vrstica.strip().upper() for vrstica in f]
        igra = Igra(random.choice(bazen_besed))
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return id_igre
    
    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        igra, _ = self.igre[id_igre]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, poskus)
        self.zapisi_igre_v_datoteko()

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f:
            igre = json.load(f)
            self.igre = {int(id_igre): (Igra(geslo, crke), poskus) for id_igre, ((geslo, crke), poskus) in igre.items()}
        return

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:
            igre = {id_igre: ((igra.geslo, igra.crke), poskus) for id_igre, (igra, poskus) in self.igre.items()}
            json.dump(igre, f)
        return