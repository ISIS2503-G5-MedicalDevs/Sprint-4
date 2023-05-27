from pymongo import MongoClient, ReturnDocument
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from bson.objectid import ObjectId
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import json
from django.conf import settings
from django.contrib.auth.decorators import login_required
from widmy_Project.auth0backend import getRole
import widmy_Project.validate as vl

rolesValidos = ["Administrador", "AdministradorSistema"]

@api_view(["GET","POST"])
@login_required
def IPSs_view(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.ips_db
    IPS = db['IPS']
    if request.method == 'GET':
        role = getRole(request)
        if role in rolesValidos:
            result = []
            data = IPS.find({})
            for dto in data:
                jsonData = {
                "id" : str(dto['_id']),
                "nombre": dto['nombre'],
                "direccion": dto['direccion'],
                "ciudad" : dto['ciudad'],
                "capacidad" : dto['capacidad']
                }
                result.append(jsonData)
            client.close()
            return JsonResponse(result, safe = False)
        else:
            return HttpResponse("Unauthorized User")
    
    elif request.method == 'POST':
        role = getRole(request)
        if role in rolesValidos:
            data = JSONParser().parse(request)
            result = IPS.insert(data)
            respo = {
                "MongoObjectID" : str(result),
                "Message" : "IPS registrada de forma exitosa"
                }
            client.close()
            return JsonResponse(respo, safe = False)
        else:
            return HttpResponse("Unauthorized User")


@login_required
@api_view(["GET","PUT"])
def IPS_view(request, pk):
    role = getRole(request)
    if role in rolesValidos:
        client = MongoClient(settings.MONGO_CLI)
        db = client.ips_db
        IPS = db['IPS']
        if request.method == 'GET':
            data = IPS.find({'_id':ObjectId(pk)})
            result = []
            for dto in data:
                jsonData = {
                    "id" : str(dto['_id']),
                    "nombre": dto['nombre'],
                    "direccion": dto['direccion'],
                    "ciudad" : dto['ciudad'],
                    "capacidad" : dto['capacidad']
                }
                result.append(jsonData)
            client.close()
            return JsonResponse(result[0], safe = False)
        
        if request.method == 'PUT':
            if not(vl.validar(json.loads(request.body))):
                return HttpResponseBadRequest(HttpResponse("Error, invalid entry for update"))
            newValues = json.loasd(request.body)
            respo = IPS.find_one_and_update({'_id': ObjectId(pk)}, {'$set': newValues }, return_document = ReturnDocument.AFTER)
            return JsonResponse(respo, safe = False)
    else:
        return HttpResponse("Unauthorized User")



@api_view(["POST","PUT"])
def IPS_test(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.ips_db
    IPS = db['IPS']
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = IPS.insert(data)
        respo = {
            "MongoObjectID" : str(result),
            "Message" : "IPS registrada de forma exitosa"
            }
        client.close()
        return JsonResponse(respo, safe = False)
    if request.method == 'PUT':
        if not(vl.validar(json.loads(request.body))):
                return HttpResponseBadRequest(HttpResponse("Error, invalid entry for update"))
        newValues = json.loasd(request.body)
        #TODO: Poner el id de la primera IPS que se termine creando aqui
        respo = IPS.find_one_and_update({'_id': ObjectId('Cambiar')}, {'$set': newValues }, return_document = ReturnDocument.AFTER)
        return JsonResponse(respo, safe = False)




#Funcion para comparar con la entrada y salida
@api_view(["PUT"])
def IPS_test2(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.ips_db
    IPS = db['IPS']
    newValues = json.loasd(request.body)
    #TODO: Poner el id de la primera IPS que se termine creando aqui
    respo = IPS.find_one_and_update({'_id': ObjectId('Cambiar')}, {'$set': newValues }, return_document = ReturnDocument.AFTER)
    return JsonResponse(respo, safe = False)