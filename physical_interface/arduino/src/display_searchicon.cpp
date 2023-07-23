#include "display_searchicon.h"

void searchIcon() {
  int width = 52;
  int height = 52;

  int startX = 47;
  int startY = 32;

  uint16_t stroke_color = ST7735_WHITE;

  int circle_radius = width / 2;

  tft.fillScreen(ST7735_BLACK);

  tft.drawCircle(startX + width / 2, startY + height / 2, circle_radius, stroke_color);
  tft.drawCircle(startX + width / 2, startY + height / 2, circle_radius + 1, stroke_color);
  tft.drawCircle(startX + width / 2, startY + height / 2, circle_radius + 2, stroke_color);
  tft.drawCircle(startX + width / 2, startY + height / 2, circle_radius + 3, stroke_color);

  tft.drawLine(94, 80, 115, 105, stroke_color);
  tft.drawLine(94, 79, 115, 104, stroke_color);
  tft.drawLine(94, 78, 115, 103, stroke_color);
  tft.drawLine(94, 77, 115, 102, stroke_color);
  tft.drawLine(94, 76, 115, 101, stroke_color);
}
