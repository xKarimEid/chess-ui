from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

@app.route('/')
def display_board():
    """
    Main entry function
    """
    return render_template('index.html')

@app.route('/img/chesspieces/wikipedia/<filename>')
def get_piece_image(filename):
    """Redirect to correct folder"""

    return send_from_directory('static/img/chesspieces/wikipedia/', filename)
