# Introdução de dados
import os
os.system('cls' if os.name == 'nt' else 'clear')# Limpa a tela do terminal para melhor visualização

# Programa para realizar uma pesquisa de opinião sobre um produto ou serviço
print("\n" + "=" * 30)
print("  PESQUISA DE OPINIÃO  ") 
print("=" * 30)


total_pessoas = int(input('Digite o número total de pessoas entrevistadas: '))

Excelente = 0
Bom = 0     
Ruim = 0

for i in range(total_pessoas): # estrutura de repetição para coletar os dados de cada pessoa
    print(f'Pessoa {i + 1}:')

    nome = input('Digite seu nome: ').strip().title() #title() para deixar a primeira letra maiúscula e o resto minúsculo
    idade = int(input('Digite sua idade: ').strip()) #strip() para remover espaços em branco no início e no final da string

    print("1 - Excelente")
    print("2 - Bom")
    print("3 - Ruim")

    # While dentro do for para garantir que o usuário digite uma opção válida
    while True: 
        voto = input('Escolha uma opção (1, 2 ou 3): ').strip().lower()
        print(f"{nome}, sua resposta foi registrada!") # teste para ver title() e lower() funcionando corretamente
    
        if voto == '1' or voto == 'excelente':
            Excelente += 1
            break
        elif voto == '2' or voto == 'bom':
            Bom += 1
            break
        elif voto == '3' or voto == 'ruim':
            Ruim += 1
            break   
        else:
            print('Opinião inválida. Por favor, digite "Excelente", "Bom" ou "Ruim".')
# Resultados    
print()
print("=" * 30) # Imprime uma linha de separação para melhor visualização
print('\nRESULTADO DA PESQUISA:')
print("=" * 30)

total = Excelente + Bom + Ruim
print(f'Excelente: {Excelente} ({(Excelente / total) * 100:.0f}%)')
print(f'Bom: {Bom} ({(Bom / total) * 100:.0f}%)')
print(f'Ruim: {Ruim} ({(Ruim / total) * 100:.0f}%)')
