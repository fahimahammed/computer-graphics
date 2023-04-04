#include<graphics.h>
int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");
    
    setcolor(GREEN);
    rectangle(100, 50, 400, 230);
    setfillstyle(SOLID_FILL,GREEN);
    floodfill(101,51,GREEN);

    setcolor(RED);
    circle(235, 140, 60);
    setfillstyle(SOLID_FILL,RED);
    floodfill(236, 141, RED);

    setcolor(WHITE);
    rectangle(90, 40, 99, 450);
    setfillstyle(1, WHITE);
    floodfill(91, 41, WHITE);

    setcolor(WHITE);
    outtextxy(200, 455, "National Flag of Bangladesh");

    getch();
    closegraph();
    return 0;
}