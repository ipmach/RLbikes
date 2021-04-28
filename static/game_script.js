var board;
var timeSetp;
const colors = ["#0bced2", "#ddbd25", "#ee0606", "#930af3"]

function startGame() {
    myGameArea.start();
    // myGamePiece = new component(10, 10, "red", 0, 0);
    boardFirstTime()
    requestLoop()
}

var myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = 500;
        this.canvas.height = 500;
        this.canvas.style.left = "200px";
        this.canvas.style.top = "200px";
        this.canvas.style.position = "absolute";
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
    }
}

function drawBoard() {
    for (i = 0; i < board.length; i++) {
        y = board[i][0] * 10
        x = board[i][1] * 10
        c = board[i][2] - 1
        new component(10, 10, colors[c], x, y);
    }
}

function component(width, height, color, x, y) {
    this.width = width;
    this.height = height;
    this.x = x;
    this.y = y;
    ctx = myGameArea.context;
    ctx.fillStyle = color;
    ctx.fillRect(this.x, this.y, this.width, this.height);
}

function processBoard(view) {
    var result = [];
    view = view.split(" ");
    for (i = 0; i < view.length - 1; i++) {
        aux = view[i].split(",");
        result.push([parseInt(aux[0]),
                    parseInt(aux[1]),
                    parseInt(aux[2])]);
    }
    return result
}

function boardFirstTime(){
    var request = new Request('http://127.0.0.1:5000/view/board/full/0');
        fetch(request)
          .then(response => {
            if (response.status === 200) {
                Promise.resolve(response.json()).then(function(value) {
                      board = processBoard(value.Board_view);
                      timeSetp = value.TimeStep;
                      drawBoard()
                })
            } else {
              throw new Error('Something went wrong on api server!');
            }
          })
          .then(response => {
            console.debug(response);
          }).catch(error => {
            console.error(error);
          });
}

function requestLoop() {
    setInterval(function () {
        var request = new Request('http://127.0.0.1:5000/view/board/update/0');
        fetch(request)
          .then(response => {
            if (response.status === 200) {
                Promise.resolve(response.json()).then(function(value) {
                  if (value.TimeStep > timeSetp) {
                      board = processBoard(value.Board_view);
                      timeSetp = value.TimeStep;
                      console.log(board)
                      drawBoard()
                  }
                })
            } else {
              throw new Error('Something went wrong on api server!');
            }
          })
          .then(response => {
            console.debug(response);
          }).catch(error => {
            console.error(error);
          });}, 1000);
}



