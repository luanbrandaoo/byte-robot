#ifndef DISPLAY_IMAGE_H
#define DISPLAY_IMAGE_H

#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>

#define TFT_CS     10
#define TFT_RST    8
#define TFT_DC     9

extern const int BUFFER_SIZE;
extern char buf[];
extern int num_pixels;
extern int current_pixel;
extern bool isSendingImage;

void displayUpdate(Adafruit_ST7735 &tft);
uint16_t makeColor(const char* buf);

#endif // DISPLAY_IMAGE_H
