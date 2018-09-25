function draw_board(board){
  var grid;
  grid += "<tr><th></th>";
  for(var k = 0; k <= 9; k++){
    grid += "<th>"+k+"</th>";
  }
  grid += "</tr>"
  for(var i = 0; i <= 9; i++){
    grid += "<tr><th height='24px' width='24px'>"+i+"</th>";
    for(var j = 0; j <= 9; j++){
      grid += "<td id='a-"+i+"-"+j+"' height='24px' width='24px'><img height='24px' width='24px' src='img/wave.jpg'/></td>";
    }
    grid += "</tr>";
  }
  $(board).html(grid);
}

function populateBoats(file){
    $.get(file,function(txt){
        var lines = txt.split("\n");
        for (var i = 0, len = lines.length; i < len; i++) {
            for(var j = 0; j <= lines[i].length; j++){
              if(lines[i].charAt(j) !== '_'){
                $("#playerBoard").find("#a-"+i+"-"+j).html(lines[i].charAt(j));
              }
            }
        }
    });
}

draw_board("#playerBoard");
draw_board("#enemyBoard");
populateBoats("http://127.0.0.1:8001/own_board.txt");
function updateEnemySquare(x, y, type){
  switch(type){
    case 'H':
      $("#enemyBoard").find("#a-"+x+"-"+y).html("<img height='24px' width='24px' src='img/hit.png'/>");
      break;
    case 'M':
      $("#enemyBoard").find("#a-"+x+"-"+y).html("M");
      break;
    default:
      break;
  }
}
$(function (){
  $('#controls').submit(function(event){
    event.preventDefault();
    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:8001',
      data: {
        x: $("#xInput").val(),
        y: $("#yInput").val()
      },
      success: function(data, textStatus, request){
        if(request.getResponseHeader('hit') == 1){
          updateEnemySquare($("#xInput").val(),$("#yInput").val(), 'H');
          if(request.getResponseHeader('sunk')){
            var sunkShip;
            switch(request.getResponseHeader('sunk')){
              case 'C':
                sunkShip = "carrier";
                break;
              case 'B':
                sunkShip = "battleship";
                break;
              case 'R':
                sunkShip = "cruiser";
                break;
              case 'S':
                sunkShip = "submarine";
                break;
              case 'D':
                sunkShip = "destroyer";
                break;
              default:
                break;
            }
            alert("You sunk the enemy's " + sunkShip + "!");
            $("#resultMessage").append("You sunk the enemy's " + sunkShip + "!<br>");
          }
        }
        else{
          updateEnemySquare($("#xInput").val(),$("#yInput").val(), 'M');
        }
      },
      error: function(request, textStatus, errorThrown){
        alert(errorThrown);
      }
    });
  });
});
