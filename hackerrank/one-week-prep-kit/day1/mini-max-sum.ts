/*
 * Complete the 'miniMaxSum' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function miniMaxSum(arr: number[]): void {
  let sorted = arr.sort();
  let min = sorted[0] + sorted[1] + sorted[2] + sorted[3];
  let max = sorted[1] + sorted[2] + sorted[3] + sorted[4];
  console.log(min, max);
}
