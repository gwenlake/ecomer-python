import os
import requests
from datetime import datetime, timedelta
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from typing import Any, Optional, List, Mapping, Type, Union, Iterable, Iterator, AsyncIterator
from tenacity import retry, stop_after_attempt, wait_random_exponential
import ecomer


API_URL = "https://api.ecomerdata.gwenlake.cloud/v1"
TIMEOUT = 60


class Client:

    def __init__(self, api_key: Optional[str] = None):
        self._api_key  = api_key or os.getenv("ECOMER_API_KEY")
        self._session  = requests.Session()
    
    @retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
    def fetch(self, query, params={}):
        url = f"{API_URL}/{query}"
        headers = { "Authorization": f"Bearer {self._api_key}" }
        response = self._session.get(url, headers=headers, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        if response.status_code != 200:
            raise Exception
        return response.json()

    def get_vessels(self):
        response = self.fetch(f"vessels")
        if "data" not in response:
            return None
        return response["data"]


    def get_metrics(self, mmsi: str, start_date: str, end_date: str, aggregate: str = "1m", save_format: str = None, fields: dict = {}):

        _start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S")
        _end_date   = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S")
        _days       = pd.date_range(_start_date, _end_date, freq='D').strftime("%Y-%m-%dT%H:%M:%S")

        data = []
        for _start_date in _days:
            _end_date = datetime.strptime(_start_date, "%Y-%m-%dT%H:%M:%S") + timedelta(days=1)
            _end_date = _end_date.strftime("%Y-%m-%dT%H:%M:%S")
            print(f"Downloading metrics for {mmsi}:", _start_date, "-", _end_date)
            params = dict(aggregate=aggregate, start_date=_start_date, end_date=_end_date)
            if fields:
                params["fields"] = fields
            response = self.fetch(f"vessels/{mmsi}/metrics", params=params)
            if "data" in response:
                data += response["data"]

        if len(data)==0:
            return None
        
        data = pd.DataFrame(data)
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        data.set_index('timestamp', inplace=True)

        if save_format == "csv":
            data.to_csv(f"ecomer metrics-{mmsi} from {start_date.replace(':','-')} to {end_date.replace(':','-')}.csv")

        elif save_format == "shp":
            geometry = [Point(xy) for xy in zip(data['longitude'], data['latitude'])]
            data = data.reset_index()
            data['timestamp'] = data['timestamp'].dt.strftime("%Y-%m-%d %H:%M:%S")
            gdf = gpd.GeoDataFrame(data, crs='EPSG:4326', geometry=geometry)
            gdf.to_file(f"ecomer metrics-{mmsi} from { start_date.replace(':','-') } to { end_date.replace(':','-') }.shp.zip")

        return data
