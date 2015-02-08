$( document ).ready(function() {

    $("#getTax").click(function(){
        var apiKey = "obANed1yNyc6tzQRMiLkh3ohCy%2BfgF8zlLyPTf54x7fBfjcicdFmB1J04cj4bkNe37RyH0XDaTTzx1UG3aq6bg%3D%3D";
        var avalaraURL = "https://taxrates.api.avalara.com/";
        var postalParam = "postal?country=usa&postal="+$('#getTax').text();
//        var avalaraAPI = "https://taxrates.api.avalara.com/postal?country=usa&postal=94109&apikey="+ apiKey;
        var avalaraAPI = avalaraURL + postalParam + "&apikey=" + apiKey;
        $.getJSON( avalaraAPI, {
            format: "json"
        })
        .done(function( data ) {
        $("#InsertTax").html(data.totalRate+"%");
        console.log(data.totalRate);
//      $.each( data.items, function( i, item ) {
//        $( "<img>" ).attr( "src", item.media.m ).appendTo( "#images" );
//        if ( i === 3 ) {
//          return false;
//        }
//      });
    });
    });
});