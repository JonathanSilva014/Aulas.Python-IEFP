import pandas as pd
from classes import Dados

def main():
    # Usando barras invertidas simples
    base_de_dados = 'guppe/AulasIEFP/#2 - PANDAS - Biblioteca/modelos/imoveis.csv'

    analise = Dados(base_de_dados)

    print('_______________-LER TABELA COMPLETA-_______________')
    print(analise.dados)

    print('_______________-LER INICIO DA TABELA-_______________')
    print(analise.ler_inicio(10))

    print('_______________-LER FIM DA TABELA-_______________')
    print(analise.ler_final(10))

    print('_______________-LER TIPO DA TABELA-_______________')
    print(analise.ler_tipo())
    
    print('_______________-VER MÉDIA DE RENDAS POR TIPO DE IMÓVEL-_______________')
    print(analise.media_rendas(agrupador='Tipo', valor_de_media='Valor'))
    
    print('_______________-VER PORCENTAGEM POR TIPO DE IMOVEL-_______________')
    print(analise.porcentagem_tipo())
    
    print('_______________-MOSTRAR VALORES NULOS-_______________')
    print(analise.mostrar_valores_nulos().head(5))
    
    print('_______________-REMOVER VALORES NULOS-_______________')
    analise.remover_valores_nulos(0)  # Correção aqui, o método já modifica os dados inplace
    
    print('_______________-ENCONTRAR VALORES A ZERO-_______________')
    print(analise.encontrar_valores_zero())
    
    print("---------Encontrar valores a 0----------")
    print(analise.encontrar_valores_zero())
    
    print('_______________-filtro de QUARTOS-_______________')
    print(analise.filtro_quarto(2))  # Exemplo de filtro para 2 quartos
    
    print('_______________-ENCONTRAR VALORES A ZERO-_______________')
    print(analise.encontrar_valores_zero())
    
    analise.guardar(nome_arquivo='imoveis_novo.csv', separador=';')

if __name__ == '__main__':
    main()
