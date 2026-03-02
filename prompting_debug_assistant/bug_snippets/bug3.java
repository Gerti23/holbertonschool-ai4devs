/**
 * Bug 3: Runtime exception - NullPointerException
 * This class should calculate the average length of strings in a list,
 * ignoring null values.
 */

import java.util.ArrayList;
import java.util.List;

public class bug3 {
    
    /**
     * Calculates the average length of non-null strings in a list.
     * 
     * @param strings List of strings (may contain nulls)
     * @return Average length of non-null strings
     */
    public static double calculateAverageLength(List<String> strings) {
        int totalLength = 0;
        int count = 0;
        
        for (String str : strings) {
            // Bug: No null check before calling length()
            totalLength += str.length();
            count++;
        }
        
        return count > 0 ? (double) totalLength / count : 0.0;
    }
    
    public static void main(String[] args) {
        List<String> words = new ArrayList<>();
        words.add("hello");
        words.add("world");
        words.add(null);  // This will cause NullPointerException
        words.add("test");
        
        System.out.println("Average length: " + calculateAverageLength(words));
        // Expected: 4.67 (ignoring null)
    }
}