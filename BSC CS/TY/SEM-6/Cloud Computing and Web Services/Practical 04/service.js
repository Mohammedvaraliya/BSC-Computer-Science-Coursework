// public/mapService.js
function initMapService(latitude, longitude) {
    const info = { lat: latitude, lng: longitude };
    const map = new google.maps.Map(document.getElementById('map'), {
      zoom: 15,
      center: info,
    });
  
    const marker = new google.maps.Marker({
      position: info,
      map: map,
    });
  }
  