if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv(override=True)

import os
import ecomer

start_date = "2024-05-01T19:35:00"
end_date   = "2024-05-02T19:35:00"


client = ecomer.Client(os.getenv("ECOMER_API_KEY"))

for vessel in client.get_vessels():

    data = client.get_metrics(mmsi=vessel["id"], start_date=start_date, end_date=end_date)
    
    print(data)

