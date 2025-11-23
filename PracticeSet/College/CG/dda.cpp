#include <graphics.h>
#include <iostream>
#include <cmath>
using namespace std;

// Function for DDA Line Drawing Algorithm
void DDA(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;

    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);

    float Xinc = dx / (float) steps;
    float Yinc = dy / (float) steps;

    float x = x1;
    float y = y1;

    for (int i = 0; i <= steps; i++) {
        putpixel(round(x), round(y), WHITE); // Plot the pixel
        x += Xinc;
        y += Yinc;
        delay(10); // Slow down for visualization
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);

    int x1, y1, x2, y2;
    cout << "Enter coordinates of first point (x1 y1): ";
    cin >> x1 >> y1;
    cout << "Enter coordinates of second point (x2 y2): ";
    cin >> x2 >> y2;

    DDA(x1, y1, x2, y2);

    getch();
    closegraph();
    return 0;
}
