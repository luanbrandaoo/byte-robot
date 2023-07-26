#include "display_icons.h"

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

void searchIcon() {
  int width = 52;
  int height = 52;

  int startX = 46;
  int startY = 30;

  uint16_t stroke_color = ST7735_WHITE;

  int circle_radius = width / 2;

  tft.fillScreen(ST7735_BLACK);

  tft.drawCircle(startX + width / 2, startY + height / 2, circle_radius, stroke_color);
  tft.drawCircle(startX + width / 2, startY + height / 2, circle_radius + 1, stroke_color);
  tft.drawCircle(startX + width / 2, startY + height / 2, circle_radius + 2, stroke_color);
  tft.drawCircle(startX + width / 2, startY + height / 2, circle_radius + 3, stroke_color);

  tft.drawLine(93, 78, 114, 103, stroke_color);
  tft.drawLine(93, 77, 114, 102, stroke_color);
  tft.drawLine(93, 76, 114, 101, stroke_color);
  tft.drawLine(93, 75, 114, 100, stroke_color);
  tft.drawLine(93, 74, 114, 99, stroke_color);
}

void loadingIcon() {
  tft.fillScreen(ST7735_BLACK);

  tft.fillCircle(77, 61, 13, ST7735_WHITE);
  tft.fillCircle(42, 61, 13, ST7735_WHITE);
  tft.fillCircle(112, 61, 13, ST7735_WHITE);
}

void blackScreen() {
  tft.fillScreen(ST7735_BLACK);
}

