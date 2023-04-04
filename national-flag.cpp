//#include <iostream>
#include<graphics.h>
#include<stdio.h>
#include<conio.h>

int main()
{
    int gd = DETECT;
    int gm;
    initgraph(&gd,&gm, (char*)"");

    setcolor(GREEN);
    rectangle(50,50,250,170);
    setfillstyle(SOLID_FILL,GREEN);
    floodfill(51,51,GREEN);

    setcolor(WHITE);
    rectangle(40,40,50,300);
    setfillstyle(SOLID_FILL,WHITE);
    floodfill(41,41,WHITE);

    setcolor(RED);
    circle(150,110,40);
    setfillstyle(SOLID_FILL,RED);
    floodfill(131,101,RED);

    getch();
    //delay(500000);
    closegraph();
    return 0;
}