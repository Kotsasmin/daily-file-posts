# Daily File Posts

---

## Important Warning

🚨 **This project is meant for fun and challenges only!** 🚨

It's a simple and playful implementation to challenge myself by trying to collect all the possible images from the daily posts. This is **not a serious project**, and it's meant just for the fun of getting the challenge to collect the images. Don't expect this to be a robust solution or anything professionally useful. It's just a small, fun experiment! 🎉

---

### Usage Disclaimer:

⚠️ **DO NOT use this script to overload the server or cause any harm.** ⚠️

This script is intended for personal use and for fun only. It is your responsibility to ensure that it does not unintentionally affect the server or its bandwidth. I am **NOT responsible** for any downtime, overloading, or server issues that may result from the use of this script. This script should **not** be used to repeatedly hit or download the image in a way that could cause unnecessary load on the server. Use it responsibly!

---

## Description

This is a simple Python implementation that periodically checks for a new image posted at [https://www.mflan.com/dailyfilepost.jpg](https://www.mflan.com/dailyfilepost.jpg). The script downloads the image, calculates its MD5 checksum, and saves it to a directory (`dailyfileposts`) only if the image is new (not previously downloaded). The checksums of the images are stored in a local file (`checksums.txt`) to keep track of downloaded images.

The script runs in an infinite loop, checking for new images every hour (3600 seconds), downloading and saving them if they're different from previously saved images.

