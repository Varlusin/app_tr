const openLocBut = document.querySelector("#openMap");
const closeLocBut = document.querySelector("#closeMap");
const locContainer = document.querySelector("#loccont");
var mymap;

function openLocationCont() {
  locContainer.style.cssText = "display: block;";
  if (mymap == undefined || mymap == null) {
    const mapdiv = document.querySelector("#map");
    const stadiaMaps = L.tileLayer(
      "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
      {
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }
    );
    mymap = new L.map(mapdiv, {
      center: [40.785273, 43.841774],
      zoom: 13,
      attributionControl: false,
      minZoom: 12,
      maxZoom: 20,
      layers: [stadiaMaps],
    });

    L.easyButton(
      '<img src="https://source.unsplash.com/random/200x200?sig=1">',
      function (btn, map) {
        alert("johvjhf");
      }
    ).addTo(mymap);

    var marker;

    mymap.on("click", (event) => {
      if (marker) {
        mymap.removeLayer(marker);
      }
      let lat = event.latlng.lat;
      let lng = event.latlng.lng;
      marker = new L.marker([lat, lng]).addTo(mymap);
      fetch(`/location/?latitude=${lat}&longitude=${lng}`, {
        headers: {
          Accept: "application.json",
          "X-Reguested-With": "XMLHttpRequest",
        },
      })
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data);
        });
    });
  }
}

openLocBut.addEventListener("click", openLocationCont);

closeLocBut.addEventListener("click", function () {
  locContainer.style.cssText = "display: none;";
});
