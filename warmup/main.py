import requests

IPSTACK_API_KEY = "Chave aqui"
OPENWEATHER_API_KEY = "#Chave aqui"

try:
    url_ipstack = f'http://api.ipstack.com/check?access_key={IPSTACK_API_KEY}'
    response = requests.get(url_ipstack, timeout=5)
    dados_ip = response.json()
    latitude = dados_ip.get('latitude')
    longitude = dados_ip.get('longitude')
    cidade = dados_ip.get('city')
    estado = dados_ip.get('region_code')

    url_weather = (
        f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}'
        f'&appid={OPENWEATHER_API_KEY}&units=metric&lang=pt_br'
    )
    resp_weather = requests.get(url_weather, timeout=5)
    dados_weather = resp_weather.json()
    temperatura = dados_weather.get('main', {}).get('temp')

    print(f'Localização atual: {cidade}, {estado}')
    if temperatura is not None:
        print(f'Temperatura atual: {temperatura}°C')
    else:
        print('Não foi possível obter a temperatura. Resposta da API:', dados_weather)

except Exception as e:
    print(f'Erro durante a consulta dos dados, por favor, tente novamente: {e}')
