
from django.contrib.gis.geos import GEOSGeometry
import requests
from location.models import Street, Building, locationAvailable

api_kay = 'c16a69a1-0e05-4430-9854-7ba5d466f145'


def find_location(latitude, longitude, api_kay= api_kay):
    get_multipolygons_from_coordinates(latitude, longitude)
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={api_kay}&format=json&geocode={longitude},{latitude}"

    # Sending the HTTP request
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the JSON response
        data = response.json()
        
        # Extracting the address from the response
        # address = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
        
        return data
    else:
        print("Error:", response.status_code)
        return response.status_code




def get_multipolygons_from_coordinates(latitude, longitude, api_kay = api_kay):
    # Constructing the request URL with rspn=1 parameter
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={api_kay}&format=json&geocode={longitude},{latitude}&rspn=1"

    # Sending the HTTP request
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the JSON response
        data = response.json()

        # Extracting multipolygons from the response
        multipolygons = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
        print(multipolygons)
        return multipolygons
    else:
        print("Error:", response.status_code)
        return None
    



def get_building_polygons(latitude, longitude, radius=25):
    overpass_query = f"""
    [out:json];
    (
        way["building"](around:{radius},{latitude},{longitude});
        relation["building"](around:{radius},{latitude},{longitude});
    );
    out geom;
    """

    # Send the query to the Overpass API
    response = requests.post("https://overpass-api.de/api/interpreter", data=overpass_query)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None



def save_new_data(data):
    dat = []
    unic_street = {}
    sity = locationAvailable.objects.get(id = 4)
    for i in data['elements']:
        tag = i['tags']
        if 'addr:city' not in tag.keys():
            continue
        if 'addr:housenumber' not in  tag.keys():
            continue
        if 'addr:street' not in tag.keys():
            continue
        adres = tag['addr:housenumber']
        siity = tag['addr:city']
        street = tag['addr:street']
        if street not in unic_street.keys():
            stret= Street.objects.filter( name_hy = street)
            if stret.count() == 1:
                pass
            else: 
                stret = Street(name=street, name_hy = street, sity = sity)
                stret.save()

        loc = 'MULTIPOLYGON((('
        for cord in i['geometry']:
            loc = loc + f"""{cord['lon']} {cord['lat']}, """
        points = GEOSGeometry(loc[:-2] + ')))', srid = 4326)
        stret= Street.objects.get( name_hy = street)
        building =  Building(sity = sity, street = stret, adres = adres, area=points )
        building.save()




# def save_new_data(data):
#     dat = []
#     unic_street = []
#     for i in data['elements']:
#         tag = i['tags']
#         if 'addr:city' not in tag.keys():
#             continue
#         if 'addr:housenumber' not in  tag.keys():
#             continue
#         if 'addr:street' not in tag.keys():
#             continue
#         adres = tag['addr:housenumber']
#         sity = tag['addr:city']
#         street = tag['addr:street']
#         if street not in unic_street:
#             unic_street.append(street)
#         loc = 'MULTIPOLYGON((('
#         for cord in i['geometry']:
#             loc = loc + f"""{cord['lat']} {cord['lon']}, """
#         points = loc[:-2] + ')))'
#         dic = {'multipolidon':points, 'sity':sity, 'adres':adres, 'street':street}
#         dat.append(dic)
#     dat.append(unic_street)

#     print(dat)
