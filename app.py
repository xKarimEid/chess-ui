"""
This is the backend for playing against a chess engine. Whenever the
user makes a move on the frontend, the backend makes a request to a 
chess engine available on "http://127.0.0.1:8080/make_random_move".
The response contains the new position after the chess engine makes 
its move. The new position is then returned to the frontend where 
it is displayed.
"""


from flask import Flask, render_template, send_from_directory, request
import requests


app = Flask(__name__)

@app.route('/')
def display_board():
    """
    Main entry function. Renders the index.html file
    which displays the chess board to the user.
    """

    return render_template('index.html')

@app.route('/img/chesspieces/wikipedia/<filename>')
def get_piece_image(filename):
    """Redirects frontend to correct folder containing piece images"""

    return send_from_directory('static/img/chesspieces/wikipedia/', filename)

@app.route('/make_move', methods = ['POST'])
def get_position():
    """
    This function is called from the front end after the user
    makes a move. The function extracts the current position
    from the request and sends it to the chess engine. The chess engine
    evaluates the position and gives back the new position after it makes
    its move. 
    """

    # Extract the current position
    fen = request.json['fen']

    # url for engine
    url = "http://127.0.0.1:8080/make_move"
    # Send a request to get the new position
    response = requests.post(url=url, json= {'fen': fen})
    # Extract the new position
    new_fen = response.json()['fen']

    return new_fen

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
