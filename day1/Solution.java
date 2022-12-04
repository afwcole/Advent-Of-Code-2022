package calories_day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void main(String[] args){
        try {
            FileReader fr = new FileReader("calories_day1\\calories.txt");
            BufferedReader br = new BufferedReader(fr);

            String line = br.readLine();

            int maxCalories = 0,  currentElfCalories = 0;
            List<Integer> allCalories = new ArrayList<>();

            while (line != null){
                if(line.isEmpty()){
                    maxCalories = Math.max(maxCalories, currentElfCalories);
                    allCalories.add(currentElfCalories);
                    currentElfCalories = 0;
                } else {
                    currentElfCalories += Integer.parseInt(line);
                }
                line = br.readLine();
            }

            maxCalories = Math.max(maxCalories, currentElfCalories);
            Collections.sort(allCalories);
            Collections.reverse(allCalories);

            int sumOfTop3Elves = 0;
            for (int i = 0; i < 3; i++){
                sumOfTop3Elves += allCalories.get(i);
            }

            System.out.println(maxCalories);
            System.out.println(sumOfTop3Elves);
            fr.close();
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
        
 
    }
}