using Gtk;

class Program
{
    public static void Main()
    {
        Application.Init();
        var window = new Window("Hello, GTK# Window!");
        window.Resize(400, 300);
        window.DeleteEvent += (o, args) => Application.Quit();
        window.ShowAll();
        Application.Run();
    }
}
