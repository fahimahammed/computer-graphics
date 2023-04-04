#include<graphics.h>
#include<stdio.h>
#include<conio.h>

int n, x[100], y[100], xShift, yShift;

void drawPolygon(){
    for(int i=0; i<n; i++){
        line(x[i], y[i], x[(i+1)%n], y[(i+1)%n]);
    }
}

void translatePolygon(){
    for(int i=0; i<n; i++){
        x[i] += xShift;
        y[i] += yShift;
    }
}

int main()
{
    int gd = DETECT;
    int gm;
    initgraph(&gd,&gm,(char*)"");

    printf("Enter number of Vertex: ");
    scanf("%d",&n);

    printf("Enter all vertex in clockwise direction:\n| x | y |)\n");
    for(int i =0; i<n; i++)
    {
        scanf("%d %d", &x[i], &y[i]);
    }
    printf("Enter Translation Factor:\n| xShift | yShift |\n");
    scanf("%d %d",&xShift,&yShift);
    cleardevice();
    drawPolygon();
    translatePolygon();
    setcolor(RED);
    drawPolygon();

    getch();
    closegraph();
    return 0;
}
/*
Input: 4
    50 50
    100 50
    100 100
    50 100
    xShift yShift
    25 25
*/