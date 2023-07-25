#ifndef DISPLAY_IMAGE_H
#define DISPLAY_IMAGE_H

#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>

extern const int BUFFER_SIZE;
extern char buf[];
extern int num_pixels;
extern int current_pixel;
extern bool isSendingImage;

void displayUpdateIndividually(Adafruit_ST7735 &tft);
uint16_t makeColor(const char* buf);

#endif // DISPLAY_IMAGE_H
