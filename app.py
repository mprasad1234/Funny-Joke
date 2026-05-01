from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

# Collection of funny jokes
jokes = [
    {
        "setup": "Why don't scientists trust atoms?",
        "punchline": "Because they make up everything!"
    },
    {
        "setup": "What do you call a bear with no teeth?",
        "punchline": "A gummy bear!"
    },
    {
        "setup": "Why did the scarecrow win an award?",
        "punchline": "Because he was outstanding in his field!"
    },
    {
        "setup": "What do you call a fake noodle?",
        "punchline": "An impasta!"
    },
    {
        "setup": "Why don't eggs tell jokes?",
        "punchline": "They'd crack each other up!"
    },
    {
        "setup": "What do you call a sleeping bull?",
        "punchline": "A bulldozer!"
    },
    {
        "setup": "Why did the math book look so sad?",
        "punchline": "Because it had too many problems!"
    },
    {
        "setup": "What do you call a fish wearing a bowtie?",
        "punchline": "So-fish-ticated!"
    },
    {
        "setup": "Why did the coffee file a police report?",
        "punchline": "It got mugged!"
    },
    {
        "setup": "What do you call a pig that does karate?",
        "punchline": "A pork chop!"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/random-joke')
def random_joke():
    """Return a random joke"""
    joke = random.choice(jokes)
    return jsonify(joke)

@app.route('/api/joke/<int:joke_id>')
def get_joke(joke_id):
    """Get a specific joke by ID"""
    if 0 <= joke_id < len(jokes):
        return jsonify(jokes[joke_id])
    return jsonify({"error": "Joke not found"}), 404

@app.route('/api/categories')
def categories():
    """Return joke categories (just for fun)"""
    categories = {
        "science": 1,
        "animals": 2,
        "food": 3,
        "punny": 4
    }
    return jsonify(categories)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
