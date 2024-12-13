from shapely import Point

from django.db.models import F

# import unicodedata
# import unidecode


from location.constants import (
    SITY_LIST,
    COMUNITY_DATA,
    SHIRAKI_MARZ,
    DONT_AVELABLE,
    SERVICE_AVAILABLE_SPACE,
)
from location.models import Building

# from django.http import JsonResponse

# from django.core.serializers import serialize


# def _get_len_code_unicode(txt) -> dict:
#     """on input accepts str returns _lncode"""
#     unicodeName = unicodedata.name(txt[0])
#     if "ARMENIAN" in unicodeName:
#         return {"len_code": "_hy", "query": unidecode(txt)}
#     elif "CYRILLIC" in unicodeName:
#         return {"len_code": "_ru", "query": unidecode(txt)}
#     elif "LATIN" in unicodeName:
#         return {"len_code": "_en", "query": txt}
#     else:
#         return {"len_code": "_en", "query": unidecode(txt)}


class find_location:
    """ 
    կլասս որը մուտքում ընդունում է՝ lon, lat ->  կետի կորդինատները,ln_code ->  http հարցման 
    լեզվի կոդը։կլասը ունի երկու մեթոդ՝query_building, definit_adres 
    """
    def __init__(self, lon: str, lat: str, ln_code: str):
        """
        service_available_space -> այն տարացքն է որտեղ հասանելի է ծառայությունը։
        sity_list -> այն քաղաքների ցանքն է որտեղ հասանելի է ծառայությունը։
        community_data -> գյումրի քաղաքն է բաժանած թաղամասերի։
        dont_avelable -> 3 լեզվով հաղորդագրություն է այն մասին որ ծառայությունը հասանելի չէ։
        shiraki_marz -> 3 լեզվով Շիրակի մարզ 
        """
        self.lon = lon 
        self.lat = lat
        self.point = Point(self.lon, self.lat)
        self.ln_code = ln_code
        self.service_available_space = SERVICE_AVAILABLE_SPACE
        self.sity_list = SITY_LIST
        self.community_data = COMUNITY_DATA
        self.dont_avelable = DONT_AVELABLE
        self.shiraki_marz = SHIRAKI_MARZ
        self.lon_lat: str  = f"""{round(float(self.lat), 4)} {round(float(self.lon), 4)}"""

    def query_building(self, sity_pk: int, community_pk: float, rezult: dict):
        """
        մեթոդը մութքին ընդունում է՝
        sity_pk -> քաղաքի կամ գյուղի id-ին ըստ՝ Building տվյալների բազաի։
        community_pk -> քաղաքի կամ գյուղի թաղամասի id-ին ըստ՝ Building տվյալների բազաի։
        rezult -> քաղաքի կամ գյուղի անունն է http հարցման լեզվով։
        Մեթոդը հարցում է կատարում տվ․բազ։ Եթե կետը չի պատկանում տվյալ քաղաքի որևէ շինության՝
        այն հետ է վերադարցնում դիկտ՝ id = None,  search_rezult = քաղաքի կամ գյուղի անունը 
        գումարած կորդինատը, 
        lon_lat = կետի կերդինատը։
        Եթե կետին համապատասխան շինություն կա ապա id = շինության id-ին։ որից հետո ստուգում է թե արդյոք շինությունը ունի փողոցի անուն եթե այո ավելացնում է search_rezult -ին և ստուգում է արդյոք շինությունը ունի հասցե եթե այո search_rezult -ին ավելացնում է հասցեն, եթե հասցեն դատարկ է ավելացնում է փնտրվող կետի կորդինատը կորդինատը։   
        """
        pnt = f"POINT({self.lon} {self.lat})"
        data = {
                                'id': None,
                                "search_rezult": rezult + " " + self.lon_lat,
                                "lon_lat" : self.lat + ' ' + self.lon,
                                }
        obj = (
            Building.objects.select_related("stret")
            .filter(
                district=community_pk,
                sity_id=sity_pk,
                geometry__contains=pnt,
            )
            .values(
                build_id=F("id"),
                adr=F("adres"),
                street=F(f"stret__name_{self.ln_code}"),
                # geom=F("geometry"),
            )
        )
        if obj:
            obj_list = list(obj)[0]
            data['id'] = obj_list["build_id"]
            if obj_list["street"]:
                data["search_rezult"] = rezult + " " + obj_list["street"]
                if obj_list["adr"]:
                    data["search_rezult"] = data["search_rezult"] + " " + obj_list["adr"]
                else: data["search_rezult"] = data["search_rezult"] + " " + self.lon_lat 

        return data
    
    def definit_adres(self):
        """
        մեթոդը ստուգում է արդյոք նշված կետում ծառայությունը հասանելի է թէ ոչ եթե ծառայությունը հասանելի չէ հետ է վերադարցնում դիկտ՝ 
        id = None,  
        search_rezult = հաղորդագրություն այն մասին որ ծառայությունը հասանելի չէ, 
        lon_lat = None։

        եթե կետը պատկանում է հասանելի տարածքին ստուգում է արդյոք թե որ քաղաքին կամ գյուղին է պատքանում կետը եթե ոչ մի քաղաքի չի պատքանում հետ է վերադարցնում 
        id = None, 
        search_rezult = շիրակի մարզ + կետի կորդինատները,
        lon_lat = կետի կորդինատները

        Եթե կետը պատկանում է որևէ քաղաքի կամ գյուղի վերցնում է այդ քաղաքի id-ին և քաղաքի անունը այնուհետև ստուգում է որ թաղամասին է պատկանում կետը եթե որևէ տաղամասի պատկանում է վերցնում է այդ թաղամասի id-ն ստացված տվյալներով դիմում է query_building մեթոդին և հետ վերադարցնում մեթոդի տված դիքտը։
        """
        data = {
            'id': None,
            "search_rezult": None,
            "lon_lat": None,
        }
        status_code = 200
        if self.point.within(self.service_available_space):
            for sity in self.sity_list:
                if sity["geometry"].contains(self.point):
                    sity_pk = sity["id"]
                    rezult = sity["sity_" + self.ln_code]
                    community_pk = None
                    if sity_pk == 1:
                        for community in self.community_data:
                            if community["geometry"].contains(self.point):
                                community_pk = community["id"]
                                break
                    data = self.query_building(sity_pk=sity_pk, community_pk=community_pk, rezult= rezult)
                    return (data, status_code)
            
            data["search_rezult"] = self.shiraki_marz["shirak_" + self.ln_code]+ " " + self.lon_lat
            data["lon_lat"] = self.lat + ' ' + self.lon
            return (data, status_code)
        
        else:
            data["search_rezult"] = self.dont_avelable["sor_" + self.ln_code]
            # status_code = 503 # պետք է գտնել այնպիսի ստատւս կոդ որ js֊ը աշիբկա չտա։ 
        return (data, status_code)
