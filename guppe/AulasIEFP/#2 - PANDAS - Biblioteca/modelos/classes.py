import pandas as pd
class Dados:
    def __init__(self, dados):
        self._dados = pd.read_csv(dados, sep=';')

    @property
    def dados(self):
        return self._dados

    def ler_inicio(self, linhas=5):
        return self.dados.head(linhas)

    def ler_final(self, linhas=5):
        return self.dados.tail(linhas)

    def ler_tipo(self):
        return type(self.dados)
    
    def media_rendas(self, agrupador, valor_de_media):
        return self.dados.groupby(agrupador)[valor_de_media].mean().round(2)
    
    def porcentagem_tipo(self):
        return self.dados.Tipo.value_counts(normalize=True)
    
    def mostrar_valores_nulos(self):
        return self.dados.isnull().sum()
    
    def remover_valores_nulos(self, novo_valor):
        return self.dados.fillna(novo_valor, inplace=True)

    def encontrar_valores_zero(self):
        return self.dados.query('Quartos == 0 | Valor == 0 | Area == 0 | Condominio == 0')

    def remover_valores_0(self):
        registo_a_remover = self.dados.query('Quartos == 0 | Valor == 0 | Area == 0 | Condominio == 0').index
        return self.dados.drop(registo_a_remover, axis=0, inplace=True)
    
    def filtro_quarto(self, num_quartos):
        return self.dados['Quartos'] == num_quartos
    
    def filtro_aluguer(self, valor_aluguer):
        return self.dados['Valor'] < valor_aluguer
    
    def filtro_quarto_aluguel(self):
        filtro1 = self.dados['Quartos'] == 1
        filtro2 = self.dados['Valor'] < 500 
        filtro_composto = filtro1 & filtro2
        return self.dados[filtro_composto]
    

    def guardar(self, nome_arquivo, separador=';', metodo=None): 
        if metodo:
            df_para_guardar = metodo()
        else:
            df_para_guardar = self.dados

        # Correção na chamada ao método to_csv
        df_para_guardar.to_csv(nome_arquivo, sep=separador, encoding='UTF-8')
        print(f'{nome_arquivo} GUARDADO COM SUCESSO')

    def ler_valor_por_mes(self):
        self.dados['Despesas Mensais'] = (self.dados['Valor'] + self.dados['Condominio'])
        return self.dados

    def ler_valor_por_ano(self):
        self.dados['Despesas Por Ano'] = (self.dados['Valor'] + self.dados['Condominio']) * 12
        return self.dados 
