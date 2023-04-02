import sys
from math import radians, sin, cos, sqrt, atan2


def distance_lat_long(lat1, lon1, lat2, lon2):
    try:
        # convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        km = 6371 * c

        return km
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("distance_lat_long Failed: %s at %s",
                     str(e), str(exc_tb.tb_lineno))

        return -1


def create_new_shop(data, ShopSerializer):
    try:
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer = serializer.save()

        return serializer.id
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("create_new_shop Failed: %s at %s",
                     str(e), str(exc_tb.tb_lineno))

        return 0
    

def update_shop_data(data, shop_obj, ShopSerializer):
    try:
        serializer = ShopSerializer(shop_obj, data=data)
        
        if serializer.is_valid():
            serializer.save()
        else:
            print("invalid serializer")   
            print(serializer.errors) 
            return False

        return True    

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("create_new_shop Failed: %s at %s",
                     str(e), str(exc_tb.tb_lineno))
        
        return False 
 