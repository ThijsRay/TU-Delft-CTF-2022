#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// This is an array that keeps indexes into event_names. Every slot
// entry in array represents a 10 minute time slot in this month
int daily_slots[366];

char* BANNER =
 " __       __   ______   __    __  ________  ________  ______  \n"
 "/  \\     /  | /      \\ /  \\  /  |/        |/        |/      \\ \n"
 "$$  \\   /$$ |/$$$$$$  |$$  \\ $$ |$$$$$$$$/ $$$$$$$$//$$$$$$  |\n"
 "$$$  \\ /$$$ |$$ |  $$ |$$$  \\$$ |$$ |__       $$ |  $$ |__$$ |\n"
 "$$$$  /$$$$ |$$ |  $$ |$$$$  $$ |$$    |      $$ |  $$    $$ |\n"
 "$$ $$ $$/$$ |$$ |  $$ |$$ $$ $$ |$$$$$/       $$ |  $$$$$$$$ |\n"
 "$$ |$$$/ $$ |$$ \\__$$ |$$ |$$$$ |$$ |_____    $$ |  $$ |  $$ |\n"
 "$$ | $/  $$ |$$    $$/ $$ | $$$ |$$       |   $$ |  $$ |  $$ |\n"
 "$$/      $$/  $$$$$$/  $$/   $$/ $$$$$$$$/    $$/   $$/   $$/ \n\n"
 "   === Moneta : A not-so modern expense management tool ===   \n\n";
                                                               
char* MENU = 
"Please select an option:\n"
"\t1) Set totally spent money for a day\n"
"\t2) Show money spent daily in one month\n"
"\t3) Exit\n"
">> ";

int monthdays[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
char *monthnames[] = {"January",   "February", "March",    "April",
                      "May",       "June",     "July",     "August",
                      "September", "October",  "November", "December"};

typedef struct Date {
  unsigned int year;
  unsigned int month;
  unsigned int day;
} Date;

int isdatevalid(Date *date){
    if(date->month <= 0 || date->month > 12 || date->day < 0 || monthdays[date->month - 1] < date->day || date->year <= 0){
        return 0;
    }
    return 1;
}

int isleapyear(int year){
    if(year % 4 == 0){
        if(year % 100 == 0){
            return year % 400 == 0 ? 1 : 0;
        }
        return 1;
    }else{
        return 0;
    }
}

int compdates(Date* d1, Date* d2){
    if(d1->year > d2->year){
        return 1;
    }else if(d1->year == d2->year){
        if(d1->month > d2->month){
            return 1;
        }else if(d1->month == d2->month){
            if(d1->day >= d2->day){
                return 1;
            }
        }
    }
    return -1;
}

int datesubtract(Date* date, Date* date2){
    int sign = compdates(date, date2);
    if(sign == -1){
        Date* empty = date;
        date = date2;
        date2 = empty;
    }

    int days = 0;

    for(int i = 0; i < date->month - 1; i++){
        days += monthdays[i];
    }
    days += date->day + isleapyear(date->year);

    int days2 = 0;

    for(int i = 0; i < date2->month - 1; i++){
        days2 += monthdays[i];
    }

    days2 += date2->day + isleapyear(date2->year);

    int diff = days - days2;
    for(int i = date2->year; i < date->year; i++){
        diff += 365 + isleapyear(i);
    }

    return diff*sign;
}

Date* getdate(){
    Date *date = malloc(sizeof(Date));

    printf("Please enter date in format: DD-MM-YYYY: ");
    scanf("%u-%u-%u", &date->day, &date->month, &date->year);

    return date;
}

void printmonth(int* monthStart, Date* date){
    printf("    %u, ", date->year);
    puts(monthnames[date->month - 1]);
    for(int i = 0; i < monthdays[date->month-1]; i++){
        if(i%7 == 0){
            printf("\n  ");
        }
        printf("%d ", monthStart[i]);
    }
    printf("\n");
}

int main(){

    int option;
    Date* d;
    int diff;
    int amount;
    Date *yearstart;
    Date *current;

    time_t t = time(NULL);
    struct tm tm = *localtime(&t);

    printf(BANNER);

    yearstart = malloc(sizeof(Date));

    yearstart->year = tm.tm_year + 1900;
    yearstart->month = 1;
    yearstart->day = 0;

    current = malloc(sizeof(Date));

    current->year = tm.tm_year + 1900;
    current->month = tm.tm_mon + 1;
    current->day = tm.tm_mday;

    printf("Current Date: %u-%u-%u\n", current->day, current->month, current->year);

    do {
        printf(MENU);

        scanf("%d", &option);
        switch(option) {
            case 1:
                d = getdate();
                if(isdatevalid(d) == 0){
                    printf("Invalid Date!\n");
                    break;
                }
                diff = datesubtract(d, yearstart);
                printf("Enter the amount you have spent that day: ");

                amount = 0;
                scanf("%d", &amount);

                *(daily_slots + diff) = amount;
                break;
            case 2:
                d = getdate();
                if(isdatevalid(d) == 0){
                    printf("Invalid Date!\n");
                    break;
                }
                d->day = 0;

                int diff = datesubtract(d, yearstart);

                printmonth(daily_slots + diff, d);
                break;
            case 3:
                printf("Good Bye!\n");
                break;
            default:
                printf("Not a valid option!\n\n");
        }
    } while(option != 4);
}


