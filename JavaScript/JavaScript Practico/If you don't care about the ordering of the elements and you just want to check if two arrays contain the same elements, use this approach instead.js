//If you don't care about the ordering of the elements and you just want to check if two arrays contain the same elements, use this approach instead.

const arr1 = ['c', 'b', 'a', 'd', 'e', 'f'];
const arr2 = ['a', 'b', 'c', 'd', 'z'];

function areEqual(array1, array2) {
  if (array1.length === array2.length) {
    return array1.every(element => {
      if (array2.includes(element)) {
        return true;
      }

      return false;
    });
  }

  return false;
}

console.log(areEqual(arr1, arr2)); // 👉️ true

//this is bullshit, no sirve la chingadera
