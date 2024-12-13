const hst = window.location.host;
const url = window.location.href;
const lnCode = url.split(hst)[1].slice(0, 3); // get page lenguage code
const profileBnt = document.getElementById("profile_bnt"); // profili login register durs gal
const profile_menu = document.getElementById("profile_menu"); // (mutq elqi) menyu
const lenBnt = document.getElementById("ln_bnt"); // lezu yntrelu kochak
const len_menu = document.getElementById("lenguage_menu"); // lezu yntrelu menu
const openLocBut = document.querySelector("#openMap"); // qartezy bacelu knopka
const closeLocBut = document.querySelector("#closeMap"); //qartezy pakelu knopka
const locContainer = document.getElementById("loccont"); // qartezi amboxjakan containern e
const formAdres = document.getElementById("mapInputFormAdres"); //qartezum search inputn e
const headFormAdres = document.getElementById("SrcLocHead"); // glxavor ejum hascei mutqn e
const srcRez = document.getElementById("src_rez"); // glxavor ejum searchi ardyunqneri memium e
const mapSrcRez = document.getElementById("map_src_rez"); // qartezum voronman ardyunqnern en
const confBut = document.getElementById("loc_confirm"); // qartezum hascei hastatman kochakn e
var mymap;
var marker;

const renderConfButData = (newDataJson) => {
  if (newDataJson.lon_lat || newDataJson.id) {
    confBut.dataset.oldPoint_id = "";
    confBut.dataset.building_id = `${newDataJson.id}`;
    confBut.dataset.lon_lat = `${newDataJson.lon_lat}`;
    confBut.style.backgroundColor = "var(--buton_col_3)";
  } else {
    confBut.dataset.oldPoint_id = "";
    confBut.dataset.building_id = "";
    confBut.dataset.lon_lat = "";
    confBut.style.backgroundColor = "var(--bg_col_1)";
  }
  formAdres.value = newDataJson.search_rezult;
};

const fatchGetLocation = async (lat, lon) => {
  try {
    const responce = await fetch(
      `${lnCode}/location/cordinats/?latitude=${lat}&longitude=${lon}`,
      {
        headers: {
          Accept: "application.json",
          "X-Reguested-With": "XMLHttpRequest",
        },
      }
    );

    if (!responce.ok) {
      throw new Error(`HTTP eror: ${responce.status}`);
    }
    const newDataJson = await responce.json();
    renderConfButData(newDataJson);
  } catch (error) {
    console.error(error.message);
  }
};

const getOldloc = async () => {
  // harcum e katarum  vorpisi stana naxkinum patvirvac hascenery

  // aystex kaleli e optimizacnel ajnpes vor harcum katari miayn ayn depqum erb usery mutq
  // gorcac lini

  try {
    const responce = await fetch(`${lnCode}/location/orderedlocation/`, {
      headers: {
        Accept: "application.json",
        "X-Reguested-With": "XMLHttpRequest",
      },
    });

    if (!responce.ok) {
      throw new Error(`HTTP eror: ${responce.status}`);
    }
    const newDataJson = await responce.json();
    for (const location of newDataJson.old_location) {
      // srcRez ev mapSrcRez avelacnum e kochak ev data vory ir mej parunakum e
      // hin_hascener axyusaki id -in data-lat data-lon kordinatnery
      srcRez.innerHTML += `<li><button class="src-btn" data-building_id="${location.building}" data-id="${location.id}" data-lat="${location.geometry[0]}" data-lon="${location.geometry[1]}">${location.adres}</button></li>`;
      mapSrcRez.innerHTML += `<li><button class="map-src-btn" data-building_id="${location.building}" data-id="${location.id}" data-lat="${location.geometry[0]}" data-lon="${location.geometry[1]}">${location.adres}</button></li>`;
    }
  } catch (error) {
    console.error(error.message);
  }
};

getOldloc();

const mymarker = (marker, lat, lon, anim = false) => {
  if (marker) {
    mymap.removeLayer(marker);
  }
  marker = new L.marker([lat, lon]).addTo(mymap);
  if (anim) {
    mymap.flyTo([lat, lon], 18, {
      animate: true,
      duration: 2, // in seconds
    });
  }
  return marker;
};

