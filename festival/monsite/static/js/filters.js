document.addEventListener("DOMContentLoaded", function() {
    let dateSelect = document.getElementById("dateSelect");
    let sceneSelect = document.getElementById("sceneSelect");
    let concerts = document.querySelectorAll(".concert-item");

    function filterConcerts() {
        let selectedDate = dateSelect.value;
        let selectedScene = sceneSelect.value;

        concerts.forEach(concert => {
            let concertDate = concert.getAttribute("data-date");
            let concertScene = concert.getAttribute("data-scene");

            let dateMatch = (selectedDate === "all" || concertDate === selectedDate);
            let sceneMatch = (selectedScene === "all" || concertScene === selectedScene);

            concert.style.display = (dateMatch && sceneMatch) ? "block" : "none";
        });
    }

    dateSelect.addEventListener("change", filterConcerts);
    sceneSelect.addEventListener("change", filterConcerts);
});
