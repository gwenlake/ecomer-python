if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv(override=True)

import pandas as pd
import matplotlib.pyplot as plt
import ecomer

start_date = "2023-12-02"
end_date   = "2023-12-03"


client = ecomer.Client()

vessels = client.get_vessels()
data = client.get_metrics(vessels[0]["id"], start_date=start_date, end_date=end_date)
print(data)


# plots
plt.plot(data.index, data['me_stb_fuel_consumption_rate'], label='me_stb_fuel_consumption_rate')
plt.plot(data.index, data['me_ps_fuel_consumption_rate'], label='me_ps_fuel_consumption_rate')
plt.title('Motor Consumption LPH (1 and 2)', fontsize=14)
plt.show()