const addEventMapSrcRez = (e) => {
  // mapSrcRez cojakin avelacnum e click event skzbic stugum e te clicky ardyoq exel e kochaki
  //vra aynuhetev kochaki datan talis e search inputin sahmanum e erku popoxakan lon lat
  //kordinatnery ev kanchum e mymarker functian
  //confBot hastatman kochaki guiny poxum e
  // ev dran talis e hin locatiai id vory yntrel e usery
  if (e.target && e.target.classList.contains("map-src-btn")) {
    const lat = parseFloat(e.target.dataset.lat);
    const lon = parseFloat(e.target.dataset.lon);
    marker = mymarker(marker, lat, lon, (anim = true));
    formAdres.value = e.target.textContent;
    confBut.dataset.lon_lat = "";
    confBut.dataset.building_id = `${e.target.dataset.building_id}`;
    confBut.dataset.oldPoint_id = `${e.target.dataset.id}`;
    confBut.style.backgroundColor = "var(--buton_col_3)";
  }
};
mapSrcRez.addEventListener("click", addEventMapSrcRez);

const addEventSrcRez = (e) => {
  if (e.target && e.target.classList.contains("src-btn")) {
    headFormAdres.value = e.target.textContent;
  }
};
srcRez.addEventListener("click", addEventSrcRez);

headFormAdres.addEventListener("click", () => (srcRez.style.display = "block"));
formAdres.addEventListener("click", () => (mapSrcRez.style.display = "block"));

formAdres.addEventListener("input", searchlocation);
headFormAdres.addEventListener("input", searchlocation);

function searchlocation(e) {
  srcRez.style.display = "block";
  if (e.target.value.length > 3) {
    fetch(`$location/adres/?q=${e.target.value}`, {
      headers: {
        Accept: "application.json",
        "X-Reguested-With": "XMLHttpRequest",
      },
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        // console.log(data)
        var srcresponse;
        for (srcresponse in data.search_rezoult)
          console.log(data.search_rezoult[srcresponse]);
        // srcRez.innerHTML += `<li><button><p>
        // ${data.search_rezoult[srcresponse].sity}
        // ${data.search_rezoult[srcresponse].stret}
        // </p></button></li>`
        // )
      });
  }
}

const mapClickEvent = (event) => {
  let lat = event.latlng.lat;
  let lon = event.latlng.lng;
  marker = mymarker(marker, lat, lon);
  fatchGetLocation(lat, lon);
};

const createLocatinBnt = () => {
  const OPTIONS = {
    enableHighAccuracy: true,
    timeout: 300000,
    maximumAge: 0,
  };

  const success = (pos) => {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;
    marker = mymarker(marker, lat, lon, (anim = true));
    fatchGetLocation(lat, lon);
  };
  const error = (err) => {
    console.warn(`ERROR(${err.code}): ${err.message}`);
  };

  bnt = L.easyButton(
    '<i class="verticalcenter"  "><img src="/static/mayin/img/gps_icon.svg"></i>',
    () => {
      navigator.geolocation.getCurrentPosition(success, error, OPTIONS);
    }
  );
  return bnt;
};

const addControlPlaceholders = (map) => {
  let corners = map._controlCorners;
  const l = "leaflet-";
  const container = map._controlContainer;

  const createCorner = (vSide, hSide) => {
    corners[vSide + hSide] = L.DomUtil.create(
      "div",
      "leaflet-" + vSide + " " + "leaflet-" + hSide,
      container
    );
  };

  createCorner("verticalcenter", "left");
  createCorner("verticalcenter", "right");
};

const renderMap = async () => {
  try {
    locContainer.style.cssText = "display: block;";
    if (mymap === undefined || mymap === null) {
      const STADYMAP = await L.tileLayer(
        "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
        {
          attribution:
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        }
      );
      const MAP_PARAMETER = {
        center: [40.785273, 43.841774],
        zoom: 13,
        attributionControl: false,
        minZoom: 12,
        maxZoom: 20,
        layers: [STADYMAP],
      };
      const mapdiv = document.getElementById("map");
      const bnt = createLocatinBnt();
      mymap = new L.map(mapdiv, MAP_PARAMETER);
      mymap.on("click", mapClickEvent);
      bnt.addTo(mymap);
      addControlPlaceholders(mymap);
      mymap.zoomControl.setPosition("verticalcenterleft");
      
    }
  } catch (eror) {
    console.warn(`ERROR(${eror.code}): ${eror.message}`);
  }
};

const openLocationCont = async () => {
  await renderMap(mymap);
};

openLocBut.addEventListener("click", openLocationCont);

closeLocBut.addEventListener("click", () => {
  locContainer.style.cssText = "display: none;";
  mapSrcRez.style.cssText = "display: none;";
});

profileBnt.onclick = function () {
  if (profile_menu.style.display !== "none") {
    profile_menu.style.display = "none";
  } else {
    profile_menu.style.display = "block";
  }
};

lenBnt.onclick = function () {
  if (len_menu.style.display !== "none") {
    len_menu.style.display = "none";
  } else {
    len_menu.style.display = "block";
  }
};
