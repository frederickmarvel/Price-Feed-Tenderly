import requests
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

url = "https://api.tenderly.co/api/v1/account/frederickmarvel/project/hmx/simulate"
headers = {
    "X-Access-key": os.getenv("TENDERLY_ACCESS_KEY"),
}
data = {
    "network_id": "42161",
    "from": "0x0000000000000000000000000000000000000000",
    "to": "0x3963FfC9dff443c2A94f21b129D429891E32ec18",
    "input": "0xe245b5af0000000000000000000000000000000000000000000000000000000000000001",
    "gas": 1000000,
    "block_number": 175000000,
    "value": "0",
    "save": True,
    "save_if_fails": True,
    "simulation_type": "quick"
}

response = requests.post(url, headers=headers, json=data)

# Convert the response to JSON
response_data = response.json()

# Extract the output in hexadecimal
# output_hex = response_data['transaction']['transaction_info']['call_trace']['output']

# # Convert the output to decimal
# output_decimal = int(output_hex, 16)

# print(output_decimal)

# Save the response to a .txt file
with open("simulation_result.txt", "w") as file:
    file.write(json.dumps(response_data, indent=4))

print("Response saved to simulation_result.txt")
