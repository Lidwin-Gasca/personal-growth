let ingrSeleccionados = [];

function check(item){
    if (ingrSeleccionados.includes(item)){
        j = ingrSeleccionados.indexOf(item);
        ingrSeleccionados.splice(j,1);
        unLoadIngSel(item)
    }
    else {
        ingrSeleccionados.push(item);
        loadIngSel(item);
    }
}

function loadIngSel(item){          
    document.getElementById('sidebar').innerHTML += '<br>' + `<button type="button" id="${item}" class=" buttonCursor buttonRound buttonBorder" onclick="check('${item}');">${item}</button>`
}
function unLoadIngSel(item){
    let elem = document.getElementById(`${item}`);
    elem.parentNode.removeChild(elem);
    return false;
}