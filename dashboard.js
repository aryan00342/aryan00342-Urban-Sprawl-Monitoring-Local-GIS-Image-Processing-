// Leaflet Map
const map = L.map('map').setView([17.385, 78.4867], 10);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Chart.js
const ctx = document.getElementById('growthChart').getContext('2d');
new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['2015', '2017', '2019', '2021', '2023'],
    datasets: [{
      label: 'Urban Area (sq km)',
      data: [120, 150, 180, 220, 260],
      borderColor: 'blue',
      fill: false
    }]
  }
});
