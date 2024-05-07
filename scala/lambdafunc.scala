object lambda{ 
  def main(args:Array[String]) { 
  	val ex1 = (x:Int) => x + 2	 
  	val ex2 = (x:Int, y:Int) => x * y 
  	println(ex1(7)) 
  	println(ex2(2, 3)) 
  } 
} 
