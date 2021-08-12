
function sterge_produs(button_id){
    fetch("/sterge-produs", {
        method: "POST",
        body: JSON.stringify({button_id: button_id}),
    }).then((_res) => {
        window.location.href = "/genereaza-nir";
    })
}

function sterge_nir(nir_id){
    const answer = window.confirm(" Sunteti sigur ca vreti sa stergeti acest NIR?")
    if (answer){
        fetch("/sterge-nir", {
            method: "POST",
            body: JSON.stringify({nir_id: nir_id}),
        }).then((_res) => {
            window.location.href = "/genereaza-nir";
        })
    }
}

