myArr = [];

function onPageLoad(){
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            myArr = JSON.parse(xmlhttp.responseText);
        }
    };
        var url = "/chart_data"
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
     }
      function drawChart() {

        var data = google.visualization.arrayToDataTable(myArr);

        var options = {
          title: 'My Daily Activities'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }



