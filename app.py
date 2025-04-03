from flask import Flask, request, jsonify, send_from_directory
import mysql.connector

app = Flask(__name__)

# Conexão com o banco de dados
def get_db_connection():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='123',
        database='gerenciador_tarefas'
    )
    return conn

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Funcionalidade 1: Adicionar Tarefa
@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa():
    descricao = request.json['descricao']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tarefas (descricao) VALUES (%s)', (descricao,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Tarefa adicionada com sucesso!'}), 201

# Funcionalidade 2: Marcar Tarefa como Concluída
@app.route('/concluir_tarefa/<int:id>', methods=['PUT'])
def concluir_tarefa(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tarefas SET concluida = TRUE WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Tarefa marcada como concluída!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
