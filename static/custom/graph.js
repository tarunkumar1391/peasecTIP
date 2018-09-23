$(function() {

     google.charts.load("current", {packages:["corechart"]});
     google.charts.setOnLoadCallback(drawChart);
     google.charts.setOnLoadCallback(drawChart2);

      function drawChart() {
          // fetch data first - published feeds
          arr = {};
          arr['table'] = 'stix_content';
          var sendData = JSON.stringify(arr, null, 2)

          $.ajax({
              url: '/publishedfeeds',
              data: sendData,
              type: 'POST',
              contentType: 'application/json;charset=UTF-8',
              dataType: 'json',
              success: function (response) {


                  //  Create a new DataTable (Charts expects data in this format)
                  var data = new google.visualization.DataTable();

                  // 6. Add two columns to the DataTable
                  data.addColumn('string', 'Type');
                  data.addColumn('number', 'feedcount');
                  // 7. Cycle through the records, adding one row per record
                  response.forEach(function (res) {
                      data.addRow([
                          (res.type),
                          (res.feedcount),
                      ]);
                  });
                  var options = {

                      pieHole: 0.5,
                      width: 850,
                      height: 650,
                      legend: {position: 'labeled'},
                      pieSliceText: 'value',

                  };

                  var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
                  chart.draw(data, options);

              },
              error: function (error) {
                  var result = JSON.stringify(error.responseText, null, "\t")

                  console.log(error);

              }

          });

      }
      function drawChart2() {
          // fetch data first - published feeds
          arr = {};
          arr['table'] = 'maec_content';
          var sendData = JSON.stringify(arr, null, 2)

          $.ajax({
              url: '/publishedmaecfeeds',
              data: sendData,
              type: 'POST',
              contentType: 'application/json;charset=UTF-8',
              dataType: 'json',
              success: function (response) {


                  //  Create a new DataTable (Charts expects data in this format)
                  var data = new google.visualization.DataTable();

                  // 6. Add two columns to the DataTable
                  data.addColumn('string', 'Type');
                  data.addColumn('number', 'feedcount');
                  // 7. Cycle through the records, adding one row per record
                  response.forEach(function (res) {
                      data.addRow([
                          (res.type),
                          (res.feedcount),
                      ]);
                  });
                  var options = {

                      pieHole: 0.5,
                      width: 850,
                      height: 650,
                      legend: {position: 'labeled'},
                      pieSliceText: 'value',

                  };

                  var chart = new google.visualization.PieChart(document.getElementById('donutchart2'));
                  chart.draw(data, options);

              },
              error: function (error) {
                  var result = JSON.stringify(error.responseText, null, "\t")

                  console.log(error);

              }

          });

      }
});

