import scala.collection.immutable._
object GFG { 
	def main(args:Array[String]) 
	{ 
		val mylist = List("C", "C#", "Java", "Scala","PHP", "Ruby") 
		println("The head of the list is:") 
		println(mylist.head) 
		println("List is empty or not:") 
        	println(mylist.isEmpty)
		println("Reverse list:" + mylist.reverse) 
	} 
}	 
