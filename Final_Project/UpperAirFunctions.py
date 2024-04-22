from siphon.simplewebservice.iastate import IAStateUpperAir
from metpy.io import add_station_lat_lon
import datetime
import pandas



def get_raobs(dt: datetime.datetime) -> pandas.DataFrame:
    data = IAStateUpperAir().request_all_data(dt)
    data = add_station_lat_lon(data)
    return (data)



def select_press(data: pandas.DataFrame, press_lev) -> pandas.DataFrame:
   
    data = data.loc[data.pressure == press_lev]
    return (data)

