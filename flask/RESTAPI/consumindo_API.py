import requests


# # GET /hoteis
URL = 'http://127.0.0.1:5000'
resposta_hoteis = requests.request('GET', URL + '/hoteis')
print(resposta_hoteis.status_code)
hoteis = resposta_hoteis.json()
print(hoteis)
len(hoteis['hoteis'])
lista_hoteis = hoteis['hoteis']
for hotel in lista_hoteis:
    print(hotel['nome'])

# # Mercado Livre
ML_URL = 'https://api.mercadolibre.com/sites'
# ML_URL = 'https://api.mercadolibre.com/sites/MLB/categories'
lista_sites = requests.request('GET', ML_URL)
print(lista_sites)
print(lista_sites.json())

# # POST /cadastro
endpoint_cadastro = URL + '/cadastro'
print(endpoint_cadastro)
body_cadastro = {
    'login': 'danilo',
    'senha': 'abc123'
}
headers_cadastro = {
    'Content-Type': 'application/json'
}
resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=headers_cadastro)
print(resposta_cadastro.status_code)
resposta_cadastro.json()

# # /login
endpoint_login = URL + '/login'
print(endpoint_login)
body_login = {
    'login': 'danilo',
    'senha': 'abc123'
}
headers_login = {
    'Content-Type': 'application/json'
}
resposta_login = requests.request('POST', endpoint_login, json=body_login, headers=headers_login)
print(resposta_login.status_code)
token = resposta_login.json()
print(token['access_token'])

# # CRUD /hoteis/{hotel_id}
endpoint_hotel_id = URL + '/hoteis/meuhotel2'
print(endpoint_hotel_id)
body_hotel_id = {
    'nome': 'Meu Hotel Alterado',
    'estrelas': 4.8,
    'diaria': 398.90,
    'cidade': 'Santos'
}
headers_hotel_id = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token['access_token']
}
# resposta_hotel_id = requests.request('POST', endpoint_hotel_id, json=body_hotel_id, headers=headers_hotel_id)
# resposta_hotel_id = requests.request('PUT', endpoint_hotel_id, json=body_hotel_id, headers=headers_hotel_id)
resposta_hotel_id = requests.request('GET', endpoint_hotel_id)
# resposta_hotel_id = requests.request('DELETE', endpoint_hotel_id, headers=headers_hotel_id)
print(resposta_hotel_id)
resposta_hotel_id.json()

# # /usuarios/{user_id}
endpoint_user_id = URL + '/usuarios/1'
print(endpoint_user_id)
headers_user_id = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token['access_token']
}
resposta_user_id = requests.request('GET', endpoint_user_id)
# resposta_user_id = requests.request('DELETE', endpoint_user_id, headers=headers_user_id)
print(resposta_user_id.status_code)
resposta_user_id.json()
