import scala.collection.mutable.HashMap 
object Geeks { 
	def main(args: Array[String]) { 
		var hashMap = HashMap("C"->"Csharp", "S"->"Scala", "J"->"Java") 
		hashMap.foreach{ 
			case (key, value) => println (key + " -> " + value)		 
		} 	
		hashMap -= "C"		
		println("After Removing") 
		hashMap.foreach { 
			case (key, value) => println (key + " -> " + value) 
		} 
	} 
} 
