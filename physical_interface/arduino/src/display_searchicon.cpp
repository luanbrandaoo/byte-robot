#include "display_searchicon.h"

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
