#include "display_image.h"
#include <Arduino.h>

const int BUFFER_SIZE = 1000;
char buf[BUFFER_SIZE];
int num_pixels = 0;
int current_pixel = 0;

int startX;
int startY;

void displayUpdate(Adafruit_ST7735 &tft) {
  if (isSendingImage && Serial.available() >= 4) {
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

    static int x = 0;
    static int y = 0;

    for (int i = 0; i < num_pixels; i += 4) {
      if (strncmp(&buf[i], "XXXX", 4) == 0) {
        isSendingImage = false;
        startX = 0;
        startY = 0;
        Serial.println("end");
        return;
      }

      uint16_t pixel = makeColor(&buf[i]);

      tft.drawPixel(x, y, pixel);

      x++;
      if (x >= tft.width()) {
        x = 0;
        y++;

        if (y >= tft.height()) {
          y = 0;
        }
      }
    }
  }
}

uint16_t makeColor(const char* buf) {
  uint16_t color;
  sscanf(buf, "%4x", &color);
  return color;
}
