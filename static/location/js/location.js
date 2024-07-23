
const openLocBut = document.querySelector("#openMap");
const closeLocBut = document.querySelector("#closeMap");
const locContainer = document.querySelector("#loccont");
const formAdres = document.querySelector('#formadres');
const headFormAdres = document.querySelector('#SrcLocHead');
var mymap;


formAdres.addEventListener("input", searchlocation);
headFormAdres.addEventListener("input", searchlocation);

function searchlocation(e){
    if(e.target.value.length >3){
        console.log('fvhuerih')
        fetch(`/location/adres/?q=${e.target.value}`, {
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
                // formAdres.value = `${data.sity} ${data.street} ${data.adres}`
              });
    }
}


function mymarker(marker,lat, lon){
  if (marker){
    mymap.removeLayer(marker);
  }
  marker = new L.marker([lat, lon]).addTo(mymap);
  fetch(`/location/cordinats/?latitude=${lat}&longitude=${lon}`, {
    headers: {
        Accept: "application.json",
        "X-Reguested-With": "XMLHttpRequest",
      },
    })
      .then((response) => {
        return response.json();
      })
      .then((resp) => {
        for(i in resp.adr){
          console.log(i);
        }
        formAdres.value = `${data.sity} ${data.street} ${data.adres}`
      });
      return marker
}


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

    var marker;

    mymap.on("click", (event) => {
      let lat = event.latlng.lat;
      let lon = event.latlng.lng;
      (e)=>mm(e)
      marker =  mymarker(marker,lat, lon)
    });

    L.easyButton(
      '<img src="https://source.unsplash.com/random/200x200?sig=1">',
      function () {
        const options = {
          enableHighAccuracy: true,
          timeout: 300000,
          maximumAge: 0,
        };
      
        function success(pos) {
            const lat = pos.coords.latitude
            const lon = pos.coords.longitude
            marker =  mymarker(marker,lat, lon)
            mymap.flyTo([lat, lon], 15, {
              animate: true,
              duration: 2 // in seconds
            });
        }
      
        function error(err) {
          console.warn(`ERROR(${err.code}): ${err.message}`);
        }
      
        navigator.geolocation.getCurrentPosition(success, error, options);
      }
    ).addTo(mymap);


  }
}

openLocBut.addEventListener("click", openLocationCont);

closeLocBut.addEventListener("click", function () {
  locContainer.style.cssText = "display: none;";
});
