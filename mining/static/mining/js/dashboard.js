$(document).ready(function() {
  case_obj = JSON.parse(cases.replace(/'/g, '"'))

  $('.inlinebar').sparkline('html', {
    type: 'bar',
    height: '36px',
    width: '100%',
    barSpacing: 2,
    negBarColor: '#8A3E0B',
    barColor: '#FFF',
    barWidth: 18
  });

  $('#container').highcharts({

    xAxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    },
    chart: {
      type: 'line',
      style: {
        fontFamily: 'Roboto',
        textTransform: 'uppercase',
        fontWeight: '100'
      }
    },
    yAxis: {
      title: {
        text: null
      }
    },
    title: {
      text: 'New Fans'
    },
    series: [{
      data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
    }]

  });
});