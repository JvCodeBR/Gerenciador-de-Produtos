import sqlite3, os
from tabulate import tabulate
from time import sleep

banco = sqlite3.connect('Loja.db')
cursor = banco.cursor()

cursor.execute('CREATE TABLE Produtos (SKU INTEGER PRIMARY KEY AUTOINCREMENT, Produto varchar(255), Estoque INTEGER, Valor float);')

def insert_product():
    os.system('cls')
    print('Incluir Produtos')
    print()
    product_name = str(input('Nome do produto: '))
    stock = int(input('Estoque do produto: '))
    price = float(input('Preço do produto: '))
    cursor.execute(f'INSERT INTO Produtos (Produto, Estoque, Valor) VALUES ("{product_name}", {stock}, {price});')
    banco.commit()
    print('Produto Incluido com Sucesso!')
    sleep(3)

def edit_product():
    os.system('cls')
    print('Edição de Produto')
    print()
    product_sku = int(input('Insira o SKU do produto a ser editado: '))
    os.system('cls')
    print(f'Editando o produto de SKU: {product_sku}')
    print()
    print('Selecione o dado a ser alterado:')
    print()
    print('1. Título')
    print('2. Estoque')
    print('3. Valor')
    print()
    print('0. Retornar')
    print()
    option = int(input('Selecione a opção: '))
    if option == 1:
        os.system('cls')
        new_product_name = str(input('Insira o novo título: '))
        cursor.execute(f'UPDATE Produtos SET Produto = "{new_product_name}" WHERE SKU = {product_sku};')
        banco.commit()
        print()
        print('Título alterado com sucesso!')
        sleep(2)
    elif option == 2:
        os.system('cls')
        new_product_stock = int(input('Insira o novo estoque: '))
        cursor.execute(f'UPDATE Produtos SET Estoque = "{new_product_stock}" WHERE SKU = {product_sku};')
        banco.commit()
        print()
        print('Estoque alterado com sucesso!')
        sleep(2)
    elif option == 3:
        os.system('cls')
        new_product_price = int(input('Insira o novo preço: '))
        cursor.execute(f'UPDATE Produtos SET Valor = "{new_product_price}" WHERE SKU = {product_sku};')
        banco.commit()
        print()
        print('Preço alterado com sucesso!')
        sleep(2)
    elif option == 0:
        pass

def show_products():
    os.system('cls')
    cursor.execute('SELECT * FROM Produtos')
    products = cursor.fetchall()
    print(tabulate(products, headers=['SKU', 'Produto', 'Estoque', 'Valor'], tablefmt='github'))
    print()
    input('Pressione qualquer tecla para voltar.')

def remove_product():
    os.system('cls')
    print('Excluir Produto')
    print()
    product_sku = int(input('Insira o SKU do produto: '))
    try:
        cursor.execute(f'DELETE FROM Produtos WHERE sku={product_sku};')
        banco.commit()
        os.system('cls')
        print('Produto removido com sucesso!')
        sleep(2)
    except:
        os.system('cls')
        print('Ocorreu algum erro!')
        print('Verifique se o SKU informado está cadastrado.')
        sleep(2)

while True:
    os.system('cls')
    print('Gerenciador de Produtos')
    print()
    print('1. Incluir Produtos')
    print('2. Excluir Produtos')
    print('3. Editar Produtos')
    print('4. Visualizar Produtos')
    print()
    print('0. Sair')
    print()
    try:
        resp = int(input('Insira a opção: '))
        if resp == 1:
            insert_product()
        elif resp == 2:
            remove_product()
        elif resp == 3:
            edit_product()
        elif resp == 4:
            show_products()
        elif resp == 0:
            break
    except:
        print()
        print('Insira uma opção válida!')
        sleep(2)

os.system('cls')
banco.close()