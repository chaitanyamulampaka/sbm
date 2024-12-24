
import random
import string
import requests

def generate_otp(length=6):
    """Generate a random alphanumeric OTP of the given length."""
    characters = string.digits
    otp = ''.join(random.choices(characters, k=length))
    return otp



def get_location_details(pincode):
    url = f"https://india-pincode-with-latitude-and-longitude.p.rapidapi.com/api/v1/pincode/{pincode}"
    headers = {
        "x-rapidapi-key": "7f922b6bf9mshe7c282b3794176fp1a3b12jsnaff16c3ee68e",
        "x-rapidapi-host": "india-pincode-with-latitude-and-longitude.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        city = data.get('City', None)
        state = data.get('State', None)
        return city, state
    else:
        return None, None

