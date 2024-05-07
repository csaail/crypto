object tuple {
	def main(args: Array[String]){ 
    var name = (15, "chandan", true)
		println(name._1) // print 1st element
		println(name._2) // print 2nd element
		println(name._3) // print 3st element
    //pattern matching
    var (a,b,c) = (15, "chandan", true)
    println(a)
    println(b)
    println(c)
    println(name.toString())
	}
}
