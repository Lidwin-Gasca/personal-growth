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
    let elem = document.getElementById(`${item}`); //para no ser repetitivo con el document.getElementById(), se lo doy a una variable (es este caso llamado elem), de esta manera en adelante solo usare esa vareable.
    elem.style.display = "none"; //esta linea no me sirvio, ya que en la linea de abajo lo remuevo el elemento por completo. pongo la variable seguido de un punto y la palabra "estilo" en ingles, para enfatizar que estoy modificando el CSS, seguido de oto punto y la propiedad que estoy deseando modificar o agregar.
    elem.parentNode.removeChild(elem); //esto elimina el elemento con el valor `item`.    /// una Alternativa seria-->  elem.remove();
    return false;
}