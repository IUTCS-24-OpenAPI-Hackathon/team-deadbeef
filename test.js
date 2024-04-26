function initMap()
{
    if (google && google.maps && google.maps.places) 
    {
        autocomplete = new google.maps.places.Autocomplete((document.getElementById('autocomplete')), {
            types: ['geocode']
        });

        autocomplete.addListener('places_changed', searchNearbyPlaces);
    } else {
        // If the Places library is not loaded, try again after a short delay
        setTimeout(initMap, 100);
    }
}

function searchNearbyPlaces()
{
    document.getElementById('places').innerHTML = ''

    var place  = autocomplete.getPlace()
    console.log(place)

    map = new google.maps.Map(document.getElementById('map'),
    {
        center:place.geometry.location,
        zoom: 15
    });

    service = new google.maps.places.PlacesService(map);
    service.nearbySearch(
        {
            location:place.geometry.location,
            radius : '500',
            type: [document.getElementById('type').value]
        }, callback);
}


function callback(results, status)
{
    if(status == google.maps.places.PlacesServiceStatus.OK)
    {
        console.log(results.length)
        for(var i = 0; i<results.length;i++)
        {
            createMarker(results[i]);            
        }
    }
}


function createMarker(place)
{
    console.log(place)
    var table = document.getElementById("places");
    var row = table.insertRow();
    var cell1 = row.insertCell(0);
    cell1.innerHTML = place.name;

    if(place.photos)
    {
        let photoUrl = place.photos[0].getUrl();
        let cell2 = row.insertCell(1)
        cell2.innerHTML = `<img width = "300" height = " 300" src="${photoUrl}"/>`
    }
    else
    {
        let photoUrl = "https://via.placeholder.com/150"
        let cell2 = row.insertCell(1)
        cell2.innerHTML = `<img width="300" height= "300" src="${photoUrl}"/>`
    }
}

