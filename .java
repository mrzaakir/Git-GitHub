public class Java100 {
    public static void main(String[] args) {
        System.out.println("Line 1: Java program generated.");
        int count = 0;
        for (int i = 1; i <= 5; i++) {
            count += i;
            System.out.println("Loop step " + i + " count=" + count);
        }

        String[] words = {"alpha", "beta", "gamma", "delta"};
        for (String word : words) {
            System.out.println("Word: " + word);
        }

        int number = 42;
        if (number % 2 == 0) {
            System.out.println("42 is even.");
        } else {
            System.out.println("42 is odd.");
        }

        printMessage("Hello from Java!");
        int result = add(10, 20);
        System.out.println("10 + 20 = " + result);

        int[] array = {3, 6, 9, 12, 15};
        System.out.println("Sum of array = " + sumArray(array));

        double radius = 5.0;
        System.out.println("Circle area = " + circleArea(radius));

        String name = "Copilot";
        System.out.println("Name length = " + name.length());

        for (int i = 0; i < 3; i++) {
            System.out.println("Iteration " + i);
        }

        int factorial = 1;
        for (int i = 1; i <= 5; i++) {
            factorial *= i;
        }
        System.out.println("5! = " + factorial);

        boolean flag = true;
        if (flag) {
            System.out.println("Flag is true.");
        }

        printNumbers(1, 5);
        System.out.println("Done.");
    }

    public static void printMessage(String message) {
        System.out.println(message);
    }

    public static int add(int a, int b) {
        return a + b;
    }

    public static int sumArray(int[] values) {
        int total = 0;
        for (int value : values) {
            total += value;
        }
        return total;
    }

    public static double circleArea(double r) {
        return Math.PI * r * r;
    }

    public static void printNumbers(int start, int end) {
        for (int i = start; i <= end; i++) {
            System.out.println("Number: " + i);
        }
    }

    public static String repeatText(String text, int times) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < times; i++) {
            sb.append(text);
        }
        return sb.toString();
    }

    public static int max(int a, int b) {
        return Math.max(a, b);
    }

    public static int min(int a, int b) {
        return Math.min(a, b);
    }

    public static void showInfo() {
        System.out.println("This is a generated Java class.");
    }

    int x = 10;
    int y = 3;
    System.out.println("X + Y = " + (x + y));
    System.out.println("X - Y = " + (x - y));
    System.out.println("X * Y = " + (x * y));
    System.out.println("X / Y = " + (x / y));
    System.out.println("Repeat: " + repeatText("Hi", 3));
    System.out.println("Max: " + max(8, 5));
    System.out.println("Min: " + min(8, 5));
    showInfo();
}
