/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr: number[]): void {
  let pos = 0;
  let neg = 0;
  let zer = 0;
  for (const n of arr) {
    if (n < 0) {
      neg += 1;
    } else if (n > 0) {
      pos += 1;
    } else {
      zer += 1;
    }
  }
  const sum = pos + neg + zer;
  console.log((pos / sum).toFixed(6));
  console.log((neg / sum).toFixed(6));
  console.log((zer / sum).toFixed(6));
}
