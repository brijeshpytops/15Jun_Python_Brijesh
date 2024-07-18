#include<stdio.h>

void main(){
   char new_[] = "sample.txt";

   int res = remove(new_);

   if (res == 0){
    printf("File deleted successfully");
   } else {
   printf("Opps, something went wrong");
   }
}
