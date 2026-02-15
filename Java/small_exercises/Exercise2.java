public class Exercise2 {
    public static int[] GeneratingInt(int N){
        int[] num = new int[N];

        for (int i=0; i<N; i++){
            num[i] += i+1;
        }
        return num;
    }

    public static int SummingUp(int[] array){
        int len = array.length;
        int sum = 0;

        for (int i=0; i<len; i ++){
            sum += array[i];
        }
        return sum;
    }

    public static void main (String[] args){

        if (args.length == 0){
            System.out.println("Please insert an integer.");
        }

        int N = Integer.parseInt(args[0]);

        if (N > 0){
            int[] integers = GeneratingInt(N);
            int total = SummingUp(integers);

            System.out.println("First " + N + " integers are : ");
            for (int i=0; i < integers.length; i++){
                System.out.print(integers[i] + " ");
            }
            System.out.println();

            System.out.println("Total sum is " + total);
        }

        else{
            System.out.println("Please provide a positive integer.");
            return;
        }
    }
}
