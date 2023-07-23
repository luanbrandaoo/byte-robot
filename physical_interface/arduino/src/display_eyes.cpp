#include "display_eyes.h"

void neutralEyes(Adafruit_ST7735 &tft) {
  tft.fillScreen(ST7735_BLACK);
  //tft.fillRoundRect(startX, startY, width, height, radius, fillColor);
  tft.fillRoundRect(4, 31, 67, 67, 25, 0xFFFF);
  tft.fillRoundRect(88, 31, 67, 67, 25, 0xFFFF);
}

void happyEyes(Adafruit_ST7735 &tft) {
  tft.fillScreen(ST7735_BLACK);
  tft.fillRoundRect(4, 31, 67, 67, 25, 0xFFFF);
  tft.fillRoundRect(88, 31, 67, 67, 25, 0xFFFF);
  tft.fillRect(4, 64, 151, 34, 0x0000);
}

void sadEyes(Adafruit_ST7735 &tft) {
  tft.fillScreen(ST7735_BLACK);
  tft.fillRoundRect(4, 31, 67, 67, 25, 0xFFFF);
  tft.fillRoundRect(88, 31, 67, 67, 25, 0xFFFF);
  tft.fillTriangle(4, 61, 4, 31, 72, 31, 0x0000);
  tft.fillTriangle(155, 61, 88, 31, 155, 31, 0x0000);
}