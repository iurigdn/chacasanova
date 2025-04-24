#!/usr/bin/env python3

import json
import os
import sys

def carregar_dados():
    """Carrega os dados do arquivo JSON."""
    try:
        with open('numeros.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Erro: Arquivo numeros.json não encontrado.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Erro: Arquivo numeros.json está corrompido.")
        sys.exit(1)

def salvar_dados(dados):
    """Salva os dados no arquivo JSON."""
    with open('numeros.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

def exibir_cartela(dados):
    """Exibe a cartela com os números disponíveis e escolhidos."""
    print("\n===== CARTELA DO CHÁ DE CASA NOVA =====")
    print("Números disponíveis: ⬜  |  Números escolhidos: ✅\n")
    
    # Exibe a cartela em formato de tabela 10x15
    for i in range(0, 150, 10):
        linha = ""
        for j in range(1, 11):
            num = i + j
            if num in dados["numeros_escolhidos"]:
                linha += f"✅{num:3d} "
            else:
                linha += f"⬜{num:3d} "
        print(linha)
    print()

def exibir_participantes(dados):
    """Exibe a lista de participantes e seus números escolhidos."""
    if not dados["participantes"]:
        print("Nenhum participante registrado ainda.")
        return
    
    print("\n===== PARTICIPANTES =====")
    for p in dados["participantes"]:
        print(f"Nome: {p['nome']} | Número: {p['numero']} | Contato: {p['contato']}")
    print()

def adicionar_participante(dados):
    """Adiciona um novo participante e marca o número como escolhido."""
    print("\n===== ADICIONAR PARTICIPANTE =====")
    
    # Exibe números disponíveis
    print("Números disponíveis:", sorted(dados["numeros_disponiveis"]))
    
    # Solicita o número
    while True:
        try:
            numero = int(input("Digite o número escolhido: "))
            if numero < 1 or numero > 150:
                print("Erro: O número deve estar entre 1 e 150.")
                continue
            if numero not in dados["numeros_disponiveis"]:
                print(f"Erro: O número {numero} já foi escolhido.")
                continue
            break
        except ValueError:
            print("Erro: Digite um número válido.")
    
    # Solicita informações do participante
    nome = input("Digite o nome do participante: ")
    contato = input("Digite o contato do participante: ")
    
    # Atualiza os dados
    dados["numeros_disponiveis"].remove(numero)
    dados["numeros_escolhidos"].append(numero)
    dados["participantes"].append({
        "nome": nome,
        "numero": numero,
        "contato": contato
    })
    
    # Salva os dados
    salvar_dados(dados)
    print(f"\nParticipante {nome} adicionado com sucesso com o número {numero}!")

def menu_principal():
    """Exibe o menu principal e processa a escolha do usuário."""
    while True:
        print("\n===== SISTEMA DE CONTROLE - CHÁ DE CASA NOVA =====")
        print("1. Visualizar cartela")
        print("2. Adicionar participante")
        print("3. Visualizar participantes")
        print("4. Sair")
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 1:
                dados = carregar_dados()
                exibir_cartela(dados)
            elif opcao == 2:
                dados = carregar_dados()
                adicionar_participante(dados)
            elif opcao == 3:
                dados = carregar_dados()
                exibir_participantes(dados)
            elif opcao == 4:
                print("\nObrigado por usar o Sistema de Controle do Chá de Casa Nova!")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")
        except ValueError:
            print("Erro: Digite um número válido.")

if __name__ == "__main__":
    # Verifica se está no diretório correto
    if not os.path.exists('numeros.json'):
        print("Erro: Execute este script no mesmo diretório que o arquivo numeros.json.")
        sys.exit(1)
    
    menu_principal()
