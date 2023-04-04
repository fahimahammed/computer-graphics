#include<graphics.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>

int main()
{
    int gd = DETECT;
    int gm;
    initgraph(&gd,&gm,(char*)"");

    int refX  = 50, refY = 200, x = 500, y = 50;
    double rotationAngle;
    printf("Enter rotation angle (clock wise): ");
    scanf("%lf", &rotationAngle);

    // original line
    line(refX, refY, x, y);
    
    rotationAngle = (rotationAngle * 3.1416) / 180;

    // x' = x0 + (xn - x0) * cos(angle) - (yn - y0)*sin(angle)
    // y' = y0 + (xn - x0) * sin(angle) + (yn - y0)*cos(angle)
    int x1 = refX + (x - refX) * cos(rotationAngle) - (y - refY) * sin(rotationAngle);
    int y1 = refY + (x - refX) * sin(rotationAngle) + (y - refY) * cos(rotationAngle);

    setcolor(RED);
    line(refX, refY, x1, y1);

    getch();
    closegraph();
    return 0;
}