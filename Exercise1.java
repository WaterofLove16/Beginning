public class Exercise1 {

    public static int SumUpTo(int N){

        int sum = 0;
        for (int i=1; i<=N; i++){
            sum += i;
        }
        return sum;
    }

    public static int SumByFormular(int N){

        int sum = (N*(N+1))/2;
        return sum;
    }

    public static void main(String[] args){
        if (args.length == 0) {
        System.out.println("Please provide an integer.");
        return;
        }
        
        int N = Integer.parseInt(args[0]);
        
        if (N >= 1){
            int sum1 = SumUpTo(N);
            int sum2 = SumByFormular(N);

            double ave2 = (double) sum2/N;
            double ave1 = (double) sum1/N;
            
            System.out.println("Total sum of loop is " + sum1);
            System.out.println("Average of loop is " + ave1);
            System.out.println("Total sum of equation is " + sum2);
            System.out.println("Average of equation is " + ave2);
        }
        
        else{
            System.out.println("Please provide a positive integer.");
        }
    }
}
