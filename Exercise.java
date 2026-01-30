public class Exercise {
    public static int[] calculate(int a, int b){
        int[] result = new int[3];
        result[0] = a+b;
        result[1] = a-b;
        result[2] = a*b;
        return result;
    }
    public static void main(String[] args){

        if (args.length < 2){
            System.out.println("Please provide two arguments.");
            return;
        }

        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);

        int[] equation = calculate(a, b);

        double quotient = (double) a / b;

        System.out.println("Sum:" + equation[0]);
        System.out.println("Difference:" + equation[1]);
        System.out.println("Product:" + equation[2]);
        System.out.println("Quotient:" + quotient);
    }
}
