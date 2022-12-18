let ingrSeleccionados = [];
let it;

function loadIngSel(item){          
    document.getElementById('sidebar').innerHTML += `<br id="${item}1">` + `<button type="button" id="${item}" class=" buttonCursortemp buttonRoundtemp buttonBordertemp" onclick="check('${item}');">${item}</button>`
}

function unLoadIngSel(item){
    let elem = document.getElementById(`${item}`); //para no ser repetitivo con el document.getElementById(), se lo doy a una variable (es este caso llamado elem), de esta manera en adelante solo usare esa vareable.
    let elem1 = document.getElementById(`${item}1`);
    elem.style.display = "none"; //esta linea no me sirvio, ya que en la linea de abajo lo remuevo el elemento por completo. pongo la variable seguido de un punto y la palabra "estilo" en ingles, para enfatizar que estoy modificando el CSS, seguido de oto punto y la propiedad que estoy deseando modificar o agregar.
    elem1.style.display = "none";
    elem.parentNode.removeChild(elem); //esto elimina el elemento con el valor `item`.    /// una Alternativa seria-->  elem.remove();
    elem1.parentNode.removeChild(elem1);
    return false;
}

function check(item){
    if (ingrSeleccionados.includes(item)){
        j = ingrSeleccionados.indexOf(item);
        ingrSeleccionados.splice(j,1);
        unLoadIngSel(item)
        document.getElementById(`${item}p`).style.backgroundColor = 'White';
        document.getElementById(`${item}p`).style.color = 'Black';
    }
    else {
        ingrSeleccionados.push(item);
        loadIngSel(item);
        document.getElementById(`${item}p`).style.backgroundColor = '#555555';
        document.getElementById(`${item}p`).style.color = '#b8b8b8';
    }
}