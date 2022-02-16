# Telegram Image Upscaler Bot

## Overview
A simple telegram bot for Upscaling images.

## Demo
TODO: youtube link

## Introduction
This bot was created with the purpose of upscaling images via telegram, in order to have higher resolution images for design or editing.
The bot will ask what kind of upscale to perform (_x2_, _x3_, _x4_) and will wait for an image.
Once it receives an image, it will apply an opencv model (ESDR) for upscaling.

## How to setup
#### Docker
- Clone this repository
- **Run** `docker build --tag bot .`
- **Run** `docker run bot`
#### Local instance
##### Requirements:
-
