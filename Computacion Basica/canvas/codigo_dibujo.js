var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d");
console.log(lienzo);

lienzo.beginPath();
lienzo.strokeStyle = "red";
lienzo.moveTo(100,80);
lienzo.lineTo(200,200);
lienzo.stroke();
lienzo.closePath();

lienzo.beginPath();
lienzo.strokeStyle = "blue";
lienzo.moveTo(10,150);
lienzo.lineTo(20,300);
lienzo.stroke();
lienzo.closePath();
