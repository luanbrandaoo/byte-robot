#ifndef DISPLAY_EYES_H
#define DISPLAY_EYES_H

#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>

// Constantes e variáveis específicas para a função displayEyes
extern int h;
extern int w;
extern int buffidx;

void neutralEyes(Adafruit_ST7735 &tft);
void happyEyes(Adafruit_ST7735 &tft);
void sadEyes(Adafruit_ST7735 &tft);

#endif // DISPLAY_EYES_H
