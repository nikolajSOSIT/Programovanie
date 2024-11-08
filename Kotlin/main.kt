import javax.swing.JFrame
import javax.swing.JLabel
import javax.swing.SwingConstants
import java.awt.Dimension

fun main() {
    // Create a new JFrame (window) and set its properties
    val frame = JFrame("Kotlin Graphic Window Example")
    frame.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
    frame.setSize(400, 300)
    frame.preferredSize = Dimension(400, 300)

    // Create a JLabel to display text
    val label = JLabel("Hello, Kotlin Graphics!", SwingConstants.CENTER)
    frame.add(label)

    // Center the window and make it visible
    frame.setLocationRelativeTo(null)
    frame.isVisible = true
}
