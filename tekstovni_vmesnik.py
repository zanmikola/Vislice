import model

def izpis_igre(igra):
    return '''stevilo preostalih poskusov: {}, do zdaj napacne crke: {}, pravilni del gesla: {}
    '''.format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napacnih(), igra.napacne_crke(), igra.pravilni_del_gesla())

def izpis_zmage(igra):
    return '''Čestitam uganil si {}'''.format(igra.geslo())

def izpis_poraza(igra):
    return '''Žal nisi ugotovil gesla {}'''.format(igra.geslo())

def zahtevaj_vnos(igra):
    return input('Vnesi črko: ')

def poženi_vmesnik():
    igra = model.nova_igra()
    