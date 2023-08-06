#include "move.h"
#include <Arduino.h>

void movefront() {
    digitalWrite(2, LOW);
    digitalWrite(3, HIGH);
    digitalWrite(5, LOW);
    digitalWrite(7, HIGH);
    delay(200);
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(5, LOW);
    digitalWrite(7, LOW);
}

void moveback() {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(5, HIGH);
    digitalWrite(7, LOW);
    delay(200);
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(5, LOW);
    digitalWrite(7, LOW);
}

void moveright() {
    digitalWrite(2, LOW);
    digitalWrite(3, HIGH);
    digitalWrite(5, HIGH);
    digitalWrite(7, LOW);
    delay(200);
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(5, LOW);
    digitalWrite(7, LOW);
}

void moveleft() {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(5, LOW);
    digitalWrite(7, HIGH);
    delay(200);
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(5, LOW);
    digitalWrite(7, LOW);
}

void stopmove() {
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(5, LOW);
    digitalWrite(7, LOW);
}