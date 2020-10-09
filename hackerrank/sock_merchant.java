import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class sock_merchant {

    // Complete the sockMerchant function below.
    static int sockMerchant(int n, int[] ar) {
        //adds a count of all socks in ar[] to a "map" 
        int[] socks = new int[101];   
        for(int i = 0; i < n; i++){
            socks[ar[i]] += 1;
        }

        int pairs = 0;

        //sums the pairs (any index with socks >= 2)
        for(int i = 0; i < 101; i++){
            if(socks[i] > 1){
                pairs+= socks[i]/2;
            }
        }

    return pairs;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] ar = new int[n];

        String[] arItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arItem = Integer.parseInt(arItems[i]);
            ar[i] = arItem;
        }

        int result = sockMerchant(n, ar);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
