/*
This is the front end which displays a chess board
for the user and lets the user makes legal moves. Whenever the
user makes a legal move a request is made to the backend to make the
chess engine play its move.
*/

// The Chess.js library is used to detect legal moves
var game = new Chess()


function onDragStart (source, piece, position, orientation) {
  // do not pick up pieces if the game is over
  if (game.game_over()) return false

  // only pick up pieces for the side to move
  if ((game.turn() === 'w' && piece.search(/^b/) !== -1) ||
      (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
    return false
  }
}

function onDrop (source, target) {
  // see if the move is legal
  var move = game.move({
    from: source,
    to: target,
    promotion: 'q' // NOTE: always promote to a queen for simplicity
  })

  // illegal move
  if (move === null) return 'snapback'

}

// update the board position after the piece snap
function onSnapEnd () {
  if (!game.game_over()){
    updateStatus()
  }
}

// Make a request to the backend to get make the chess engine
// play its move and get back the new position after the move is made
function updateStatus () {
  var header = {
    'Content-Type': 'application/json'
  };

  var postData = { fen: game.fen()};
  
  $.ajax({
    type: 'POST',
    url: "http://127.0.0.1:5000/make_move",
    headers: header,
    data: JSON.stringify(postData),
    
    success: function(data){
      console.log("data recieved back from engine: ", data);
      board.position(data);
      game.load(data, {skipValidation: true});
    }
  });
}

var config = {
  draggable: true,
  position: 'start',
  onDragStart: onDragStart,
  onDrop: onDrop,
  onSnapEnd: onSnapEnd
}

// initialize the chessboard
board = Chessboard('board', config)
