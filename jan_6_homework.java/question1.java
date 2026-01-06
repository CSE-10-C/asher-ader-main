import java.util.Random;   // Allows us to generate random numbers

public class Question1 {
    public static void main(String[] args) {

        // Create a Random object
        Random rand = new Random();

        // Generate the first random number between 1 and 100
        int num = rand.nextInt(100) + 1;

        // Set both minimum and maximum to the first number
        // This gives us a starting point for comparisons
        int minimum = num;
        int maximum = num;

        // Loop 9 more times so we have 10 numbers total
        for (int i = 0; i < 9; i++) {

            // Generate another random number
            num = rand.nextInt(100) + 1;

            // If the new number is smaller than the current minimum,
            // update the minimum
            if (num < minimum) {
                minimum = num;
            }

            // If the new number is larger than the current maximum,
            // update the maximum
            if (num > maximum) {
                maximum = num;
            }
        }

        // Output the final minimum and maximum values
        System.out.println(minimum + " " + maximum);
    }
}