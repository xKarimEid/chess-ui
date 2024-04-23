//var board = Chessboard('board', 'start')

//var board = null
var game = new Chess()
//var $status = $('#status')
//var $fen = $('#fen')
//var $pgn = $('#pgn')

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
    promotion: 'q' // NOTE: always promote to a queen for example simplicity
  })

  // illegal move
  if (move === null) return 'snapback'

  

}

// update the board position after the piece snap
// for castling, en passant, pawn promotion
function onSnapEnd () {
  //board.position(game.fen())
  if (!game.game_over()){
    updateStatus()
  }
  
}

function updateStatus () {
  var header = {
    'Content-Type': 'application/json'
  };

  var postData = { fen: game.fen()};
  
  $.ajax({
    type: 'POST',
    url: "http://127.0.0.1:8080/make_random_move",
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

board = Chessboard('board', config)