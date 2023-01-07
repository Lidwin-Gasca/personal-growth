// let ingrSeleccionados = ['Pan de hamburguesa', 'Carne molida', 'Mayonesa', 'Queso'];
// let HamburguesaRequisito = ['Pan de hamburguesa', 'Carne molida', 'Mayonesa', 'Queso']

// function check(){
//     for (let i = 0; i < ingrSeleccionados.length; i++){
        
//     }
// }

// const receta = ['Pan de hamburguesa', 'Carne molida', 'Mayonesa', 'Queso']; 
const receta = ['Pan de hamburguesa', 'Carne molida', 'Mayonesa', 'Queso']
const ing = ["one", "two", "three", "four"]
let j = 0;
let existe = false;
for (let y in receta){
  
  for (let x in ing) {
    
    existe = ing.some((items) => {
      items = receta[y];
      if (items === ing[x]){ return existe = true;}         //Alternativa: ➡   if (items.toLowerCase() === ing[x].toLowerCase())
    });
    console.log(receta[y]);
  console.log(ing[x]);
  console.log(existe);
  j++;
  console.log(j);
}
}
console.log("total de " + j + " loops");
console.log(existe);

//💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢💢
//he a qui lo que realmente queria hacer:


// Lidwin Guillermo Gasca García:
// I need help coding in Javascript for a html5 website.
// I have two arrays, first array contains four elements which are: "bread", "meat", "tomato" and "cheese". the second array contains the following: "bun", "lemon", "bread", "meat", "tomato", "salt" and "cheese". 
// If the elements inside of the second array contain every single existing element from the first array, then print an image of a hamburger. 

//BOT:
//Certainly! Here is some code that should accomplish this task:
const firstArray = ["bread", "meat", "tomato", "cheese"];
const secondArray = ["bun", "lemon", "bread", "meat", "tomato", "salt", "cheese"];

function printHamburger(firstArray, secondArray) {
  let allElementsPresent = true;
  for (const element of firstArray) {
    if (!secondArray.includes(element)) {
      allElementsPresent = false;
      break;
    }
  }
  if (allElementsPresent) {
    // Print hamburger image here
    console.log("Hamburger image goes here!");
  } else {
    console.log("Some elements from the first array are missing from the second array.");
  }
}

printHamburger(firstArray, secondArray);

//This code first defines the two arrays that you provided. Then, it defines a function printHamburger that takes the two arrays as arguments. 
//The function uses a loop to check if every element in the first array is present in the second array. 
//If any element is missing, the allElementsPresent variable is set to false and the loop is exited. 
//If the loop completes without setting allElementsPresent to false, then it means that all the elements in the first array are present in the second array. 
//In that case, the function prints the hamburger image. 
//If allElementsPresent is false, the function prints a message indicating that some elements from the first array are missing from the second array.