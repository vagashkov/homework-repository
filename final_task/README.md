<h1 align="center">WallGrabber</h1>

## Description

WallGrabber is a simple VK-only (for now) wall information parser implemented using Python.

## How to use
Fill the form on index page:
- Your access token (read [here](https://dev.vk.com/api/access-token/getting-started) how to obtain it) 
- Owner ID (required field)
- mark fields to export (or leave all selected by default) - also required field
- select export start date (or leave field empty and get the whole wall)
and press "Grab It" button.
After that you will be automatically redirected to results page if parsing was successful or to the error page otherwise.
On results page click "Statistics" button in order to show/hide statistics tables or "Download" button in order to download CSV file with report.

## About the project.
- WallGrabber is implemented using VK API calls to obtain wall, post or post attachment description.

## Project setup
0. You need Docker Composer to be installed.
1. Download repository content
2. Navigate to homework-repository folder.
3. Enter the command below

```
docker-compose up

```

## Future scope

- Add more versatile error implementation.
- Make weekdays statistics human-readable.
- Create Utils class for common functions (getJSON etc).
- Add obligatory fields control in Source abstract class __init__ method.
