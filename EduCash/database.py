import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",  
            user="root",  
            password="bellasz13", 
            database="educash"
        )
        if conn.is_connected():
            print("Conexão ao banco de dados realizada com sucesso!")
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def criar_usuario(nome, email, senha):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO cadastro (nome, email, senha) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, email, senha))
            conn.commit()
            print("Usuário cadastrado com sucesso!")
            return cursor.lastrowid 
        except Error as e:
            raise Exception(f"Erro ao criar usuário: {e}")
        finally:
            cursor.close()
            conn.close()
    
def verificar_usuario(nome, senha):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        try:
            sql = "SELECT id FROM cadastro WHERE nome = %s AND senha = %s"
            cursor.execute(sql, (nome, senha))
            resultado = cursor.fetchone()
            return resultado is not None  
        except Error as e:
            raise Exception(f"Erro ao verificar usuário: {e}")
        finally:
            cursor.close()
            conn.close()

def adicionar_dados_extra(usuario_id, telefone, data_nascimento):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO extra (usuario_id, telefone, data_nascimento) VALUES (%s, %s, %s)"
            cursor.execute(sql, (usuario_id, telefone, data_nascimento))
            conn.commit()
            print("Dados extras adicionados com sucesso!")
        except Error as e:
            raise Exception(f"Erro ao adicionar dados extras: {e}")
        finally:
            cursor.close()
            conn.close()

def buscar_dados_extra(usuario_id):
    conn = conectar()
    if conn:
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT * FROM extra WHERE usuario_id = %s"
            cursor.execute(sql, (usuario_id,))
            return cursor.fetchall()  
        except Error as e:
            raise Exception(f"Erro ao buscar dados extras: {e}")
        finally:
            cursor.close()
            conn.close()