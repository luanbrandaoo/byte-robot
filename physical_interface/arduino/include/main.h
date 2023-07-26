#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include "display_image.h"
#include "display_icons.h"

#define TFT_CS     10
#define TFT_RST    8
#define TFT_DC     9

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);
bool isSendingImage = false;