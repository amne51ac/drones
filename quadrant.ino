#include <math.h>
int NWPin = 0;
int NEPin = 1;
int SEPin = 2;
int SWPin = 3;
int NWval;
int NEval;
int SEval;
int SWval;
int Y;
int X;
int intensity;
int acardinal;
int cardinal;
int truecard;
const float pi = 3.14159265359;


void setup() {
Serial.begin(9600);
}

void loop() {
NWval=analogRead(NWPin);
NEval=analogRead(NEPin);
SEval=analogRead(SEPin);
SWval=analogRead(SWPin);

Y = ((NEval + NWval)/2) - ((SEval + SWval)/2);
X = ((NEval + SEval)/2) - ((NWval + SWval)/2);

if (X==0)
{acardinal=90;}
else
{intensity = pow((pow(X,2)+pow(Y,2)),0.5);
acardinal = abs(atan(Y/X));}

if (Y > 0 && X > 0)
{cardinal = acardinal * (180 / pi);}
      else if (Y > 0 && X < 0)
      {cardinal = (pi - acardinal) * (180 / pi);}
      else if (Y < 0 && X < 0)
      {cardinal = (pi + acardinal) * (180 / pi);}
      else if (Y < 0 && X > 0)
      {cardinal = ( pi * 2 - acardinal) * (180 / pi);}
      else if (X == 0 && Y > 0)
      {cardinal = 90;}
      else if (X == 0 && Y < 0)
      {cardinal = 270;}
      else if (Y == 0 && X > 0)
      {cardinal = 0;}
      else if (Y == 0 && X < 0)
      {cardinal =180;}
      else if (Y == 0 && X == 0)
      {intensity = 0;
      cardinal = 90;}

truecard = (-(cardinal-90)) % 360;


Serial.print(" NW value : ");
Serial.println(NWval);
Serial.print(" NE value : ");
Serial.println(NEval);
Serial.print(" SE value : ");
Serial.println(SEval);
Serial.print(" SW value : ");
Serial.println(SWval);
Serial.print(" acardinal : ");
Serial.println(acardinal);
Serial.print(" cardinal : ");
Serial.print(cardinal);
Serial.print(" truecard : ");
Serial.print(truecard);
}
