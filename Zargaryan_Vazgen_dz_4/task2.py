from requests import get

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
content = response.content.decode(encoding=response.encoding)

def currency_rates(country_code):
# Поиск валют
    values = []
    for el in content.split('<Value>')[1:]:
        val = el.split('</Value')[0]
        values.append(val)
# Поиск стран
    char_code = []
    for el in content.split('<CharCode>')[1:]:
        code = el.split('</CharCode>')[0]
        char_code.append(code)
    valute = dict(zip(char_code,values)) # объединение страны и соотношение рубля к их валюте (в словарь)

    for k,v in valute.items():
        if k == country_code:
            print(k,v)
        else:
            None
if __name__ == '__main__':

    currency_rates('USD')
