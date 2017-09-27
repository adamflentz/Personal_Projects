class Left_Rotation_Array {
    public int[] rotate(int number, int leftrotation){
        int[] arrayInput = new int[number];
        int[] arrayOutput = new int[number];
        for(int i = 0; i < number; i++){
            arrayInput[i] = i+1;
        }
        for(int i = 0; i < number; i++){
            arrayOutput[i] = arrayInput[(i + leftrotation) % number];
        }
        return arrayOutput;
    }
    public static void main(String[] args){
        if(args.length != 2){
            System.out.println("Not Enough Arguments Given");
        }
        else{
            Left_Rotation_Array array = new Left_Rotation_Array();
            int[] Array = array.rotate(Integer.valueOf(args[0]), Integer.valueOf(args[1]));
            for(int i=0; i < Array.length; i++){
                System.out.println(Array[i]);
            }
        }
    }
}