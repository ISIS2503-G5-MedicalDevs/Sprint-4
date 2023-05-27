from ..models import IPS
from django.db import models

def get_IPSs():
    ips = IPS.objects.using('default').all()
    return ips

def get_IPS(IPS_pk):
    ips = IPS.objects.using('default').get(pk=IPS_pk)
    return ips

def create_IPS(Ips):
    ips = IPS(
        nombre = Ips["nombre"],
        direccion = Ips["direccion"],
        ciudad = Ips["ciudad"],
        capacidad = Ips["capacidad"]
    )
    ips.save(using='default')
    return ips

def update_IPS(Ips_pk, Ips):
    ips = get_IPS(Ips_pk)
    ips.nombre = Ips["nombre"]
    ips.direccion = Ips["direccion"]
    ips.ciudad = Ips["ciudad"]
    ips.capacidad = Ips["capacidad"]
    ips.save(using='default')
    return ips

def delete_IPS(Ips_pk):
    ips = get_IPS(Ips_pk)
    ips.delete()
    return ips
