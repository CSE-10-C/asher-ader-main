public class Question3 {
    public static void main(String[] args) {

        // Start a counter at 0
        int count = 0;

        // Loop through numbers from 1 to 100
        for (int num = 1; num <= 100; num++) {

            // Check if the number is even
            // Even numbers have no remainder when divided by 2
            if (num % 2 == 0) {

                // Increase the counter by 1
                count = count + 1;
            }
        }

        // Output the total number of even numbers
        System.out.println(count);
    }
}