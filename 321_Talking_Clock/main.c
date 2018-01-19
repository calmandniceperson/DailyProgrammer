// Author(s): Michael Koeppl

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char *number_words[] = {"twelve", "one", "two", "three", "four", "five", "six",
                    "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
                    "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                    "nineteen"};
const char *minutes_ten_steps_words[] = {"twenty", "thirty", "forty", "fifty"};

const char *base = "It's ";

const char *INPUT_FILE_PATH = "./input.txt";

void attach_hour(char **dest, int *hour) {
    if (*hour <= 12) {
        strcat(*dest, number_words[*hour]);
    } else {
        strcat(*dest, number_words[*hour - 12]);
    }
}

void attach_minutes(char **dest, int *minutes) {
    if (*minutes > 0) {
        if (*minutes >= 20) {
            // Split the minute into two parts, so 31 becomes 3 and 1
            // This allows us to build the number string.
            char *minute_parts = malloc(2);
            sprintf(minute_parts, "%d", *minutes);
            int major = minute_parts[0] - '0';
            int minor = minute_parts[1] - '0';

            // At the major part in any case.
            strcat(*dest, " ");
            strcat(*dest, minutes_ten_steps_words[major-2]);

            // Add the minor part as well if it's not 0.
            if (minor > 0) {
                strcat(*dest, " ");
                strcat(*dest, number_words[minor]);
            }
        } else if (*minutes > 10 && *minutes < 20) {
            strcat(*dest, " ");
            strcat(*dest, number_words[*minutes]);
        } else {
            // If we have a minute 0 < m <= 10, we put an 'oh' before the minute
            // string, as in "two oh five pm".
            strcat(*dest, " oh ");
            strcat(*dest, number_words[*minutes]);
        }
    }
}

void attach_am_pm(char **dest, int *hour) {
    if (*hour <= 11) {
        strcat(*dest, " am");
    } else {
        strcat(*dest, " pm");
    }
}

int main(int argc, char **argv) {
    FILE* input_file = fopen(INPUT_FILE_PATH, "r");
    if (input_file == NULL) {
        fprintf(stderr, "Failed to open input file\n");
        return -1;
    }

    // 7 bytes (5 for characters, 2 for newline)
    size_t line_size = 7;
    char *line = malloc(line_size);

    while (fgets(line, line_size, input_file) != NULL) {
        int hour = (line[0] - '0') * 10 + (line[1] - '0');
        int minutes = (line[3] - '0') * 10 + (line[4] - '0');
        
        char *time_str = malloc(1024);
        strcat(time_str, base);

        attach_hour(&time_str, &hour);   
        attach_minutes(&time_str, &minutes);
        attach_am_pm(&time_str, &hour);
        
        printf("%s\n", time_str);
    }
    free(line);
    fclose(input_file);

    return 0;
}