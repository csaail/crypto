// Scala program to create an ArrayBuffer 
// ArrayBuffer class is imported 
import scala.collection.mutable.ArrayBuffer 

object GFG {  
    def main(args: Array[String]) { 
      	var name = ArrayBuffer[String]() 
      	name += "GeeksForGeeks"
      	name += "gfg"
      	name += "Chandan"
      	println(name) 
        // accessing 1th index element of arraybuffer 
        println(name(1))
        // adding one or more element using append method  
        name.append("S-series", "Ritesh")  
        // printing arraybuffer 
        println(name) 
        name.remove(1, 3) 
        // printing resultant arraybuffer 
        println(name)  
  }   
} 
