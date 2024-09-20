if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv(override=True)

import os
import pandas as pd
import matplotlib.pyplot as plt
import ecomer

start_date = "2024-05-01T19:35:00"
end_date   = "2024-05-02T19:35:00"

client = ecomer.Client(os.getenv("ECOMER_API_KEY"))

vessels = client.get_vessels()
data = client.get_metrics(vessels[0]["id"], start_date=start_date, end_date=end_date)
print(data)


# plots
plt.plot(data.index, data['me_stb_fuel_consumption_rate'], label='me_stb_fuel_consumption_rate')
plt.plot(data.index, data['me_ps_fuel_consumption_rate'], label='me_ps_fuel_consumption_rate')
plt.title('Motor Consumption LPH (1 and 2)', fontsize=14)
plt.show()
