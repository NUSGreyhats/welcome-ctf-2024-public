#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {

	char flag[45];
	flag[0] = 'g';
	flag[1] = 'r';
	flag[2] = 'e';
	flag[3] = 'y';
	flag[4] = '{';
	flag[5] = 's';
	flag[6] = 't';
	flag[7] = 'a';
	flag[8] = 'c';
	flag[9] = 'k';
	flag[10] = '_';
	flag[11] = 's';
	flag[12] = 't';
	flag[13] = 'r';
	flag[14] = 'i';
	flag[15] = 'n';
	flag[16] = 'g';
	flag[17] = 's';
	flag[18] = '_';
	flag[19] = 'a';
	flag[20] = 'r';
	flag[21] = 'e';
	flag[22] = '_';
	flag[23] = 'n';
	flag[24] = 'o';
	flag[25] = 't';
	flag[26] = '_';
	flag[27] = 'v';
	flag[28] = 'e';
	flag[29] = 'r';
	flag[30] = 'y';
	flag[31] = '_';
	flag[32] = 's';
	flag[33] = 't';
	flag[34] = 'r';
	flag[35] = 'i';
	flag[36] = 'n';
	flag[37] = 'g';
	flag[38] = 's';
	flag[39] = 'a';
	flag[40] = 'b';
	flag[41] = 'l';
	flag[42] = 'e';
	flag[43] = '}';
	flag[44] = 0;

	char input[48];
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	printf("flag? ");
	read(STDIN_FILENO,input, 48);
	if (!strncmp(input, flag, 44)) {
		puts("correct");
	} else {
		puts("wrong");
	}


}
