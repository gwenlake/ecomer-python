# Ecomer Python Library

The Ecomer Python library provides convenient access to the Ecomer API
from applications written in the Python language.


## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install -U git+https://github.com/gwenlake/ecomer-python
```

## Usage

The library needs to be configured with your account's secret key. 

```python
import ecomer

# initialize client
client = ecomer.Client(api_key=os.getenv("ECOMER_API_KEY"))

# get vessels
vessels = client.get_vessels()
print(vessels)

# get metrics
data = client.get_metrics(vessels[0]["id"], start_date="2024-05-01T00:00:00", end_date="2024-05-02T00:00:00")
print(data)

# get metrics and save in CSV format
data = client.get_metrics(vessels[0]["id"], start_date="2024-05-01T00:00:00", end_date="2024-05-02T00:00:00", save_format="csv")
print(data)

# get metrics and save in SHP format
data = client.get_metrics(vessels[0]["id"], start_date="2024-05-01T00:00:00", end_date="2024-05-02T00:00:00", save_format="shp")
print(data)

```

