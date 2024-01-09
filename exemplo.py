import psycopg2


class Empresa:

    id = None
    nome_empresa = None

    
    def salvar_empresa(self, cursor):
        
        cursor.execute("""
                       INSERT INTO empresa (empr_id, empr_nome) values (%s, %s);
                       """,
                       (self.id, self.nome_empresa))
        
        

def main():
    ########### SCRIPT PARA CRIA A TABELA EMPRESA ############
    # CREATE TABLE empresa (empr_id int, empr_nome varchar); #
    ##########################################################
    conexao = psycopg2.connect(database = "meta", host = "localhost", user = "postgres", password = "postgres", port = "5432")
    cursor = conexao.cursor()
    
    
    nome_empresa = input("Insiria o nome da sua empresa: \n") # Pego input do meu usario
    print(f"Sua empresa sera salva com esse nome [ {nome_empresa} ]")

    cursor.execute("""
                   SELECT count(*) FROM empresa;
                   """)
    
    qtd_empr = cursor.fetchone()[0] # Pego a quantidade de empresas que tenho para usar de ID
    
    empresa = Empresa() # Crio uma instancia da minha class Empreas
    empresa.id = qtd_empr + 1
    empresa.nome_empresa = nome_empresa # Defino o nome da empresa sendo o nome que o usuario deu o input
    empresa.salvar_empresa(cursor) # salvo a empresa

    cursor.close()
    conexao.commit()
    conexao.close()



if __name__ == "__main__":
    main()
    