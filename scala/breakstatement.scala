import scala.util.control.Breaks._

object breakstatement{
  def main(args: Array[String]) {
    breakable { 
  		for (a <- 1 to 10){
  			if (a == 6)
          break 
  			else
  			  println(a);
  		}
  	}
  }
}
