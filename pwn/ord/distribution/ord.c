#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <stdlib.h>

#define FORMAT "%FT%T"
#define DAY 86400
#define YEAR DAY * 365

void setup(){
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
}

int* get_int_ptr(){
    return malloc(4);
}

int main(){
    char buf[100];
    int *now = get_int_ptr();
    int *enlistment = get_int_ptr();
    int *ord = get_int_ptr();
    struct tm *time_struct = NULL;

    setup();


    time(now);
    time_struct = localtime(now);
    strftime(buf, 100, FORMAT, time_struct);
    printf("Enter enlistment date in ISO-8601 format (eg the time now is %s): ", buf);
    fgets(buf, 100, stdin);

    // Parse input
    strptime(buf, FORMAT, time_struct);

    *enlistment = mktime(time_struct);


    if(*enlistment < *now){
        puts("Sorry, only future dates allowed");
        exit(0);
    }

    *ord = *enlistment + 2 * YEAR;

    time_struct = localtime(ord);
    strftime(buf, 100, FORMAT, time_struct);
    printf("ORD date: %s\n", buf);


    while(*now < *ord){
        time(now);
        // :(
        sleep(DAY);
    }

    puts("ORD loh!");
    system("cat flag.txt");

    free(now);
    free(enlistment);
    free(ord);
}
