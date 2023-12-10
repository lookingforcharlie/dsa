class Solution {
    public boolean isPalindrome(String s) {
        String tempString = s.toLowerCase(); 
        ArrayList<Character> clearString = new ArrayList<>();
        for (char currentChar: tempString.toCharArray()) {
          if (Character.isLetter(currentChar) || Character.isDigit(currentChar)) {
            clearString.add(currentChar);
          }
        }

        ArrayList<Character> reversedClearString = new ArrayList<>(clearString);
        Collections.reverse(reversedClearString);

        if (reversedClearString.size() == 1) {
          return true;
        } else if (reversedClearString.equals(clearString))  {
          return true;
        } else {
            return false;
        }

        
    }
}