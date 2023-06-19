// PRINT HELLO WORLD

#include <iostream>
using namespace std;
int main() {
  cout << "Hello World!";
}



// PRINT HELLO WORLD

#include <iostream>
using namespace std;
int main() {
  cout << "Hello"<<"World!";
}




// PRINT PHYSICS WALLAH

#include <iostream>
using namespace std;
int main() {
  printf("Physics\nWallah");
}



// SUM  OF THE NUMBER GIVEN  BY USER

#include <iostream>
using namespace std;
int main() {
  int n1, n2, sum;
  cout << "enter the number= ";
  cin >> n1;
  cout << "enter the number= ";
  cin >> n2;
  sum = n1 + n2;
  cout << sum << endl;
  return 0;
}




// Take 2 integer values in two variables x and y and print their product.

#include <iostream>
using namespace std;
int main() {
  int X, Y, Pr;
  cout << "enter the number=";
  cin >> X;
  cout << "enter the number=";
  cin >> Y;
  Pr = X * Y;
  cout << Pr << endl;
  return 0;
}




// TAKE A LENGTH AND BREADTH OF A RECTANGLE AND FIND AREA.

#include <iostream>
using namespace std;
int main()
{
  int length, breadth, area;
  cout<<"Length=";
  cin>>length;
  cout<<"Breadth=";
  cin>>breadth;
  area=length*breadth;
  cout<<"Area="<<area;
  return 0;
}





// CALCULATE THE CUBE OF A NUMBER

#include <iostream>
using namespace std;
int main() {
  int a, cube;
  cout << "Enter the number = ";
  cin >> a;
  cube = a * a * a;
  cout << "Cube = " << cube;
  return 0;
}





// FIND THE SIZE OF DATA

#include <iostream>
using namespace std;
int main() {
  cout << "Size of basic data type in bytes\n";
  cout << "The size of int data type = " << sizeof(int) << " bytes \n";
  cout << "The size of char data type = " << sizeof(char) << " bytes \n";
  cout << "The size of bool data type = " << sizeof(bool) << " bytes \n";
  cout << "The size of wchar_t data type = " << sizeof(wchar_t) << " bytes \n";
  cout << "The size of float data type = " << sizeof(float) << " bytes \n"; 
  cout << "The size of double data type = " << sizeof(double) << " bytes \n";
   return 0;
}



// SWIFE THE TWO NUMBER BY THIRD NUMBER

#include <iostream>
using namespace std;
int main() {
  int n1, n2, n3;
  cout << "Enter the first number = ";
  cin >> n1;
  cout << "Enter the second number = ";
  cin >> n2;
  n3 = n2;
  n2 = n1;
  n1 = n3;
  cout << "The first number = " << n1 << "\n";
  cout << "The second number = " << n2 << "\n";
  return 0;
}




// FIND THE ADD, SUB,MULTIPLY AND SUBSTRACTION OF GIVEN 2 INTEGERS

#include <iostream>
using namespace std;
int main() {
  int n1, n2, sum, div, mul, squ, cube, divi;
  cout << "Enter the number = ";
  cin >> n1;
  cout << "Enter the number = ";
  cin >> n2;
  sum = n1 + n2;
  div = n1 - n2;
  mul = n1 * n2;
  divi = n1 / n2;
  squ = div * div;
  cube = div * div * div;
  cout << "Sum = " << sum << "\n";
  cout << "Divide = " << div << "\n";
  cout << "Multiply = " << mul << "\n";
  cout << "Square = " << squ << "\n";
  cout << "Cube = " << cube << "\n";
  cout << "Division = " << divi << "\n";
  return 0;
}



// EXCHANGE THE VALUE OF VARIABLE

#include <iostream>
using namespace std;
int main() {
  int apple = 4;
  cout << apple;
  apple = 10;
  cout << apple;
  return 0;
}

// EXCHANGE THE VALUE OF VARIABLE

#include <iostream>
using namespace std;
int main() {
int rate = 50;
rate = 60;
cout<<rate; 
return 0;
}




// USE OF << (LEFT SHIFT)

#include <iostream>
using namespace std;
int main(void)
{
  int a,B, sum;
  cout<<"enter the number = ";
  cin>>a;
  sum=a<<2;
  cout<<B;
return 0;
}




// USE OF COMMA OPERATOR

#include <iostream>
using namespace std;
int main(void) {
  int a = (2, 3, 9);
  cout << a << endl;
  return 0;
}



// USE OF POST INCREAMENT AND PRE INCREAMENT OPERATOR

 #include <iostream>
 using namespace std;
 int main()
 {
   int a = 6;
   cout << (a++) << endl ;
   int b=86;
   cout<<(--b)<< endl;
   cout<<(++a)<< endl;
 return 0;
 }



