class Solution {
    public int lengthOfLastWord(String s) {
        String[] myString = s.split(" "); 
        int len = myString.length; 
        int result = myString[len -1 ].length();
        return result;
    }
}