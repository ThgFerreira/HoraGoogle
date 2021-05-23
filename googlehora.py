import requests
from bs4 import BeautifulSoup

googlehorasbusca = str(input("Digite o lugar que deseja saber a hora: "))
#googlehoras = 'https://www.google.com/search?q=que+horas+s%C3%A3o&oq=que+horas&aqs=chrome.1.69i57j0l9.5678j0j7&sourceid=chrome&ie=UTF-8'
googlehoras = 'https://www.google.com.br/search?q=hora+'


agent = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

resposta = requests.get(googlehoras + googlehorasbusca, headers=agent)

soup = BeautifulSoup(resposta.content, 'html.parser')

titulo = soup.find('h2', class_='Uo8X3b').get_text()

horaeminu = soup.find('div', class_='gsrt vk_bk dDoNo FzvWSb XcVN5d DjWnwf').get_text()

local = soup.find('span', class_='vk_gy vk_sh').get_text().strip()

HoraMinuSeparado = horaeminu.split(':')


horastr = HoraMinuSeparado[0]#horas

horafloat = float(horastr)

hora = int(float(horafloat))

minutostr = HoraMinuSeparado[1]#minutos

minutosfloat = float(minutostr)

minutos = int(float(minutosfloat))

#print(titulo, "Google")
#print(hora,'h', minutos,'m')
#print(local)


print(f"""
{titulo}, Google

{hora} horas e {minutos} minutos
    
{local}
    
    """)
