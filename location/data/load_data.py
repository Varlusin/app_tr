import geopandas as gpd
import numpy as np
from sqlalchemy import create_engine

connection_string = "postgresql://djangoapp:yourpass@localhost:5432/app"

def import_geojson_to_postgis(geojson_file, table_name, connection_string, add_center_point = False):
    gdf = gpd.read_file(geojson_file)    
    gdf.set_crs(epsg=4326)    
    if add_center_point:
        gdf = gdf[['adres', 'sity_id', 'district',  'stret_id', 'id','geometry']]
        gdf['center_point'] =  gdf.geometry.centroid
        gdf['center_point'] = gdf['center_point'].set_crs(epsg=4326)
    engine = create_engine(connection_string)
    gdf.to_postgis(table_name, engine, if_exists='append')


def main():
    # import_geojson_to_postgis("location_available.geojson", "location_locationavailable", connection_string)
    # import_geojson_to_postgis("shirak_stret_final.geojson", "location_street", connection_string)
    import_geojson_to_postgis("shirak_build_final.geojson", "location_building", connection_string, add_center_point=True)

if __name__ == "__main__":
    main()