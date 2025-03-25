from flask import Flask, jsonify, request
from model.user import User
from model.twit import Twit

app = Flask(__name__)

# Временное хранилище твитов
twits = []

# Проверка работоспособности API
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})

# Создание твита
@app.route('/twit', methods=['POST'])
def create_twit():
    twit_json = request.get_json()

    if not twit_json or 'body' not in twit_json or 'author' not in twit_json:
        return jsonify({'error': 'Missing "body" or "author" in request'}), 400

    author = User(twit_json['author'])
    twit = Twit(twit_json['body'], author)
    twits.append(twit)
    return jsonify({'status': 'success'}), 201

# Получение списка всех твитов
@app.route('/twit', methods=['GET'])
def get_twits():
    return jsonify([twit.to_dict() for twit in twits]), 200

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
