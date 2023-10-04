import mysql.connector

# Conecta-se ao banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mestre",
    database="crud"
)

# Cria um cursor para executar consultas SQL
cursor = db.cursor()

class Usuario:
    def __init__(self, id=0, nome="Sem Nome", email="SemNome@SemEmail.com"):
        self.id = id
        self.nome = nome
        self.email = email

    def cadastrar_usuario(self, nome, email):
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
        db.commit()  

    
    @classmethod #Demostração de como se usa metodos de classe (estatico)
    def listar_usuarios(cls, usuario=None):
        if usuario:
            cursor.execute("SELECT id, nome, email FROM usuarios WHERE id=%s", (usuario.id,))
        else:
            cursor.execute("SELECT id, nome, email FROM usuarios")
        
        usuarios = []
        for (id, nome, email) in cursor:
            usuario = cls()
            usuario.id = id
            usuario.nome = nome
            usuario.email = email

            usuarios.append(usuario)
        return usuarios

    def atualizar_usuario(self, id, nome, email):
        usuario = self.encontrar_usuario(id)
        if usuario:
            usuario.email = email
            usuario.nome = nome

        cursor.execute("UPDATE usuarios SET nome=%s, email=%s WHERE id=%s", (nome, email, id))
        db.commit()  

    def deletar_usuario(self, id):
        cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
        db.commit()  
    
    def encontrar_usuario(self, id):
        cursor.execute("SELECT id, nome, email FROM usuarios WHERE id=%s", (id,))
        row = cursor.fetchone()
        if row:
            self.id, self.nome, self.email = row
            return self
        return None


class Produto:
    def __init__(self, id=0, nome="Sem Nome",descricao="Sem Descricao"):
        self.id = id
        self.nome = nome
        self.descricao = descricao
       

    def cadastrar_produto(self, nome, descricao):
        cursor.execute("INSERT INTO produtos (nome, descricao) VALUES (%s, %s, %s)", (nome, descricao))
        db.commit()  

    @classmethod #Demostrar como usar metodos de classe (estaticos)
    def listar_produtos(cls, usuario=None):
        cursor.execute("SELECT id, nome, descricao FROM produtos")

        produtos = []
        for (id, nome, descricao) in cursor:
            produto = cls(id, nome, descricao)
            produtos.append(produto)
        return produtos

    def atualizar_produto(self, id, nome, descricao):
        cursor.execute("UPDATE produtos SET nome=%s, descricao=%s WHERE id=%s", (nome, descricao, id))
        db.commit()  

    def deletar_produto(self, id):
        cursor.execute("DELETE FROM produtos WHERE id=%s", (id,))
        db.commit()  

    def encontrar_produto(self, id):
        cursor.execute("SELECT id, nome, descricao FROM produtos WHERE id=%s", (id,))
        row = cursor.fetchone()
        if row:
            id, nome, descricao= row
            return Produto(id, nome, descricao)
        return None

