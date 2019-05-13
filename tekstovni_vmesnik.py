from model import *

def izpis_igre():
    return '''stevilo preostalih poskusov: {}, do zdaj napacne crke: {}, pravilni del gesla: {}
    '''.format(STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napacnih(), igra.napacne_crke(), igra.pravilni_del_gesla())

def izpis_zmage():
    return '''Čestitam uganil si {}'''.format(igra.geslo())

def izpis_poraza():
    return '''Žal nisi ugotovil gesla {}'''.format(igra.geslo())