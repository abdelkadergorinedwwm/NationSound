document.addEventListener('DOMContentLoaded', function() {
    // Carte centrée sur le Parc de la Villette à Paris
    const map = L.map('map').setView([48.8566, 2.3522], 15); // Coordonnées du Parc de la Villette

    // Ajout du fond de carte OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Données des points d'intérêt
    const points = {
        scenes: [
            { name: 'Galactica', lat: 48.8566, lng: 2.3522},
            { name: 'Nebula', lat: 48.8576, lng: 2.3532},
            { name: 'Electroverse', lat: 48.8556, lng: 2.3512},
            { name: 'Scène Vibe Space', lat: 48.8546, lng: 2.3502},
            { name: 'Futur Wave', lat: 48.8546, lng: 2.3542} // Corrigée, ajout d'une virgule
        ],
        food: [
            { name: 'Food Truck 1', lat: 48.8570, lng: 2.3525, description: 'Burgers' },
            { name: 'Food Truck 2', lat: 48.8565, lng: 2.3515, description: 'Pizza' },
            { name: 'Restaurant', lat: 48.8575, lng: 2.3518, description: 'Restaurant du festival' }
        ],
        toilets: [
            { name: 'Toilettes 1', lat: 48.8568, lng: 2.3528},
            { name: 'Toilettes 2', lat: 48.8558, lng: 2.3518}
        ],
        info: [
            { name: 'Point Info Principal', lat: 48.8566, lng: 2.3520, description: 'Accueil principal' },
            { name: 'Point Info Secondaire', lat: 48.8560, lng: 2.3525, description: 'Point information' }
        ]
    };

    // Création des icônes personnalisées
    const icons = {
        scenes: L.divIcon({
            className: 'custom-icon',
            html: '<i class="fas fa-music" style="background-color: #e74c3c; padding: 8px; border-radius: 50%;"></i>',
            iconSize: [30, 30]
        }),
        food: L.divIcon({
            className: 'custom-icon',
            html: '<i class="fas fa-utensils" style="background-color: #2ecc71; padding: 8px; border-radius: 50%;"></i>',
            iconSize: [30, 30]
        }),
        toilets: L.divIcon({
            className: 'custom-icon',
            html: '<i class="fas fa-restroom" style="background-color: #3498db; padding: 8px; border-radius: 50%;"></i>',
            iconSize: [30, 30]
        }),
        info: L.divIcon({
            className: 'custom-icon',
            html: '<i class="fas fa-info-circle" style="background-color: #f1c40f; padding: 8px; border-radius: 50%;"></i>',
            iconSize: [30, 30]
        })
    };

    // Groupes de marqueurs pour chaque type
    const markerGroups = {};

    // Création des marqueurs pour chaque type de point
    Object.keys(points).forEach(type => {
        markerGroups[type] = L.layerGroup();

        points[type].forEach(point => {
            const marker = L.marker([point.lat, point.lng], {icon: icons[type]})
                .bindPopup(`<strong>${point.name}</strong><br>${point.description || ''}`);

            markerGroups[type].addLayer(marker);
        });

        // Ajout du groupe à la carte par défaut
        markerGroups[type].addTo(map);
    });

    // Gestion des filtres
    document.querySelectorAll('.filter-button').forEach(button => {
        button.addEventListener('click', () => {
            const type = button.dataset.type;
            button.classList.toggle('active');

            if (map.hasLayer(markerGroups[type])) {
                map.removeLayer(markerGroups[type]);
            } else {
                map.addLayer(markerGroups[type]);
            }
        });
    });
});
