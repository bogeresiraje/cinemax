
var link = "The_Meg_1";

function getServerData() {
  var url = "http://127.0.0.1:5000/appdir/booking/" + link;

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if(this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText);
      data = data.chart;
      showTable(data);
    }
  };
  xhttp.open("GET", url , true);
  xhttp.send();
}

function setLink() {
  var movieTitle = document.getElementById("mov");
  var startTime = document.getElementById("start");
  link = movieTitle + "_" + startTime;
}

function showTable(data) {

  var colHead = ["", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
    18, 19, 20];
  var rowHead = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
   'M', 'N', 'O', 'P'];

  var myTable = document.getElementById("chartTable");

  for(var i = 0; i < 17; i++) {
    var row = myTable.insertRow(i);

    for(var j = 0; j < 21; j++) {
      if(i%2 == 1){
        row.classList.add("alt");
      }
      if(i == 0){
        var cell = row.insertCell(j);
        cell.innerHTML = colHead[j];
      } else {
        if(j == 0){
          var cell = row.insertCell(j);
          cell.innerHTML = rowHead[i-1];
        }else {
          var cell = row.insertCell(j);
          cell.innerHTML = data[i-1][j-1];
        }
      }
    }
  }
}


function checkSeats() {
  var categ = document.getElementById("opt").value;
  var bookReserve = document.getElementById("b_or_r").value;
  var url = "http://127.0.0.1:5000/appdir/booking/movie?" + "movie_link=" + link + "&category=" + categ
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if(this.readyState == 4 && this.status == 200) {
      seats = JSON.parse(this.responseText);
      seats = seats.available;

      if(seats != null){
        var thisForm = document.getElementById("avaiableSeats");
        var thisURL = "http://127.0.0.1:5000/booking/" +link+ "/" +categ+ "/" +bookReserve;
        thisForm.setAttribute("action", thisURL);

        selectElement = document.getElementById("rightPane");
        var element = document.getElementById("selectForm");
        selectElement.removeChild(element);

        //side1 div
        var mydiv = document.getElementById("side1");

        //side2 div
        var mydiv2 = document.getElementById("side2");

        //side3 div
        var mydiv3 = document.getElementById("side3");

        //side4 div
        var mydiv4 = document.getElementById("side4");

        var divTitle = document.getElementById("divHead");

        if(categ == 1){
          divTitle.innerHTML = "Available Twin Seats";
        } else if(categ == 2){
          divTitle.innerHTML = "Available VVIP Seats";
        } else if(categ == 3){
          divTitle.innerHTML = "Available VIP Seats";
        } else {
          divTitle.innerHTML = "Available Economy Seats";
        }

        var seatLength = seats.length;
        var initLength = Math.ceil(seatLength/4);

        //div side1
        var length = 0;
        var newLength = initLength;

        if(newLength < seats.length){

        } else {
          newLength = seats.length;
        }

        for(var i = length; i < newLength; i++){
            var node = document.createElement('div');
            node.innerHTML = '<input type="checkbox" name='+seats[i]+' id="check'+i+'" value='+seats[i]+'> <label for="check'+i+'">'+seats[i]+'</label>'
            mydiv.appendChild(node);
        }

        //div side2
        length = newLength;
        newLength = 2 * initLength;

        if(newLength < seats.length){

        } else {
          newLength = seats.length;
        }

        for(var i = length; i < newLength; i++){
            var node = document.createElement('div');
            node.innerHTML = '<input type="checkbox" name='+seats[i]+' id="check'+i+'" value='+seats[i]+'> <label for="check'+i+'">'+seats[i]+'</label>'
            mydiv2.appendChild(node);
        }

        //div side3
        length = newLength;
        newLength = 3 * initLength;
        if(newLength < seats.length){

        } else {
          newLength = seats.length;
        }

        for(var i = length; i < newLength; i++){
            var node = document.createElement('div');
            node.innerHTML = '<input type="checkbox" name='+seats[i]+' id="check'+i+'" value='+seats[i]+'> <label for="check'+i+'">'+seats[i]+'</label>'
            mydiv3.appendChild(node);
        }

        //side4
        length = newLength;
        newLength = 4 * initLength;
        if(newLength < seats.length){

        } else {
          newLength = seats.length;
        }

        for(var i = length; i < newLength; i++){
            var node = document.createElement('div');
            node.innerHTML = '<input type="checkbox" class="fool" name='+seats[i]+' id="check'+i+'" value='+seats[i]+'> <label for="check'+i+'">'+seats[i]+'</label>'
            mydiv4.appendChild(node);
        }

        buttondiv1 = document.getElementById("button1");
        buttondiv1.innerHTML = '<input type="button" value="cancel" id="butt1">'

        buttondiv2 = document.getElementById("button2");
        buttondiv2.innerHTML = '<input type="button" value="submit" id="butt2" onclick="submit()">'
      } else {
        if(categ == 1){
          divTitle.innerHTML = "No More Available Twin Seats";
        } else if(categ == 2){
          divTitle.innerHTML = "No More Available VVIP Seats";
        } else if(categ == 3){
          divTitle.innerHTML = "No MoreAvailable VIP Seats";
        } else {
          divTitle.innerHTML = "No More Available Economy Seats";
        }
      }
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}
