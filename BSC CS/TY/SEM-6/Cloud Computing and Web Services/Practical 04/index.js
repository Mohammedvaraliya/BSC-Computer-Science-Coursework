function showMap() {
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;

    // Check if latitude and longitude are provided
    if (!latitude || !longitude) {
        alert('Please enter both latitude and longitude.');
        return;
    }

    initMap(latitude, longitude);
}

function initMap(latitude=22.878710, longitude=78.804316, data = {}) {
    const info = { lat: parseFloat(latitude), lng: parseFloat(longitude) };
    const zoom = (data && data.zoom) || 6;
    const center = info;

    const map = new google.maps.Map(document.getElementById('map'), {
        zoom,
        center
    });

    const marker = new google.maps.Marker({
        position: info,
        map
    });
}
