object nestedIfElse { 
      def main(args: Array[String]) { 
        var a: Int = 70
        var b: Int = 40
        var c: Int = 100  
        // condition_1 
        if (a > b)  
        { 
            // condition_2 
            if(a > c) { 
                println("a is largest"); 
            } 
            else{ 
                println("c is largest") 
            } 
        }
      }
}
