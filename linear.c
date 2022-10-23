#include <stdio.h>
#include <string.h>
float solve(float a, float b){
   float c;
   if(a == 0){
      printf("value of c cannot be predicted
");
   }else{
      c = -b / a;
   }
   return c;
}
int main(){
   float a, b, c;
   printf("
 enter a,b values: ");
   scanf("%f%f", &a, &b);
   c = solve(a, b);
   printf("
 linear eq of one variable in the form of ax+b = 0, if a=%f,b=%f,then x=    %f",a,b,c);
   return 0;
}
