const button = document.getElementById("btn");
button.addEventListener("click", async function (){
    const module = await import("./file.js");
    module.hello(); //llamar los modulos genear un inport dinamico//
});