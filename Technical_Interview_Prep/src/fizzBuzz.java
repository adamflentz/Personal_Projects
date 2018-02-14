public class fizzBuzz{
    public void fizzBuzzFunction (int start, int finish){
        String fizz = "fizz";
        String buzz = "buzz";
        for(int i = start; i <= finish; i++){
            if(start % 5 == 0 && start % 3 == 0){
                System.out.println(fizz + buzz);
            }
            else if (start % 3 == 0){
                System.out.println(fizz);
            }
            else if (start % 5 == 0){
                System.out.println(buzz);
            }
            else{
                System.out.println(start);
            }
        }
    }

    public static void main(String[] args){
        if(args.length != 3){
            System.out.println("wrong number of arguments");
        }
        else{
            fizzBuzz fizzBuzz = new fizzBuzz();
            int start = Integer.parseInt(args[1]);
            int finish = Integer.parseInt(args[2]);
            fizzBuzz.fizzBuzzFunction(start, finish);
        }
    }
}