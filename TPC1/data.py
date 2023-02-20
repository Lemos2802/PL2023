
import textwrap
from matplotlib import pyplot as plt
from valores import valores

class data:
	def __init__(self):
		
		with open("myheart.csv") as f:
			file = f.readlines()
			file.pop(0)
			self.dados = []
			for line in file:
				y = line.split(",")
				idade = int(y[0])
				sexo = y[1]
				tensao = int(y[2])
				colesterol = int(y[3])
				batimento = int (y[4])
				temDoenca = int(y[5])
				self.dados.append(valores(idade,sexo,tensao,colesterol,batimento,temDoenca))
			#for i in self.dados:
			#	print(i)
			
	def dist_sexo(self):
		
		male = 0
		female = 0

		for valor in self.dados:
			if valor.getTemDoenca() == 1 and valor.getSexo() == 'M':
				male += 1
			
			elif valor.getTemDoenca() == 1 and valor.getSexo() == 'F':
				female += 1

		return [(male,female)]
	
	def dist_ee(self):
		res = {}
		for i in self.dados:
			idade = i.getIdade() - (i.getIdade()%5)
			try:
				value = res[idade]
				res[idade] = value+1
			except:
				res[idade] = 1
		return sorted(res.items(), key=lambda x:x[0])
	
	def dist_nc(self):
		res = {}
		for i in self.dados:
			colesterol = i.getColesterol()-(i.getColesterol() % 10)
			try:
				value = res[colesterol]
				res[colesterol] = value+1
			except:
				res[colesterol] = 1
		return sorted(res.items(), key=lambda x:x[0])

def table(title, rows):
# calculate the maximum width of each column
	max_widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]

	# create the table title
	title_line = '+'.join('-' * (int(len(title)/2)+1) for i in range(len(rows[0])))
	title = textwrap.fill(title, 80)
	title = f"\n{title_line}\n|{title:^{sum(max_widths) + 4}}|\n{title_line}\n"

	# create the separator line
	sep = '+'.join('-' * (max_widths[i] + 2) for i in range(len(rows[0])))

	# create the table rows
	table = ''
	for row in rows:
		table += '\n' + '|'.join(textwrap.wrap(' | '.join(f"{r:<{max_widths[i]}}" for i, r in enumerate(row)), width=80))

	# print the table
	print(f"{title}{table}\n{sep}")

h = data()
dist_sexo = h.dist_sexo()
dist_ee = h.dist_ee()
dist_nc = h.dist_nc()
table("Distribuicao por sexo", dist_sexo)
y1 = ["Masculino", "Feminino"]
y2 = list(h.dist_sexo()[0])
plt.bar(y1, y2, color="red")
plt.xlabel("Género")
plt.ylabel("Número de pessoas com a doença")
plt.title("Distribuição da doença por Género")
plt.show()

table("Distribuicao por idade", dist_ee)
y1 = dict(dist_ee).keys()
y2 = dict(dist_ee).values()
plt.bar(y1, y2, color="red")
plt.xlabel("Faixa Etária (anos)")
plt.ylabel("Número de pessoas com a doença")
plt.title("Distribuição da doença por Idades")
plt.show()

table("Distribuicao por colesterol", dist_nc)
y1 = dict(dist_nc).keys()
y2 = dict(dist_nc).values()
plt.bar(y1, y2, color="red")
plt.xlabel("Nivel de colesterol")
plt.ylabel("Número de pessoas com a doença")
plt.title("Distribuição da doença por nivel de colesterol")
plt.show()


#print(i.dist_sexo())
#print(sorted(i.dist_ee().items(), key=lambda x:x[0]))
#print(sorted(i.dist_nc().items(), key=lambda x:x[0]))
