import java.util.HashMap;
import java.util.Map;
// Question taken from https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
public class Anagram {

    private Map<Character, Integer> MakeDict(String a){
        Map<Character, Integer> numberdict = new HashMap<>();
        for(int i = 0; i < a.length(); i++){
            char currentchar  = a.charAt(i);
            if(numberdict.containsKey(currentchar) == true){
                numberdict.put(currentchar, numberdict.get(currentchar) + 1);
            }
            else{
                numberdict.put(currentchar, 1);
            }
        }
        return numberdict;
    }

    private int findDeleteCount(String a, String b, Map<Character, Integer> dicta, Map<Character, Integer> dictb){
        int deletioncount = 0;
        for(int i=0; i<dicta.size(); i++){
            char currentchar = a.charAt(i);
            if(dictb.containsKey(currentchar)){
                if(dicta.get(currentchar) != dictb.get(currentchar)){
                    deletioncount += Math.abs(dictb.get(currentchar) - dicta.get(currentchar));
                }
            }
            else{
                deletioncount += dicta.get(currentchar);
            }
        }
        for(int i=0; i<dictb.size(); i++){
            char currentchar = b.charAt(i);
            if(dicta.containsKey(currentchar) == false){
                deletioncount += dictb.get(currentchar);
            }
        }
        return deletioncount;
    }

    public int findDeletion(String a, String b){
        Map<Character, Integer> dicta = MakeDict(a);
        Map<Character, Integer> dictb = MakeDict(b);
        int deletioncount = 0;
        deletioncount += findDeleteCount(a, b, dicta, dictb);
        return deletioncount;
    }

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Not Enough Arguments Given");
        } else {
            Anagram a = new Anagram();
            int output = a.findDeletion(args[0], args[1]);
            System.out.println(output);
        }
    }


}
