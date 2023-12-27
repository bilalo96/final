var google;

function init() {
    var myLatlng = new google.maps.LatLng(25.184242, 55.272430);

    var mapElement = document.getElementById('map'); // Define mapElement first

    var mapOptions = {
        zoom: 7,
        center: myLatlng,
        scrollwheel: false,
        styles: [
            {
                "featureType": "administrative.country",
                "elementType": "geometry",
                "stylers": [
                    {
                        "visibility": "simplified"
                    },
                    {
                        "hue": "#ff0000"
                    }
                ]
            }
        ]
    };

    var map = new google.maps.Map(mapElement, mapOptions); // Create the map using mapElement and mapOptions

    new google.maps.Marker({
        position: { lat: 25.255901445315114, lng: 55.33936933429995 },
        map: map,
        label: "A",
        title: "SpeedSwichCarRental",
        draggable: false,
        animation: google.maps.Animation.BOUNCE,
    });

    var addresses = ['Dubai'];

    for (var x = 0; x < addresses.length; x++) {
        $.getJSON('https://maps.googleapis.com/maps/api/geocode/json?address=' + addresses[x] + '&sensor=false', null, function (data) {
            var p = data.results[0].geometry.location;
            var latlng = new google.maps.LatLng(p.lat, p.lng);
            new google.maps.Marker({
                position: latlng,
                map: map,
                icon: 'images/loc.png'
            });

        });
    }
}

google.maps.event.addDomListener(window, 'load', init);
google.maps.event.addDomListener(window, 'load', init);
