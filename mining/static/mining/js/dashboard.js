$(document).ready(function() {
  var customers = ["Humana", "Cerner", "Baystate", "Ochsner", "Epic", "Legacy", "Alexian", "Others"];
  var month_year = [new Date(2014, 7, 1), new Date(2014, 8, 1), new Date(2014, 9, 1), new Date(2014, 10, 1),
  new Date(2014, 11, 1), new Date(2015, 0, 1), new Date(2015, 1, 1), new Date(2015, 2, 1), new Date(2015, 3, 1),
  new Date(2015, 4, 1), new Date(2015, 5, 1), new Date(2015, 6, 1), new Date(2015, 7, 1)]
  var case_obj = JSON.parse(cases.replace(/'/g, '"'));

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });

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
      categories: ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul']
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
      text: '# of Cases -- Timeline'
    },
    legend: {
      layout: "vertical",
      align: "right",
      verticalAlign: "middle"
    },
    series: getMonthlyData()
  });

//console.log($(".col-xs-4 section header i").text}))
  $(".col-xs-4 section").click(function(e) {
    $.ajax({
      type: 'POST',
      url: 'case_list/',
      data: {"customer": $(this).find("header").text(), 'csrfmiddlewaretoken': csrftoken},
      success: function(){console.log("success!")}
    });
  });

  function getMonthlyData() {
    series_data = []
    for(var i = 0; i < customers.length; i++) {
        var customer_cases = case_obj[customers[i]]
        date_list = []
        for(var j = 0; j < month_year.length-1; j++) {
            var filtered = customer_cases.filter(function(obj) {
                case_create_date = new Date(Date.parse(obj["value"]))
                return case_create_date > month_year[j]
                && case_create_date < month_year[j+1]
            });
            date_list.push(filtered.length)
        }
        series_data.push({name: customers[i], data: date_list})
    }
    return series_data;
  }
});