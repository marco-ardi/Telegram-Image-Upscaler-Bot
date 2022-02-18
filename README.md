# Telegram Image Upscaler Bot

## Overview
A simple telegram bot for Upscaling images.

## Demo
[![Telegram Image Upscaler Bot](https://user-images.githubusercontent.com/50525101/154658678-34b59686-6c6b-4875-9b17-b157ac9bd01a.png)](https://youtu.be/-YN-cHnVdJE)


## Introduction
This bot was created with the purpose of upscaling images via Telegram, in order to have higher resolution images for design or editing.
The bot will ask users which kind of upscale to perform (_x2_, _x3_, _x4_) and it will wait for an input image.
Once it receives an image, an openCV model ([EDSR](https://arxiv.org/abs/1707.02921)) for upscaling will be applied and the result image will be sent back.

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
Here you can see the comparison between EDSR upscaling and [Nearest Neighour](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm) or [Cubic interpolation](https://en.wikipedia.org/wiki/Bicubic_interpolation) upscaling:



![confronto - input output](https://user-images.githubusercontent.com/50525101/154659754-cdaaca1d-c222-45ba-aa53-287025a6ea30.png)


![confronto - nn output](https://user-images.githubusercontent.com/50525101/154659811-f2b2e032-e69a-4a40-ba77-e10e353f079c.png)

