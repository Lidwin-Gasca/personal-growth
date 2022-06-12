//callbacks

function sum(num1, num2) {
    return num1 + num2;
}
function calc(num1, num2, callback) { ///lo llamamos callback por buena practica pero podria ser llamado de cualquier forma
    return callback(num1, num2);
}
console.log(calc(2, 2, sum));


//otro ejemplo de callback
function date(callback){
    console.log(new Date);
    setTimeout(function () {
        let date = new Date;
        callback(date);
    }, 3000)
}
function printDate(dateNow) {
    console.log(dateNow);
}

date(printDate);


/* la función que recibe como parámetro otra función.
Una función que recibe otra función como parámetro se le denomina función de orden superior (higher-order function).
El callback en este caso sería la función que es pasada como parámetro, mas no la función que lo recibe
*/