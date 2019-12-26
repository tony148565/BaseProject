#include <stdio.h>
#include <stdlib.h>
struct subject
{
    //int h1,m1,h2,m2,w;
    char sub[100];
    int check;
} subject;

typedef struct subject Subject;

int main()
{
    int option=1;
    int i,j=0,k=8,p,q=0;

    Subject a[120];
    while(1){
    if(q==1){
    	printf("請選擇功能(1輸入讀書計畫 2輸入完成情況 3離開): ");
    	scanf("%d",&option);
	}
    
    if(option==1)//輸入讀書計畫
    {
    	FILE *fp1= fopen("file.txt", "w");
        ///input
        for(i=0; i<7; i++)
        {
            k=0;
            printf("星期%d\n",i+1);

            for(p=0; p<16; p++)
            {
                printf("請輸入科目名稱(無就輸入no): ");
                scanf("%s",a[j].sub);
                //fprintf(fp3,"%s,",a[j].sub);
                j++;
            }
        }
///print the file
        fprintf(fp1,"|     |",i+1);
        for(i=8; i<24; i++)
            fprintf(fp1,"|%02d:10~%02d:00|",i,i+1);
        fprintf(fp1,"\n");
///time
        p=0;
        for(i=0; i<7; i++)
        {
            for(j=0; j<16; j+=1)
            {
                if(j==0)
                    p=1;
                if(p==1)
                    fprintf(fp1,"|星期%d|",i+1);
                if(a[j].sub[0]=='n'&&a[j].sub[1]=='o')
					fprintf(fp1,"|           |",a[j].sub);
				else
					fprintf(fp1,"|%11s|",a[j].sub);
                if(j==15)
                {
                    fprintf(fp1, "\n");
                }
                p=0;
            }
        }
        fprintf(fp1, "\n");
        q=1;
        fclose(fp1);
    }
    
    else if(option==2)//輸入完成情況
	{
		FILE *fp2= fopen("file1.txt", "w");
		for(i=0; i<7; i++)///input
        {
            k=0;
            printf("星期%d\n",i+1);
            //for(q=0;q<16;q++){
            	for(j=0; j<16; j++)
	            {
					printf("|%02d:10~%02d:00|\n",j+8,j+9);
	                printf("請輸入是否完成(0:no/1:yes): ");
	                scanf("%d",&a[j].check);
	            }
			//}
        }
        ///print the file
        ///做好的不印，沒做的印 
        fprintf(fp2,"|     |",i+1);
        for(i=8; i<24; i++)
            fprintf(fp2,"|%02d:10~%02d:00|",i,i+1);
        fprintf(fp2,"\n");
///time
        p=0;
        for(i=0; i<7; i++)
        {
            for(j=0; j<16; j+=1)
            {
                if(j==0)
                    p=1;
                if(p==1)
                    fprintf(fp2,"|星期%d|",i+1);
                if(a[j].check==0){
                	fprintf(fp2,"|%11s|",a[j].sub);
				}
                else{
                	fprintf(fp2,"|           |",a[j].sub);
				}
                if(j==15)
                {
                    fprintf(fp2, "\n");
                }
                p=0;
            }
        }
        fprintf(fp2, "\n");
        fclose(fp2);
    }
    
    else if(option==3) return 0;
	}

    //fclose(fp1);//closing file
    //fclose(fp2);    

    return 0;
}
/*
a
b
c
d
e
f
g
h
i
j
k
l
m
o
p
no

1
1
0
1
0
1
1
0
0
1
1
1
1
1
1
1
 
*/
//if(a[j].h1 == 24 && a[j].m1 == 60 && a[j].h2 == 24 && a[j].m2 == 60)
