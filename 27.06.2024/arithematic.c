include <stdio.h>
int main(){
    char s;
    int x,y;
    printf("Enter the character");
    scanf("%c",&s);
    printf("Enter two numbers");
    scanf("%d%d",&x,&y);
    switch(s){
        case '+':
        printf("%d",x+y);
        break;
        case '-':
        printf("%d",x-y);
        break;
        case '*':
        printf("%d",x*y);
        break;
        case '/':
        printf("%d",x/y);
        break;
    }
    return 0;
}
