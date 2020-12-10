from flask import Flask, jsonify

app = Flask(__name__)

hello = [
    {
        'creator_name': 'adwaya',
        'version': '2.0',
        'species': 'humanoid',
        'entertainment': {
            'games': 'PUBG',
            'to-do': 'learning to think like a coder'
        }
    }
]

#GET /info
@app.route('/hello')
def get_info():
    return jsonify({'message': "hello world"})

app.run(host="0.0.0.0",port=8080,debug=True,use_reloader=True)
