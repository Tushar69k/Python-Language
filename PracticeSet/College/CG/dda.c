// DDA ALGORITHM
#include <graphics.h>
#include <stdio.h>
#include <math.h>
void DDA(int x1, int y1, int x2, int y2) {
int dx = x2 -x1;
int dy = y2 - y1;
int steps = abs(dx) > abs(dy) ?
abs(dx) : abs(dy);
float Xinc = dx / (float) steps;
float Yinc = dy / (float) steps;
float x = x1;
float y = y1;
for (int i = 0;i <= steps; i++) {
putpixel(round(x), round(y).
WHITE); // plot pixel
x+= Xinc;
y += Yinc;
-
1
int main() {
int gd = DETECT, gm;
initgraph(&gd, &gm, NULL);
int ×1, y1, ×2, y2;
printf("Enter coordinates of first point
(x1 y1): ");
scanf("%d %d", &x1, &y1);
printf("Enter coordinates of second
point (x2 y2): ");
scanf("%d %d", &x2, &y2);
DDA(x1, y1, x2, y2);
getch();
closegraph0;
return 0;
1
-
Created with Mi Notes
