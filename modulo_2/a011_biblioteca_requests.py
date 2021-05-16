import requests

meus_cookies = {'Última-visita': '05-03-2021'}

requisicao = requests.get('https://musicbrainz.org/ws/2/release?artist=65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab&status=bootleg&type=live',
cookies=meus_cookies)
print(requisicao.status_code)