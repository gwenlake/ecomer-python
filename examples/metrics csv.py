if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv(override=True)

import ecomer

start_date = "2023-12-02"
end_date   = "2023-12-04"


client = ecomer.Client()

for vessel in client.get_vessels():
    
   client.get_metrics(vessel["id"], start_date=start_date, end_date=end_date, save_format="csv")
