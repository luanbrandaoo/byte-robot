#ifndef DISPLAY_ICONS_H
#define DISPLAY_ICONS_H

#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>

extern Adafruit_ST7735 tft;

void searchIcon();
void loadingIcon();
void blackScreen();
void neutralEyes(Adafruit_ST7735 &tft);
void happyEyes(Adafruit_ST7735 &tft);
void sadEyes(Adafruit_ST7735 &tft);

#endif // DISPLAY_ICONS_H
