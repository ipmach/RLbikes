var board;
var timeSetp;
const colors = ["#333333", "#ff4d4d", "#4da6ff", "#ee0606", "#930af3"]

function startGame(num) {
    myGameArea.start();
    // myGamePiece = new component(10, 10, "red", 0, 0);
    boardFirstTime(num)
    requestLoop(num)
}

var myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        div = document.getElementById("board");
        this.canvas.width = 500;
        this.canvas.height = 500;
        //this.canvas.style.left = "200px";
        //this.canvas.style.top = "250px";
        //this.canvas.style.position = "absolute";
        this.context = this.canvas.getContext("2d");
        //document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        div.appendChild(this.canvas)
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

function boardFirstTime(num){
    var request = new Request('http://127.0.0.1:5000/view/board/full/' + num);
        fetch(request)
          .then(response => {
            if (response.status === 200) {
                Promise.resolve(response.json()).then(function(value) {
                      board = processBoard(value.Board_view);
                      timeSetp = value.TimeStep;
                      drawBoard()
                })
            } else {
              throw new Error('Something went wrong on the api server!');
            }
          })
          .then(response => {
            console.debug(response);
          }).catch(error => {
            console.error(error);
          });
}

function updateInfo(value){
     document.getElementById("info").innerHTML = "Game: ${Game} <br>  Number of bikes: ${Bikes}/${NBikes} <br> Status: ${status} ".replace("${status}",
                                                                                                                          value.Status).replace("${Bikes}",
                                                                                                                          value.OnlineBikes).replace("${NBikes}",
                                                                                                                          value.NBikes).replace("${Game}",
                                                                                                                          value.Game)
     document.getElementById("info").style.color  = "#333333"
     document.getElementById("info").style.fontSize  =  "20px";
     document.getElementById("info2").innerHTML = "TimeSetp: ${Time} <br> Map: ${Map}".replace("${Time}", value.TimeStep).replace("${Map}", value.Map)
     document.getElementById("info2").style.color  = "#333333"
     document.getElementById("info2").style.fontSize  =  "20px";
}

function requestLoop(num) {
    setInterval(function () {
        var request = new Request('http://127.0.0.1:5000/view/board/update/' + num);
        fetch(request)
          .then(response => {
            if (response.status === 200) {
                Promise.resolve(response.json()).then(function(value) {
                  if (value.TimeStep > timeSetp || value.Status == "Finish") {
                      if ( value.Status != "Finish") {
                         board = processBoard(value.Board_view);
                         drawBoard()
                         console.log(board)
                      }
                      timeSetp = value.TimeStep;
                  }
                  updateInfo(value)
                })
            } else {
              throw new Error('Something went wrong on the api server!');
            }
          })
          .then(response => {
            console.debug(response);
          }).catch(error => {
            console.error(error);
          });}, 1000);
}



