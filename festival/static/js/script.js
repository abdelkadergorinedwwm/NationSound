/**
 * Sound Nation Festival - script.js
 * Ce fichier contient toutes les fonctionnalités JavaScript du site
 */

// Fonction pour le compteur à rebours jusqu'au festival
function initCountdown() {
    // Date du festival (12 juillet 2025 à 18h)
    const festivalDate = new Date("July 12, 2025 18:00:00").getTime();
    
    // Sélection des éléments du DOM pour le compteur
    const daysEl = document.getElementById("days");
    const hoursEl = document.getElementById("hours");
    const minutesEl = document.getElementById("minutes");
    const secondsEl = document.getElementById("seconds");
    const countdownEl = document.getElementById("countdown");
    
    // Si les éléments n'existent pas, ne pas initialiser le compteur
    if (!countdownEl) return;
    
    // Mise à jour du compte à rebours toutes les secondes
    const countdown = setInterval(function() {
        // Date actuelle
        const now = new Date().getTime();
        
        // Différence entre la date du festival et maintenant
        const distance = festivalDate - now;
        
        // Calculs pour jours, heures, minutes et secondes
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
        // Affichage des résultats avec padding de zéros
        if (daysEl) daysEl.innerHTML = days.toString().padStart(2, '0');
        if (hoursEl) hoursEl.innerHTML = hours.toString().padStart(2, '0');
        if (minutesEl) minutesEl.innerHTML = minutes.toString().padStart(2, '0');
        if (secondsEl) secondsEl.innerHTML = seconds.toString().padStart(2, '0');
        
        // Si le compte à rebours est terminé
        if (distance < 0) {
            clearInterval(countdown);
            if (countdownEl) countdownEl.innerHTML = "<h3>Le festival a commencé!</h3>";
        }
    }, 1000);
}

// Animation des cartes au défilement
function initCardAnimations() {
    const cards = document.querySelectorAll('.card');
    
    if ('IntersectionObserver' in window) {  // Vérification plus concise
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                    observer.unobserve(entry.target); // Arrêter l'observation une fois l'animation lancée
                }
            });
        }, { threshold: 0.2 });
        
        cards.forEach(card => {
            observer.observe(card);
        });
    } else {
        // Fallback pour les navigateurs qui ne supportent pas IntersectionObserver
        cards.forEach(card => {
            card.classList.add('animated');
        });
    }
}

// Navigation fluide pour les liens d'ancrage
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80, // Ajuster pour la hauteur de la navbar
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Initialiser la vidéo en arrière-plan
function initBackgroundVideo() {
    const videos = document.querySelectorAll('video');
    if (document.visibilityState === 'hidden') {
        // Si la page est déjà invisible au chargement, on met en pause la vidéo
        videos.forEach(video => video.pause());
    } else {
        // Si la page est visible, on tente de lire la vidéo
        videos.forEach(video => {
            const playPromise = video.play();
            if (playPromise !== undefined) {
                playPromise.catch(error => {
                    console.log("Lecture automatique empêchée:", error);
                });
            }
        });
    }

    // Gérer les changements de visibilité de la page
    document.addEventListener('visibilitychange', () => {
        videos.forEach(video => {
            if (document.visibilityState === 'hidden') {
                video.pause();
            } else {
                video.play().catch(error => {
                    console.log("Reprise empêchée:", error);
                });
            }
        });
    });
}

// Exécuter toutes les initialisations quand le DOM est chargé
document.addEventListener('DOMContentLoaded', function() {
    initCountdown();
    initCardAnimations();
    initSmoothScroll();
    initBackgroundVideo();
    
    // Activer les tooltips Bootstrap si disponibles
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function(tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
});
