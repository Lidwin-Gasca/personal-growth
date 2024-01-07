let ingrSeleccionados = [];
let HamburguesaRequisito = ['Pan de hamburguesa', 'Carne molida', 'Mayonesa', 'Queso']
let HamburguesaExtras = ['Lechuga', 'cebolla', 'Jitomate', 'Tocino', 'Huevo']
let HotdogRequisito = ['Pan de hotdog', 'Salchicha', 'Mayonesa'];
let HotdogExtras = ['cebolla', 'Jitomate', 'Tocino', 'Queso'];
let TacosRequisito = ['Tortilla', 'Harina de maiz', 'Harina de Trigo'];
let TacoCarnes = ['Carne molida', 'Carne en filete', 'Carne en filete de pollo', 'Carne en trozo', 'Carne de pollo'];
let TacosExtras = ['Limon', 'Cebolla', 'Jitomate', 'Sal', 'Chile fresco'];
let contadorDeHamburguesa = 0;

function loadIngSel(item){          
    document.getElementById('sidebar').innerHTML += `<br id="${item}1">` + `<button type="button" id="${item}" class=" buttonCursortemp buttonRoundtemp buttonBordertemp" onclick="check('${item}');">${item}</button>`;
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
        let j = ingrSeleccionados.indexOf(item);
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

  function checkImageLoad() {
    setTimeout(
        function printImage(firstArray, secondArray) {
            firstArray = HamburguesaRequisito;
            secondArray = ingrSeleccionados;
            let allElementsPresent = true;
            for (const element of firstArray) {
              if (!secondArray.includes(element)) {
                allElementsPresent = false;
                break;
                }
              }
            if (allElementsPresent) {
              // Print hamburger image here
              document.getElementById('content1').innerHTML += '<img id="hamburguesa" src="./images/content/hamburger.jpg" alt="Hamburguesa">';
            } else {
                if (document.getElementById("hamburguesa") == true){
                    parentNode.removeChild(document.getElementById("hamburguesa"));
                }
            }
          }, 2000);
          setTimeout(
            function printImage(firstArray, secondArray) {
                firstArray = HotdogRequisito;
                secondArray = ingrSeleccionados;
                let allElementsPresent = true;
                for (const element of firstArray) {
                  if (!secondArray.includes(element)) {
                    allElementsPresent = false;
                    break;
                  }
                }
                if (allElementsPresent) {
                  // Print hamburger image here
                  document.getElementById('content2').innerHTML += '<img id="hotdog" src="./images/content/Hotdog.jpg" alt="Hotdog">';
                } else {
                    if (document.getElementById("hotdog") == true){
                        console.log("quitalo");
                        parentNode.removeChild(document.getElementById("hotdog"));
                    }
                }
              }, 2000);
              setTimeout(
                function printImage(firstArray, secondArray) {
                    firstArray = TacoCarnes;
                    secondArray = ingrSeleccionados;
                    let allElementsPresent = true;
                    for (const element of firstArray) {
                      if (!secondArray.includes(element)) {
                        allElementsPresent = false;
                        break;
                      }
                    }
                    if (allElementsPresent) {
                      // Print hamburger image here
                      console.log("a ver");
                      if (!document.getElementById("taco") == true){
                          document.getElementById('content3').innerHTML += '<img id="taco" src="./images/content/taco.jpg" alt="Tacos">';
                          console.log("sera que funciona");
                      }
                     else {
                        console.log("o quiza");
                        if (document.getElementById("hotdog") == true){
                            parentNode.removeChild(document.getElementById("taco"));
                            console.log("no funciona");
                            }
                        }
                    }
                  }, 2000);
  }





