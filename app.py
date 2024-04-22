"""
Backend for setting up the chess UI and keeping track
of the chess position (fen)
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

    return jsonify({'msg': data})
