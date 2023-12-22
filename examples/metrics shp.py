if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv(override=True)

import ecomer

start_date = "2023-04-01"
end_date   = "2023-10-01"
fields     = "timestamp,latitude,longitude"


client = ecomer.Client()

for vessel in client.get_vessels():
    
   client.get_metrics(vessel["id"], start_date=start_date, end_date=end_date, fields=fields, save_format="shp")