class ListaDesejos:
    def __init__(self, id=0, usuario_id=0, produto_id=0, quantidade=0):
        self.id = id
        self.usuario_id = usuario_id
        self.produto_id = produto_id
        self.quantidade = quantidade

    def cadastrar_item_lista_desejos(self, usuario_id, produto_id, quantidade):
        cursor.execute("INSERT INTO lista_desejos (usuario_id, produto_id, quantidade) VALUES (%s, %s, %s)",
                       (usuario_id, produto_id, quantidade))
        db.commit()  

    @classmethod
    def listar_itens_lista_desejos(cls, usuario_id=None):
        if usuario_id:
            cursor.execute("""
                SELECT ld.id AS id_desejo, ld.usuario_id, ld.produto_id, u.nome AS usuario_nome, p.nome AS produto_nome, ld.quantidade
                FROM lista_desejos ld
                JOIN usuarios u ON ld.usuario_id = u.id
                JOIN produtos p ON ld.produto_id = p.id
                WHERE ld.usuario_id=%s
            """, (usuario_id,))
        else:
            cursor.execute("""
                SELECT ld.id AS id_desejo, ld.usuario_id, ld.produto_id, u.nome AS usuario_nome, p.nome AS produto_nome, ld.quantidade
                FROM lista_desejos ld
                JOIN usuarios u ON ld.usuario_id = u.id
                JOIN produtos p ON ld.produto_id = p.id
            """)

        itens_lista_desejos = []
        for (id_desejo, usuario_id, produto_id, usuario_nome, produto_nome, quantidade) in cursor:
            item_lista_desejos = cls(id_desejo, usuario_id, produto_id, quantidade)
            item_lista_desejos.usuario_nome = usuario_nome  
            item_lista_desejos.produto_nome = produto_nome 

            itens_lista_desejos.append(item_lista_desejos)
        return itens_lista_desejos
    
    def atualizar_item_lista_desejos(self, id, usuario_id, produto_id, quantidade):
        cursor.execute("UPDATE lista_desejos SET usuario_id=%s, produto_id=%s, quantidade=%s WHERE id=%s",
                       (usuario_id, produto_id, quantidade, id))
        db.commit()  

    def deletar_item_lista_desejos(self, id):
        cursor.execute("DELETE FROM lista_desejos WHERE id=%s", (id,))
        db.commit()  

    def encontrar_item_lista_desejos(self, id):
        cursor.execute("SELECT id, usuario_id, produto_id, quantidade FROM lista_desejos WHERE id=%s", (id,))
        row = cursor.fetchone()
        if row:
            id, usuario_id, produto_id, quantidade = row
            return ListaDesejos(id, usuario_id, produto_id, quantidade)
        return None


