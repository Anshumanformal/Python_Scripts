#include<stdio.h>
#include<stdlib.h>
void alkane();
void alkene();
void alkyne();
void ask_exit();

int c = 0,hc = 0,h = 0;

int main(){

while(1){
printf("Enter the desired hydrocarbon:\n\n1. Alkane\n2. Alkene\n3. Alkyne\n");
scanf("%d",&hc);
if(hc > 3 || hc < 0){
	printf("Enter correct number from 1 to 3!");
	continue;
}
else{
while(1){
printf("\nEnter the number of carbons upto 10.\n");
scanf("%d",&c);
if(c > 10){
	printf("Number of carbons out of range of 10!");
	continue;
}
else{
	break;
}
}


switch(hc){
	case 1:{
		alkane();
		break;
	}
	case 2:{
		alkene();
		break;
	}
	case 3:{
		alkyne();
		break;
	}
}
}

}
return 0;
}


void ask_exit(){
	char exit_choice;
	printf("Do you want to exit the program?\nPress y or Y to exit.\nPress anything else to continue\n.");
	scanf("%c",&exit_choice);
	if(exit_choice == 'y' || exit_choice == 'Y'){
		printf("\n");
		exit(0);
	}
	else{
		return;
	}
}


void alkane(){
	h = 2*c + 2;
	printf("The hydrocarbon is: C%dH%d\n\n",c,h);
	ask_exit();
}

void alkene(){
	h = 2*c;
	printf("The hydrocarbon is: C%dH%d\n\n",c,h);
	ask_exit();
}

void alkyne(){
	h = 2*c - 2;
	printf("The hydrocarbon is: C%dH%d\n\n",c,h);
	ask_exit();
}
