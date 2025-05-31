import java.util.*;
public class customCompare {
    public static void main(String[] args) {


       Comparator com = new Comparator() {
           @Override
           public int compare(Object o1, Object o2) {
               String s1 = (String) o1;
               String s2 = (String) o2;
               if (s1.length() > s2.length())
                   return 1;
               else
                   return  -1;
           }
       };

        List<String> l = new ArrayList<>();


        l.add("Gowtham");
        l.add("Sai");
        l.add("Manoj");
        l.add("Jalam Uma");
        l.add("Sourya");

        Collections.sort(l, com);

        System.out.println(l);



    }
}
