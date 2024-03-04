import geopandas as gpd
import numpy as np
from sqlalchemy import create_engine

def import_geojson_to_postgis(geojson_file, table_name, connection_string):
    gdf = gpd.read_file(geojson_file)
    gdf['center_point'] =  gdf.geometry.centroid
    gdf = gdf[['id', 'center_point', 'adres', 'geometry', 'sity_id', 'stret_id']]
    engine = create_engine(connection_string)
    gdf.to_postgis(table_name, engine, if_exists='append')

# Example connection string for PostgreSQL/PostGIS
connection_string = "postgresql://djangoapp:yourpass@localhost:5432/app"
import_geojson_to_postgis("new_build_gy.geojson", "location_building", connection_string)
