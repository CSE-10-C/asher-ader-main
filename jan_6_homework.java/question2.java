public class Question2 {
    public static void main(String[] args) {

        // Array of numbers to examine
        int[] numbers = {5, 2, 9, 1, 7};

        // Set both minimum and maximum to the first number in the array
        int minimum = numbers[0];
        int maximum = numbers[0];

        // Loop through each number in the array
        for (int num : numbers) {

            // Check if the current number is smaller than the minimum
            if (num < minimum) {
                minimum = num;
            }

            // Check if the current number is larger than the maximum
            if (num > maximum) {
                maximum = num;
            }
        }

        // Output the minimum and maximum found
        System.out.println(minimum + " " + maximum);
    }
}