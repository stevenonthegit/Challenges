// https://leetcode.com/problems/two-sum/

import java.util.Arrays;

 class TwoSum {

    private static int getIndexOf(int value, int[] arr){
        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] == value) { return i; }
        }

        return -1;
    }

    public static int[] twoSum(int[] nums, int target) {
        int[] arr = nums.clone();
        Arrays.sort(arr); //sort values to aid in runtime

        for(int i = arr.length-1; i >= 1; i--){
            if(arr[i] >= target) continue; //filter values >= target

            for(int j = i-1; j>=0; j--){
                if(arr[i] + arr[j] == target) {//found match
                    
                    //search original, unsorted array for indices to return
                    int a = getIndexOf(arr[j], nums); 
                    int b = getIndexOf(arr[i], nums);
                    return new int[] {a,b};
                }
            }
        }

        return new int[]{}; //if there are no matches, return empty array.
    }

    public static void main(String[] args){
        System.out.println("\n\n\n\nHello:");

        System.out.println(Arrays.toString(twoSum(new int[]{3,2,4}, 6)));
    }
}