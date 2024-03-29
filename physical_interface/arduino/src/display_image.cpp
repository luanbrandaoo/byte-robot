#include "display_image.h"
#include <Arduino.h>

const int BUFFER_SIZE = 1000;
char buf[BUFFER_SIZE];
int num_pixels = 0;
int current_pixel = 0;

void displayPixels(Adafruit_ST7735 &tft) {
  if (isSendingImage && Serial.available() >= 12) {
    memset(buf, 0, BUFFER_SIZE);
    num_pixels = 0;
    current_pixel = 0;

    while (Serial.available() && current_pixel < BUFFER_SIZE - 1) {
      buf[current_pixel] = Serial.read();
      if (buf[current_pixel] == '\n') {
        break;
      }
      current_pixel++;
      num_pixels++;
    }
    buf[current_pixel] = '\0';

    for (int i = 0; i < num_pixels; i += 12) {
      if (strncmp(&buf[i], "XXXXXXXXXXXX", 12) == 0) {
        isSendingImage = false;
        Serial.println("end");
        return;
      }

      int X, Y;
      uint16_t color;

      sscanf(&buf[i], "%d,%d,%4hx", &X, &Y, &color);
      uint16_t pixel = makeColor(&buf[i + 8]);

      tft.drawPixel(X, Y, pixel);
    }
  }
}

uint16_t makeColor(const char* buf) {
  uint16_t color;
  sscanf(buf, "%4x", &color);
  return color;
}
