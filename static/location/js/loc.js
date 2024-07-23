const formAdres = document.querySelector('#id_q')


formAdres.addEventListener("input", searchlocation);


function searchlocation(e){
    if(e.target.value.length >3){
        console.log(e.target.value)
        fetch(`/location/adres/?q=${e.target.value}`)
    }
}