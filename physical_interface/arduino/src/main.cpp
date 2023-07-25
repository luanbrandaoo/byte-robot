#include "main.h"

void setup() {
  Serial.begin(57600);
  tft.initR(INITR_BLACKTAB);
  tft.setRotation(3);
  tft.fillScreen(ST7735_BLACK);
}

void loop() {
  if (!isSendingImage) {
    if (Serial.available() >= 10) {
      char buf[11];
      Serial.readBytes(buf, 10);
      buf[10] = '\0';
      if (strcmp(buf, "send_image") == 0) {
        isSendingImage = true;
        Serial.println("ok");
      } else if (strcmp(buf, "emotionneu") == 0) {
        Serial.println("emotion");
        neutralEyes(tft);
      } else if (strcmp(buf, "emotionhap") == 0) {
        Serial.println("emotion");
        happyEyes(tft);
      } else if (strcmp(buf, "emotionsad") == 0) {
        Serial.println("emotion");
        sadEyes(tft);
      } else if (strcmp(buf, "searchicon") == 0) {
        Serial.println("search");
        searchIcon();
      }
    }
  } else {
    displayPixels(tft);
  }
}