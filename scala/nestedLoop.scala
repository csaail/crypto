object nestedLoop{     
  def main(args: Array[String]) {
    var a = 5;
    var b = 0; 
    while (a < 7) {
       b = 0;
       while (b < 7 ) 
       {
         println("Value of a = " +a, " b = "+b);
         b = b + 1;
       }
      
       println()
       a = a + 1;
       println("Value of a Become: "+a);
       println()
    } 
  }
}
