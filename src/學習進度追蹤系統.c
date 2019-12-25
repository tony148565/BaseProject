#include <stdio.h>
#include <stdlib.h>

int week[8][5][50] = {0}; //type4 check, week[day][timetype][value]
char name[8][50][101];

void printname(int j)
{
    FILE *fp1= fopen("file.txt", "a");
    int i,p,f=0;
    //fprintf(fp1,"\n");
    for(i=0; i<7; i++)
    {
        fprintf(fp1, "%s ",name[i][j]);
        /*
        if((name[i][j][0]='\0')||(week[i][0][j] == 24 && week[i][1][j] == 60 && week[i][2][j] == 24 && week[i][3][j] == 60))
        {
            fprintf(fp1, "|                   |");
        }
        else
        {
            fprintf(fp1, "|%s",name[i][j]);
            if(i!=6)
                fprintf(fp1, "                |");
        }
        */
    }
    fprintf(fp1, "  |\n");
}

void time(){
    FILE *fp1= fopen("file.txt", "a");
    int i,j,k,p;
    int f=0;
    for(j=1; j<50; j++)
    {
        for(i=0; i<7; i++)
        {
            if(week[i][0][j] != 0 && week[i][1][j] != 0 && week[i][2][j] != 0 && week[i][3][j] != 0)
            {
                if(week[i][0][j] == 24 && week[i][1][j] == 60 && week[i][2][j] == 24 && week[i][3][j] == 60)
                {
                    fprintf(fp1, "|                   |");
                }
                else
                {
                    fprintf(fp1, "|%3d:",week[i][0][j]);
                    fprintf(fp1, "%3d  ~",week[i][1][j]);
                    fprintf(fp1, "%3d:",week[i][2][j]);
                    fprintf(fp1, "%3d",week[i][3][j]);
                    if(i!=6)
                        fprintf(fp1, "  |");
                }

            }
        }
        printname(j);
        //fprintf(fp1, "\n");
        //if(week[i][0][j] != 00 && week[i][1][j] != 0 && week[i][2][j] != 0 && week[i][3][j] != 0)

    }
}

int main()
{
    FILE *fp1= fopen("file.txt", "w");
    //fprintf(fp, "a|b\n");//writing data into file

    int option;
    int i,j,k,p;
    int f=0;

    //while(1){}
    /*
    printf("請選擇功能(1輸入讀書計畫 2輸入完成情況): ");
    scanf("%d",&option);
    if(option==1)//輸入讀書計畫{}
    else if(option==2)//輸入完成情況{}
    */
    //*

    //*
    for(i=0; i<7; i++)
    {
        j=0;
        k=0;
        printf("星期%d",i+1);

        while(1)
        {
            printf("i=%d",i);
            printf("請輸入時間(xx:yy~xx:yy): ");
            scanf("%d%d%d%d",&week[i][0][j],&week[i][1][j],&week[i][2][j],&week[i][3][j]);
            //printf("%d %d %d %d\n",week[i][0][j],week[i][1][j],week[i][2][j],week[i][3][j]);//test
            //printf("a%d %d %d %d\n",week[i][0][j],week[i][1][j],week[i][2][j],week[i][3][j]);//test
            if(week[i][0][j] == 24 && week[i][1][j] == 60 && week[i][2][j] == 24 && week[i][3][j] == 60)
                break;
            if((week[i][0][j]>week[i][2][j])||(week[i][0][j]==week[i][2][j]&&week[i][1][j]>week[i][3][j]))
            {
                printf("Error\n");
                continue;
            }
            //printf("b%d %d %d %d\n",week[i][0][j],week[i][1][j],week[i][2][j],week[i][3][j]);//test
            printf("請輸入科目名稱: ");
            scanf("%s",name[i][k]);
            printf("%s\n",name[i][k]);
            k++;
            j++;
//	printf("c%d %d %d %d\n",week[0][0][3],week[0][1][3],week[0][2][3],week[0][3][3]);//test
//	}
//	printf("d%d %d %d %d\n",week[0][0][3],week[0][1][3],week[0][2][3],week[0][3][3]);//test
//	}
//	printf("e%d %d %d %d\n",week[0][0][3],week[0][1][3],week[0][2][3],week[0][3][3]);//test
            //fwrite(week,1,sizeof(week),fp1);
            //*/
        }
    }

    for(i=0; i<7; i++)
        fprintf(fp1,"|       星期%d       |",i+1);
    fprintf(fp1,"\n");

        for(i=0; i<7; i++)
        {
            if(week[i][0][0] != 0 && week[i][1][0] != 0 && week[i][2][0] != 0 && week[i][3][0] != 0)
            {
                if(week[i][0][0] == 24 && week[i][1][0] == 60 && week[i][2][0] == 24 && week[i][3][0] == 60)
                {
                    for(p=0; p<7; p++)
                        f=1;
                    if(f!=0)
                        fprintf(fp1, "|                   |");
                }
                else
                {
                    fprintf(fp1, "|%3d:",week[i][0][0]);
                    fprintf(fp1, "%3d  ~",week[i][1][0]);
                    fprintf(fp1, "%3d:",week[i][2][0]);
                    fprintf(fp1, "%3d",week[i][3][0]);
                    if(i!=6)
                        fprintf(fp1, "  |");
                }

            }
        }

        //if(week[i][0][j] != 00 && week[i][1][j] != 0 && week[i][2][j] != 0 && week[i][3][j] != 0)
        fprintf(fp1, "  |\n");
        printname(j);
        time();

    fclose(fp1);//closing file

    return 0;
}
/*
fprintf(fp1, "%s",name[i][j]);
1 1 1 1
aaa
24 60 24 60
2 2 2 2
bbb
24 60 24 60
3 3 3 3
ccc
4 4 4 4
ddd
24 60 24 60
24 60 24 60
24 60 24 60
24 60 24 60
5 5 5 5
eee
24 60 24 60

24 60 24 60
24 60 24 60
24 60 24 60
24 60 24 60
24 60 24 60
24 60 24 60
24 60 24 60

*/

