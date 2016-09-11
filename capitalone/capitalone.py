# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


import requests
import json

if __name__ == "__main__":
    argument1 = 'enterprise'
    argument2 = 'customers'
    apiKey = '4b868eb987258f2407ad8b80b58a1072'
    url = 'http://api.reimaginebanking.com/{}/{}?key={}'.format(argument1, argument2, apiKey)
    print(url)
    payload = {}
    # Create a Savings Account
    response = requests.get(
        url, 
        headers={'content-type':'application/json'},
    )
    print(response.text)

    if response.status_code == 200:
        print('account created')
