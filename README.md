# Telegram Image Upscaler Bot

## Overview
A simple telegram bot for Upscaling images.

## Demo
TODO: youtube link

## Introduction
This bot was created with the purpose of upscaling images via Telegram, in order to have higher resolution images for design or editing.
The bot will ask users which kind of upscale to perform (_x2_, _x3_, _x4_) and it will wait for an input image.
Once it receives an image, an openCV model (ESDR) for upscaling will be applied and the result image will be sent back.

## How to setup
### Docker
##### Steps
- Clone this repository
- Add your API token in row XXXXXX
- **Run** `docker build --tag bot .`
- **Run** `docker run bot`

### Local instance
##### Requirements:
- python >= 3.7 with the following modules:
  - python-telegram-bot.
  - opencv-contrib-python
-(optional) nvidia GPU and CUDA toolkit
##### Steps
- Clone this repository
- Add your API token in row XXXXXX
- **Run** `python bot.py`

## Results
