var $rentData = $('#rentData');

$.ajax({
    url:"https://www.kimonolabs.com/api/dp1wjjii?apikey=J2tyH8bzr1IF4HK8Tu8kqTM9FXOhzaQK",
    dataType: 'jsonp',
    success: function (response) {
    console.log(response);
        var rentList = response[1];
        for (var i = 0; i < rentList.length; i++) {
            $rentData.append('<li> ' + rentList[i] + '</li>')
        }
    },
    error: function (xhr, status) {
    console.log(xhr, status)
    }
});