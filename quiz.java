// public class quiz {
//     public static void main(String[] args) {

//         int arr[] = { 45, 78, 98, 56 };
//         int n = arr.length;
//         int max = arr[0];
//         int min = arr[0];
//         for (int i = 1; i < n; i++) {
//             if (arr[i] > max) {
//                 max = arr[i];
//             }
//             if (arr[i] < min) {
//                 min = arr[i];
//             }
//         }
//         System.out.println("Maximum element is " + max);
//         System.out.println("Minimum element is " + min);
//     }
// }

// public class quiz{
//     public static void main(String[] args) {
//         int fact = 1;
//         int n = 5;
//         for(int i = 1; i <= n; i++){
//             fact = fact * i;
//         }
//         System.out.println("Factorial of " + n + " is " + fact);
//     }
// }

// print first 10 even  number

// public class quiz {
//     public static void main(String[] args) {
//         int n = 1;
//         while (n <= 20) {
//             if (n % 2 == 0) {
//                 System.out.println(n);
//             }
//             n++;
//         }
//     }
// }

// merge sort

public class quiz {
    public static void main(String[] args) {
        int arr[] = { 12, 11, 13, 5, 6 };
        mergeSort(arr, 0, arr.length - 1);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void mergeSort(int arr[], int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    public static void merge(int arr[], int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;
        int L[] = new int[n1];
        int R[] = new int[n2];
        for (int i = 0; i < n1; ++i)
            L[i] = arr[left + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[mid + 1 + j];
        int i = 0, j = 0;
        int k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

}