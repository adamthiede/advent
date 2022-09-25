#include <stdio.h>
#include <stdlib.h>

int part1(){
	FILE *fin;
	char *text;
	long numbytes;
	fin=fopen("7.txt","r");
	fseek(fin,0L,SEEK_END);
	numbytes=ftell(fin);
	fseek(fin,0L,SEEK_SET);
	text=(char*)calloc(numbytes,sizeof(char));
	if(text==NULL){
		return 1;
	}
	fread(text,sizeof(char),numbytes,fin);
	fclose(fin);

	printf("%d",text[0]);

	return 0;
}

int main(){
	int x=part1();
	printf("%i\n",x);
	return 0;
}
