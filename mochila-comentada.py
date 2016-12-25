#coding: utf-8

def mochila(val, pes, item, cap): #o problema
	if(item == 0 or cap == 0): #se não houver itens ou a capacidade da mochila for 0, nada é feito
		return 0 
	else:
		if(pes[item - 1] > cap): #se o peso da ultimo item da lista foi maior que a capacidade da mochila...
			return mochila(val, pes, item - 1, cap) #nada é feito e a função é chamada para o próximo item(no caso, o penúltimo)
		else: #se o peso do item for menor que a capacidade
			return max( #função padrão do python que retorna o maior valor entre dois parâmetros (A e B)
				val[item - 1] + mochila(val, pes, item - 1, cap - pes[item - 1]), 
				#A) Soma o valor do item atual, desconta seu peso e chama a função para o próximo item da lista
				mochila(val, pes, item-1, cap) 
				#B) Chama a função para o próximo item descartando o valor e peso do item atual. Voltamos à linha 29 com item - 1
			)

def defValores(val, pes): #declara função para coletar o valor e peso dos itens e capacidade da mochila
	quant = input("Insira a quantidade de itens: ",)
	print
	for j in range(2):
		if j == 0:
			for i in range(quant):
				print "Insira o valor do item ", i + 1, ": ",
				aux = input()
				val.append(aux) #joga o valor da variável auxiliar para a lista valor na posição i
			print
		else:
			for i in range(quant):
				print "Insira o peso do item ", i + 1, ": ",
				aux = input() 
				pes.append(aux) #joga o valor da variável auxiliar para a lista peso na posição i
			print

	cap = input("Insira a capacidade da mochila: ",) 
	print
	return cap #a função retorna a capacidade da mochila mesmo manipulando os valores dos vetores			
	
valor = [] #declara vetor/lista para os valores dos itens
peso = [] #declara vetor/lista para os pesos dos itens

#Exemplo:
	#Capacidade da mochila: 30;
	#Quantidade: 5;
   	#Valor: {20, 100, 50, 5, 30};
  	#Peso: {5, 19, 11, 1, 20};
 	
	#Resultado no melhor caso: 150

capacidade = defValores(valor, peso) #a função é chamada e capacidade recebe o valor retornado pela função(cap)
print "Valor máximo: ", mochila(valor, peso, len(valor), capacidade) #len(valor) é o comprimento do vetor


