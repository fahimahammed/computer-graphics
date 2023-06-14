//#include <iostream>
#include<graphics.h>
#include<stdio.h>
#include<conio.h>

int main()
{
    int gd = DETECT;
    int gm;
    initgraph(&gd,&gm, (char*)"");

    // line(50,150,113,150); 
    // line(50,150,100,50); 
    // line(100,50,150,113);

    // setcolor(WHITE);
    // arc(170,170,0,270,60);
    // circle(170,170,60);

    // rectangle(170,170,290,290);


    setcolor(WHITE);
    line(50,150,150,150);
    line(50,150,100,50);
    line(100,50,150,150);
    setfillstyle(SOLID_FILL,BLACK);
    floodfill(80,148,WHITE);

    setcolor(YELLOW);
    circle(170,170,80);
    setfillstyle(SOLID_FILL,BLACK);
    floodfill(171,171,YELLOW);

    setcolor(WHITE);
    rectangle(170,170,290,290);
    setfillstyle(SOLID_FILL,BLACK);
    floodfill(289,289,WHITE);

    getch();
    return 0;
}