const locContainer = document.querySelector("#loccont");
const openLocBut = document.querySelector("#openMap");
const closeLocBut = document.querySelector("#closeMap");
const getLocation = document.querySelector("#getlocation");


function createMap(latitude, longitude, zom = 13) {
  const stadiaMaps = L.tileLayer(
    "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }
  );
  const mymap = L.map("map", {
    center: [latitude, longitude],
    zoom: zom,
    attributionControl: false,
    minZoom: 12,
    maxZoom:20,
    layers: [stadiaMaps],
  });
  mymap.on("click", (event) => {
    let lat = event.latlng.lat;
    let lng = event.latlng.lng;
    L.marker([lat, lng]).addTo(mymap);
    fetch(`/location?latitude=${lat}&longitude=${lng}`);
  });

  return mymap;
}

function openLocationCont() {
  locContainer.style.cssText = "display: block;";
  createMap((latitude = 40.785273), (longitude = 43.841774));
}


closeMap.addEventListener("click", function () {
  locContainer.style.cssText = "display: none;";
});



// getLocation.addEventListener("click", function () {
//     const options = {
//       enableHighAccuracy: true,
//       timeout: 10000,
//       maximumAge: 0,
//     };
  
//     function success(pos) {
//         const crd = pos.coords;
//             // mymap.remove();
//             // createMap((latitude = crd.latitude), (longitude = crd.longitude), (zom = 17));
//             L.marker([crd.latitude, crd.longitude]).addTo(mymap);    
//     }
  
//     function error(err) {
//       console.warn(`ERROR(${err.code}): ${err.message}`);
//     }
  
//     navigator.geolocation.getCurrentPosition(success, error, options);
//   });