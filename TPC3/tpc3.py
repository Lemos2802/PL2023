import os
import re
import json


def parser():
	
	with open("processos.txt") as file:

		estrutura = re.compile(r'^(?P<pasta>[0-9]+)::(?P<data>\d{4}-\d{2}-\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<pai>[a-zA-Z ]+)?::(?P<mae>[a-zA-Z ,]+)?::(?P<observacoes>.+)[:]+$')
		lista = []
		verificacao = None

		lines = file.readlines()
		for line in lines:
			x = estrutura.match(line)
			if x:
				chave = (x.group(3), x.group(4)) # faço uma lista que contem tuplos(nome,pai) e se outra linha tiver o mesmo nome e pai não será adicionada pois é linha repetida 

				if chave != verificacao:
					lista.append(x.groupdict())
					verificacao = chave
	
	return lista
			

def freqAno(lista):
	datas = dict()
	for dic in lista:
		ano = dic["data"].split("-")[0]
		if ano in datas.keys():
			datas[ano] += 1
		else:
			datas[ano] = 1
	
	return dict(sorted(datas.items(), key=lambda x:x[0]))

def calcula_sec(data):
	if data[2] == '0' and data[3] == '0':
		return data[:2]
	else: 
		return str(int(data[:2])+1)
	

def freqNome(lista):
	names = dict()
	apelidos = dict()
	i = 0

	for dic in lista:
		nome_completo = dic["nome"].split(" ")
		nome = nome_completo[0]
		apelido = nome_completo[-1]
		
		ano = dic['data'].split("-")[0]
		sec = calcula_sec(ano)
		
		if sec not in names:
			names[sec] = {}

		if sec not in apelidos:
			apelidos[sec] = {}

		if nome in names[sec].keys():
			names[sec][nome] += 1
			
		else:
			names[sec][nome] = 1

		if apelido in apelidos[sec].keys():
			apelidos[sec][apelido] += 1
		else:
			apelidos[sec][apelido] = 1

	dic_nome_org = dict(sorted(names.items(), key=lambda x: x[0]))
	dic_apel_org = dict(sorted(names.items(), key=lambda x: x[0]))


	for sec in dic_nome_org.keys():
		nomes_sec = names[sec]
		nomes_ordenados = sorted(nomes_sec.items(), key=lambda x: x[1], reverse=True)
		dic_nome_org[sec] = dict(nomes_ordenados[:5])

	
	for sec in dic_apel_org.keys():
		apelidos_sec = apelidos[sec]
		apelidos_ordenados = sorted(apelidos_sec.items(), key=lambda x: x[1], reverse=True)
		dic_apel_org[sec] = dict(apelidos_ordenados[:5])

		

	return dic_nome_org,dic_apel_org

def relacoes(lista):
	lista_relacoes = list()
	dict_final = {}
	regex = re.compile(r"[a-z],([A-Z][a-zA-Z ]*?)\.\s(?=Proc)") ##r"[a-z],([A-Z][a-zA-Z ]*?)\.
	for dic in lista:
		lista_relacoes += regex.findall(dic["observacoes"])

	for relacao in lista_relacoes:
		if relacao in dict_final.keys():
			dict_final[relacao] += 1
		else:
			dict_final[relacao] = 1

	return dict_final

def dic_json(lista):

	lista_aux = lista[:20]
	with open("dict.json","w+") as file:
		json.dump(lista_aux, file,indent=' ')
				

def main():
	dic = parser()
	freq_ano = freqAno(dic)
	freq_nome,freq_apelido = freqNome(dic)
	exec3 = relacoes(dic)
	print(freq_apelido)
	os.system('clear')
	
	while True:
		print("---------Deseja visualizar qual dos exercicios---------")
		print("1 - Frequência de processos por ano" )
		print("2a - Frequência de Nomes próprios ou Apelidos" )
		print("2b - Frequência de Apelidos")
		print("3 - Frequêcia dos tipos de relações" )
		print("4 - Converter os 20 primeiros registos em um ficheiro json" )
		string = input()
		os.system('clear')
		match string:
			case "1":
				print(json.dumps(freq_ano,indent=' '))
			case "2a":
				print(json.dumps(freq_nome,indent=' '))
			case "2b":
				print(json.dumps(freq_apelido,indent=' '))
			case "3":
				print(json.dumps(exec3,indent =' '))
			case "4":
				dic_json(dic)
			case "q":
				break
		
	
	


if __name__ == "__main__":
	main()

		
	


