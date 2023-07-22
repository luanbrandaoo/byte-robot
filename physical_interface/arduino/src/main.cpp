#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include "display_image.h"

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

void setup() {
  Serial.begin(57600);
  tft.initR(INITR_BLACKTAB);
  tft.setRotation(0);
  tft.fillScreen(ST7735_BLACK);
}

void loop() {
  displayUpdate(tft);
}
