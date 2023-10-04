# Sistema de Cadastro de Lista de Desejos

Este é um sistema de cadastro de lista de desejos simples desenvolvido em Python e MySQL. Ele permite que os usuários cadastrem-se, criem listas de desejos, cadastrem produtos e gerenciem suas listas de desejos.

## Requisitos

Para rodar o sistema, você precisará do Python instalado em seu ambiente e da biblioteca MySQL Connector/Python. Você também precisará de um servidor MySQL e dois arquivos SQL: "criarBD.sql" para criar a estrutura do banco de dados e "cargaInicialExemplo.sql" para carregar dados iniciais de exemplo.

## Instalação

1. Clone este repositório:
   
   git clone https://github.com/seu-usuario/sistema-lista-desejos.git

2. Instale a biblioteca MySQL Connector/Python:
   
   pip install mysql-connector-python

3. Importe a estrutura do banco de dados:
   
   mysql -u seu-usuario -p < criarBD.sql

   Insira sua senha quando solicitado.

4. Carregue dados iniciais de exemplo (OPCIONAL):

   mysql -u seu-usuario -p < cargaInicialExemplo.sql

   Insira sua senha quando solicitado.

5. Mude as configurações de conexão com Banco de dados no arquivo listadedesejos.py

  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="crud" )

## Uso

Para iniciar o sistema, execute o arquivo `listadedesejos.py`:

python listadedesejos.py

Siga as instruções no console para usar as funcionalidades do sistema.

## Funcionalidades

- Cadastro de Usuários
- Listagem de Usuários
- Atualização de Usuários
- Exclusão de Usuários
- Cadastro de Desejos
- Listagem de Desejos
- Atualização de Desejos
- Exclusão de Desejos
- Cadastro de Produtos (Administrador)
- Listagem de Produtos (Administrador)
- Atualização de Produtos (Administrador)
- Exclusão de Produtos (Administrador)
- Listagem de Usuários por Produto (Administrador)

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções de bugs. Abra uma "issue" para discutir as alterações que você deseja fazer.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
