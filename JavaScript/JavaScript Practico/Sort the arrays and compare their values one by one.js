//Sort the arrays and compare their values one by one.


function arrayCompare(_arr1, _arr2) {
    if (
        !Array.isArray(_arr1)
        || !Array.isArray(_arr2)
      || _arr1.length !== _arr2.length
      ) {
        return false;
    }
    
    // .concat() to not mutate arguments
    const arr1 = _arr1.concat().sort();
    const arr2 = _arr2.concat().sort();
    
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) {
            return false;
        }
    }
    
    return true;
}
console.log(arrayCompare([10, 6, 19, 16, 14, 15, 2, 9, 5, 3, 4, 13, 8, 7, 1, 12, 18, 11, 20, 17, 'string'], [12, 'string', 18, 20, 11, 19, 14, 6, 7, 8, 16, 9, 3, 1, 13, 5, 4, 15, 10, 2, 17]));

// let arr1= [10, 6, 19, 16, 14, 15, 2, 9, 5, 3, 4, 13, 8, 7, 1, 12, 18, 11, 20, 17];
// let arr2= [12, 18, 20, 11, 19, 14, 6, 7, 8, 16, 9, 3, 1, 13, 5, 4, 15, 10, 2, 17];