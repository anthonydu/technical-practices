/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function timeConversion(s: string): string {
  let hour = parseInt(s.substring(0, 2));
  if (s.substring(8, 9) == "A" && hour == 12) {
    hour = 0;
  }
  if (s.substring(8, 9) == "P" && hour != 12) {
    hour += 12;
  }

  return hour.toString().padStart(2, "0") + s.substring(2, 8);
}
