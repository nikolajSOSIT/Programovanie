#include <raylib.h>
#include <windows.h>
#include <iostream>

int main()
{
    InitWindow(300, 600, "Tetris");
    SetTargetFPS(60);

    while (!WindowShouldClose()) 
    {
        BeginDrawing();

        for (int i = 0; i < 256; i++)
        {
            Color color = {i, 0, 0, 255};
            DrawRectangle(50, 50, 10, 10, color);
            Sleep(1000);
        }
        EndDrawing();
    }
}