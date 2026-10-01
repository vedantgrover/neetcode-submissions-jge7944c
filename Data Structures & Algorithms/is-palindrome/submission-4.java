class Solution {
    public boolean isPalindrome(String s) {
        String cleanedS = "";

        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                cleanedS += Character.toLowerCase(c);
            }
        }

        int l = 0;
        int r = cleanedS.length() - 1;
        while (l < r) {
            if (cleanedS.charAt(l) != cleanedS.charAt(r)) {
                return false;
            }

            l++;
            r--;
        }
        
        return true;
    }
}
