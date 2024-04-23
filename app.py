"""
Backend for setting up the chess UI and keeping track
of the chess position (fen)

To do:
Add chess engine abililty to play random moves when the user makes his/her move
If chess engine finds a response from /trained_model then get moves from there
else get moves from /random_move

"""

from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

@app.route('/')
def display_board():
    """
    Main entry function
    """

    return render_template('index.html')

@app.route('/img/chesspieces/wikipedia/<filename>')
def get_piece_image(filename):
    """Redirect to correct folder containing piece images"""

    return send_from_directory('static/img/chesspieces/wikipedia/', filename)

@app.route('/post_position', methods = ['POST'])
def submit_position():
    """
    API endpoint for receiving the fen position
    This endpoint gets called by the front-end whenever the user
    makes a move
    """

    data = request.json['fen']

    position = get_move()
    fen = position['fen']

    #print("new_position: ", new_position.data)

    return jsonify({'msg': fen}), 200

@app.route('/get_move')
def get_move():
    """
    For a given fen position returns the engine's move
    If there is no engine, returns a random move
    """
    print("in get move")
    #fen = request.json['fen']
    outcome = "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"
    return {'fen': outcome}
