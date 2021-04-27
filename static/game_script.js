var board;
var timeSetp;

function startGame() {
    myGameArea.start();
    myGamePiece = new component(30, 30, "red", 10, 120);
    boardFirstTime()
    requestLoop()
}

var myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = 480;
        this.canvas.height = 270;
        this.canvas.style.left = "200px";
        this.canvas.style.top = "200px";
        this.canvas.style.position = "absolute";
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
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

function boardFirstTime(){
    var request = new Request('http://127.0.0.1:5000/view/board/full/0');
        fetch(request)
          .then(response => {
            if (response.status === 200) {
                Promise.resolve(response.json()).then(function(value) {

                      board = value.Board_view;
                      timeSetp = value.TimeStep;
                })
            } else {
              throw new Error('Something went wrong on api server!');
            }
          })
          .then(response => {
            console.debug(response);
            // ...
          }).catch(error => {
            //console.error(error);
          });
}

function requestLoop() {
    setInterval(function () {
        var request = new Request('http://127.0.0.1:5000/view/board/update/0');
        fetch(request)
          .then(response => {
            if (response.status === 200) {
                Promise.resolve(response.json()).then(function(value) {
                  board = value.Board_view;
                  timeSetp = value.TimeStep;
                })
            } else {
              throw new Error('Something went wrong on api server!');
            }
          })
          .then(response => {
            console.debug(response);
            // ...
          }).catch(error => {
            console.error(error);
          });}, 1000);
}



