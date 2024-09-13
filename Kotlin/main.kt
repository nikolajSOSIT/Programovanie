class Car(var brand: String, var model: String, var year: Int) {
  // Class function
  fun drive() {
    println("Wrooom!")
  }
}

fun main() {
  val c1 = Car("Ford", "Mustang", 1969)
  
  // Print property values
  println(c1.brand + " " + c1.model + " " + c1.year)
  
  // Call the function
  c1.drive()  
}