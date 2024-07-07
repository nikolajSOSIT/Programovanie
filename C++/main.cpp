#include "raylib.h"
#include <string>

int main() {
	const int width = 300;
	const int height = 600;

	InitWindow(width, height, "Hello");

	while (!WindowShouldClose()){
		BeginDrawing();
		ClearBackground(RAYWHITE);
		int x = 0;
		int y = 0;
		for (int i = 0; i < 51; i++)
		{
			unsigned char r = i * 5;
			Color color = {r,r, 0, 255};
			DrawRectangle(x, y, x+5, 300, color);	
			x += 5;
		}
		EndDrawing();
	}
	return 0;
}