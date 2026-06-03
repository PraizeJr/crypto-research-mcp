import requests

BASE_URL = "https://api.llama.fi"

def get_top_protocols_by_tvl(limit=10):
    response = requests.get(
        f"{BASE_URL}/protocols"
    )

    data = response.json()

    sorted_protocols = sorted(
        data,
        key=lambda x: x["tvl"],
        reverse=True
    )

    return sorted_protocols[:limit]

#Protocol Info
def get_protocol_info(protocol_name):
    response = requests.get(
        f"{BASE_URL}/protocol/{protocol_name}"
    )

    return response.json()

#Chains
def get_top_chains(limit=10):
    response = requests.get(
        f"{BASE_URL}/chains"
    )

    data = response.json()

    sorted_chains = sorted(
        data,
        key=lambda x: x["tvl"],
        reverse=True
    )

    return sorted_chains[:limit]
