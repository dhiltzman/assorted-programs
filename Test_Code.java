import java.util.Scanner;

public class Test_Code{
    public static int temp;
    public static int a;
    public static int b;


    public static void main(String[] args){
        int[] NumArray = {6,11,2,25,0,-1};

        //finding smallest int
        for (int i = 0; i < 5; i++){
            a = NumArray[i];   
            b = NumArray[i + 1];

            if (a > b){
                a = b;
            }
        }

        System.out.println("Smallest Number: " + a);
        
        int min = 1000000;
        for (int v: NumArray){
            if (v < min){
                min = v;
            }
        }

        System.out.println("Smallest Number: " + min);
        /*
        for (int i = 0; i < 7; i++){
            System.out.println(NumArray[i]);
        }
        */
    }
}