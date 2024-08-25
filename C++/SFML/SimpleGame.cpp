#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <SFML/Window.hpp>

int main() {
    sf::RenderWindow window(sf::VideoMode(200,200), "SFML Works!");
    sf::CircleShape shape(100.0f);
    shape.setFillColor(sf::Color::Green);

    while(window.isOpen()) {    
        sf::Event e;
        while (window.pollEvent(e))
        {
            if(e.type == sf::Event::Closed)
                window.close();
        }
        window.clear();
        window.draw(shape);
        window.display();
    }
    return 0;
}