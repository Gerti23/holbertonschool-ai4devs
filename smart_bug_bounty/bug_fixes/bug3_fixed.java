import java.util.HashMap;
import java.util.Map;

public class bug3_fixed {
    public static char firstUniqueChar(String text) {
        if (text == null || text.isEmpty()) {
            return '\0';
        }

        Map<Character, Integer> counts = new HashMap<>();
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            counts.put(c, counts.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (counts.get(c) == 1) {
                return c;
            }
        }

        return '\0';
    }

    public static void main(String[] args) {
        System.out.println(firstUniqueChar("swiss"));
    }
}
