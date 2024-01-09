import datetime
import requests

# bibliotecas para conexao com o banco de dados
import psycopg2



# criar conexão com banco de dados postgres

conexao = psycopg2.connect(database = "meta",
                           host = "localhost",
                           user = "postgres",
                           password = "postgres",
                           port = "5432")

#print(conexao.info)
#print(conexao.status)

cursor = conexao.cursor()

# criar classes

        
class Departamento:
    def __init__(self, id, descricao_departamento, id_empresa):
        self.id = id
        self.descricao_departamento = descricao_departamento
        self.id_empresa = id_empresa
        
    def criar_departamento():
        novo_departamento = input()
        comando =f'INSERT INTO empresa ("{novo_departamento}")'
        cursor.execute(comando)
        conexao.commit() #edita banco de dados
    def salvar_departamento():
        pass
    def inativar_departamento():
        pass
    def editar_departamento():
        edita_departamento = input()
        comando =f'UPDATE empresa SET nome_empresa = ("{edita_departamento}")'
        cursor.execute(comando)
        conexao.commit() #edita banco de dados
        
class Colaborador:
    def __init__(self, id, nome, email, telefone, id_departamento, id_empresa ):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.id_departamento = id_departamento
        self.id_empresa = id_empresa
    
    def criar_colaborador():
        novo_colaborador = input()
        comando =f'INSERT INTO empresa ("{novo_colaborador}")'
        cursor.execute(comando)
        conexao.commit() #edita banco de dados
    def salvar_colaborador():
        pass
    def inativar_colaborador():
        pass
    def editar_colaborador():
        edita_colaborador = input()
        comando =f'UPDATE empresa SET nome_empresa = ("{edita_colaborador}")'
        cursor.execute(comando)
        conexao.commit() #edita banco de dados
        
class Indicador_kpi:
    def __init__(self, id, descricao_indicador_kpi, polaridade, unidade_medida, memoria_calculo, data_cadastro):
        self.id = id
        self.descricao_indicador_kpi = descricao_indicador_kpi
        self.unidade_medida = unidade_medida
        self.memoria_calculo = memoria_calculo
        self.data_cadastro = data_cadastro
    
    def criar_indicador_kpi():
        novo_indicador_kpi = input()
        comando =f'INSERT INTO empresa ("{novo_indicador_kpi}")'
        cursor.execute(comando)
        conexao.commit() #edita banco de dados
    def salvar_indicador_kpi():
        pass
    def inativar_indicador_kpi():
        pass
    def editar_indicador_kpi():
        edita_indicador_kpi = input()
        comando =f'UPDATE empresa SET nome_empresa = ("{edita_indicador_kpi}")'
        cursor.execute(comando)
        conexao.commit() #edita banco de dados

class Meta:
    def __init__(self, id, descricao_meta, id_indicador_kpi, id_colaborador, id_departamento, id_empresa, periodo, valor_meta, valor_real, valor_meta_acumulado, valor_real_acumulado, tipo_calculo_acumulado, percentual_atingimento, percentual_atingimento_acumulado):
        self.id = id
        self.descricao_meta = descricao_meta
        self.id_indicador_kpi = id_indicador_kpi
        self.id_colaborador = id_colaborador
        self.id_departamento = id_departamento
        self.id_empresa = id_empresa
        self.periodo = periodo
        self.valor_meta = valor_meta
        self.valor_real = valor_real
        self.valor_meta_acumulado = valor_meta_acumulado
        self.valor_real_acumulado = valor_real_acumulado
        self.percentual_atingimento = percentual_atingimento
        self.percentual_atingimento_acumulado = percentual_atingimento_acumulado
    
    def criar_meta():
        pass
    
    def salvar_meta():
        pass
    
    def editar_meta():
        pass
    
    def cancelar_meta():
        pass
    
    
            
        

        