# Função principal (Menu e interação com o usuário)
def main():
    try:
    
        while True:
            print("\n# Sistema de Cadastro de Lista de Desejos #\n")
            print("> Área do Usuário          > Lista de Desejos")
            print("  1. Cadastrar Usuário       10. Cadastrar Desejo")
            print("  2. Listar Usuário          11. Listar Desejos")
            print("  3. Atualizar Usuário       12. Atualizar Desejo")
            print("  4. Deletar Usuário         13. Deletar Desejo")
            print("----------------------")
            print("> Área do Administrador")
            print(" 101. Cadastrar Produto")
            print(" 102. Listar Produtos")
            print(" 103. Atualizar Produto")
            print(" 104. Deletar Produto")
            print(" 105. Listar Usuários")
            print("----------------------")
            print("000. Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == '1': # Cadastrar Usuário
                nome = input("Digite o nome do usuário: ")
                email = input("Digite o email do usuário: ")
                usuario = Usuario()
                usuario.cadastrar_usuario(nome, email)
                print("\nUsuário cadastrado com sucesso!")

            elif opcao == '2': # Listar Usuários
                usuario_id = int(input("Digite o ID do usuário: "))
                usuario = Usuario()
                usuario_e = usuario.encontrar_usuario(usuario_id)

                if usuario_e:
                    usuarios = Usuario.listar_usuarios(usuario_e)
                    for usuario in usuarios:
                        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")
                else:
                    print("\nUsuário não encontrado.")

            elif opcao == '3': # Atualizar Usuário
                id = int(input("Digite o ID do usuário que deseja atualizar: "))
                usuario = Usuario()
                usuario = usuario.encontrar_usuario(id)

                if usuario:
                    nome = input("Digite o novo nome: ")
                    email = input("Digite o novo email: ")
                    usuario.atualizar_usuario(id, nome, email)
                    print("\nUsuário atualizado com sucesso!")
                else:
                    print("\nUsuário não encontrado.")

            elif opcao == '4':  # Deletar Usuário
                id = int(input("Digite o ID do usuário que deseja deletar: "))
                usuario = Usuario()
                usuario = usuario.encontrar_usuario(id)
                
                if usuario:
                    usuario.deletar_usuario(id)
                    print("\nUsuário deletado com sucesso!")
                else:
                    print("\nUsuário não encontrado.")
        
            elif opcao == '10': # Cadastrar Desejo
                usuario_id = int(input("Digite o ID do usuário: "))
                produto_id = int(input("Digite o ID do produto: "))
                quantidade = int(input("Digite a quantidade desejada: "))
                
                usuario = Usuario().encontrar_usuario(usuario_id)
                produto = Produto().encontrar_produto(produto_id)
                
                if usuario and produto:
                    item = ListaDesejos()
                    item.cadastrar_item_lista_desejos(usuario_id, produto_id, quantidade)
                    print("\nDesejo cadastrado com sucesso!")
                else:
                    print("\nUsuário ou produto não encontrado.")
                    
            elif opcao == '11': # Listar Desejos
                # List wish list items
                usuario_id = int(input("Digite o ID do usuário: "))
                
               
                usuario = Usuario().encontrar_usuario(usuario_id)
                
                if usuario:
                    itens = ListaDesejos.listar_itens_lista_desejos(usuario_id)
                    if len(itens) > 0:
                        for item in itens:
                            print(f"ID Desejo: {item.id}, Produto: {item.produto_nome}, Quantidade: {item.quantidade}")
                    else:
                        print("\nNenhum desejo encontrado.")
                else:
                    print("\nUsuário não encontrado.")
                    
            elif opcao == '12': # Atualizar Desejo
                id_desejo = int(input("Digite o ID do desejo que deseja atualizar: "))
                usuario_id = int(input("Digite o novo ID do usuário: "))
                produto_id = int(input("Digite o novo ID do produto: "))
                quantidade = int(input("Digite a nova quantidade desejada: "))
                
                usuario = Usuario().encontrar_usuario(usuario_id)
                produto = Produto().encontrar_produto(produto_id)
                desejo = ListaDesejos().encontrar_item_lista_desejos(id_desejo)
                
                if usuario and produto and desejo:
                    item = ListaDesejos()
                    item.atualizar_item_lista_desejos(id_desejo, usuario_id, produto_id, quantidade)
                    print("\nDesejo atualizado com sucesso!")
                else:
                    print("\nUsuário, produto ou desejo não encontrado.")
                    
            elif opcao == '13': # Deletar Desejo
                id_desejo = int(input("Digite o ID do desejo que deseja deletar: "))
                item = ListaDesejos().encontrar_item_lista_desejos(id_desejo)
                
                if item:
                    ListaDesejos().deletar_item_lista_desejos(id_desejo)
                    print("\nDesejo deletado com sucesso!")
                else:
                    print("\nDesejo não encontrado.")
         
            elif opcao == '101': # Cadastrar Produto
                nome = input("Digite o nome do produto: ")
                descricao = input("Digite a descrição do produto: ")
                usuario_id = int(input("Digite o ID do usuário dono do produto: "))

                dono = Usuario()
                dono = dono.encontrar_usuario(usuario_id)

                if dono:
                    produto = Produto()
                    produto.cadastrar_produto(nome, descricao, dono.id)
                    print("\nProduto cadastrado com sucesso!")
                else:
                    print("\nUsuário não encontrado.")

            elif opcao == '102': # Listar Produtos
                produtos = Produto.listar_produtos()

                if len(produtos) > 0:
                    for produto in produtos:
                        print(f"ID: {produto.id}, Nome: {produto.nome}, Descrição: {produto.descricao}")
                else:
                    print("\nNenhum produto encontrado.")
                
            elif opcao == '103': # Atualizar Produto
                id = int(input("Digite o ID do produto que deseja atualizar: "))
                nome = input("Digite o novo nome: ")
                descricao = input("Digite a nova descrição: ")

                produto = Produto()
                produto.atualizar_produto(id, nome, descricao)
                print("\nProduto atualizado com sucesso!")

            elif opcao == '104': # Deletar Produto
                id = int(input("Digite o ID do produto que deseja deletar: "))
                produto = Produto()
                produto.deletar_produto(id)
                print("\nProduto deletado com sucesso!")
            
            elif opcao == '105': # Listar Usuários (Todos) por Produto
                usuarios = Usuario.listar_usuarios()
                if len(usuarios) > 0:
                    for usuario in usuarios:
                        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")
                else:
                    print("\nUsuários não encontrados.")

            elif opcao == '000': # Sair
                print("\nEncerrando o programa.")
                break
            else:
                print("\nOpção inválida. Tente novamente.")

    except Exception as e:
        print(f"Ocorreu um erro e a aplicação foi encerrada: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
