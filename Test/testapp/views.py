import sys
import decimal
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
import json
from testapp.utils import create_new_shop, update_shop_data, distance_lat_long
from .models import *
from .serializers import *

# Create your views here.
class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return
    

class CreateUpdateShopAPI(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):

        response = {}
        response['status'] = 500
        try:
            
            data = request.data

            if not isinstance(data, dict):
                data = json.loads(data)
            # data = request.data
            shop_id = data.get('shop_id')
            name = data.get("name")
            owner = data.get("owner")
            try:
                lat = decimal.Decimal(data.get("latitude"))
                long = decimal.Decimal(data.get("longitude"))

            except:   
                response['status'] = 403
                response["message"] = "Please check the value entered for latitude and longitude. Please enter valid decimal range." 
                return Response(data=response) 

            if not name.strip():
                response['status'] = 403
                response["message"] = "Please enter valid name for shop." 
                return Response(data=response)
            
            if not owner.strip():
                response['status'] = 403
                response["message"] = "Please enter valid owner name for shop." 
                return Response(data=response)
            
            
            if lat < -90 or lat > 90:
                response['status'] = 403
                response["message"] = "Please enter valid latitude(Range -90 to 90)." 
                return Response(data=response)
            
            if long < -180 or  long > 180:
                response['status'] = 403
                response["message"] = "Please enter valid longitude(Range -180 to 180)." 
                return Response(data=response)

            response['status'] = 200
            if shop_id:
                shop_obj = Shop.objects.get(id=int(shop_id))
                successful = update_shop_data(data, shop_obj, ShopSerializer)
                if successful:
                    response["message"] = "The data for shop with shop_id: " + str(shop_id) + " has been updated."
                else:   
                    response["message"] = "Oops! An error occured while updating this shop. Please try after some time."
                    response['status'] = 500   
            else:
                shop_id = create_new_shop(data, ShopSerializer)
                if shop_id:
                    response["message"] = "A new shop has been created having shop_id: " + str(shop_id) + "."
                else:
                    response["message"] = "Oops! An error occured while creating new shop. Please try after some time."
                    response['status'] = 500    

            
            return Response(data=response)
        except Exception as e:  # noqa: F841
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("CreateUpdateShopAPI: %s at %s",
                         str(e), str(exc_tb.tb_lineno))
            response['status'] = 500
            response["message"] = "Internal server error!"

        return Response(data=response)


class DeleteShopAPI(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):

        response = {}
        response['status'] = 500
        try:
            
            data = request.data

            if not isinstance(data, dict):
                data = json.loads(data)
            # data = request.data
            shop_id = data.get('shop_id')
            Shop.objects.filter(id=int(shop_id)).delete()
            response["message"] = "Shop with shop_id: " + str(shop_id) + ", is deleted successfully!"
            response['status'] = 200
            return Response(data=response)

        except Exception as e:  # noqa: F841
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("DeleteShopAPI: %s at %s",
                         str(e), str(exc_tb.tb_lineno))
            
            response["message"] = "Internal server error!"

        return Response(data=response)   


class GetShopAPI(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):

        response = {}
        response['status'] = 500
        try:
            
            data = request.data

            if not isinstance(data, dict):
                data = json.loads(data)
            # data = request.data
            shop_id = data.get('shop_id')
            serialized_data = {}
            if shop_id:
                shop_obj = Shop.objects.filter(id=int(shop_id)).first()
                serializer = ShopSerializer(shop_obj)
            else:
                shop_objs = Shop.objects.all()
                serializer = ShopSerializer(shop_objs, many=True)

            serialized_data = serializer.data

            response["data"] = serialized_data
            response['status'] = 200
            return Response(data=response)

        except Exception as e:  # noqa: F841
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("GetShopAPI: %s at %s",
                         str(e), str(exc_tb.tb_lineno))
            
            response["message"] = "Internal server error!"

        return Response(data=response)
    

def ShopForm(request):  # noqa: N802
    try:
        

        return render(request, "testapp/shop_form.html", {
        })
        
    except Exception as e:  # noqa: F841
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Error ShopForm! %s %s",
                     str(e), str(exc_tb.tb_lineno))
        
        return HttpResponseNotFound()
    

def HomeShop(request):  # noqa: N802
    try:
        
        shop_objects = Shop.objects.all()
        return render(request, "testapp/home_shops.html", {
            "shops": shop_objects
        })
        
    except Exception as e:  # noqa: F841
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Error HomeShop! %s %s",
                     str(e), str(exc_tb.tb_lineno))
        
        return HttpResponseNotFound()    
    

class SubmitShopFormAPI(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):

        response = {}
        response['status'] = 500
        try:
            
            data = request.data

            if not isinstance(data, dict):
                data = json.loads(data)
            # data = request.data

            try:
                latitude = decimal.Decimal(data.get("latitude"))
                longitude = decimal.Decimal(data.get("longitude"))

            except:   
                response['status'] = 403
                response["message"] = "Please check the value entered for latitude and longitude. Please enter valid decimal range." 
                return Response(data=response) 
            
            if latitude < -90 or latitude > 90:
                response['status'] = 403
                response["message"] = "Please enter valid latitude(Range -90 to 90)." 
                return Response(data=response)
            
            if longitude < -180 or  longitude > 180:
                response['status'] = 403
                response["message"] = "Please enter valid longitude(Range -180 to 180)." 
                return Response(data=response)
            
            
            try:
                distance = decimal.Decimal(data.get('distance'))
            except:   
                response['status'] = 403
                response["message"] = "Please enter valid distance in km. It shoud be a number." 
                return Response(data=response) 
            
            if distance < 0:
                response['status'] = 403
                response["message"] = "Please enter valid distance(equal to or greater than 0)." 
                return Response(data=response)


            shop_objects = Shop.objects.all()
            shop_list = []
            for obj in shop_objects.iterator():
                obj_lat = obj.latitude
                obj_long = obj.longitude
                distance_in_km = distance_lat_long(latitude, longitude, obj_lat, obj_long)
                if distance_in_km != -1 and distance_in_km <= distance:
                    shop_list.append({"shop_id": obj.id, 
                                      "name": obj.name, 
                                      "owner": obj.owner,
                                      "latitude": obj_lat,
                                      "longitude": obj.longitude})

            response["data"] = shop_list
            response['status'] = 200
            return Response(data=response)

        except Exception as e:  # noqa: F841
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("SubmitShopFormAPI: %s at %s",
                         str(e), str(exc_tb.tb_lineno))
            
            response["message"] = "Internal server error!"

        return Response(data=response)
    

CreateUpdateShop = CreateUpdateShopAPI.as_view()
DeleteShop = DeleteShopAPI.as_view()
GetShop = GetShopAPI.as_view()    
SubmitShopForm = SubmitShopFormAPI.as_view()  


