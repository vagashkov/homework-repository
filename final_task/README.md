<h1 align="center">WallGrabber</h1>

## Description

WallGrabber is a simple VK-only (for now) wall information parser implemented using Python.

## How to use
Fill the form on index page:
- Your access token (you can read [here](https://vk.com/dev/implicit_flow_user) how to obtain it or follow the steps below)
    - navigate to [Application Management](https://vk.com/apps?act=manage) page and create your own VK application;
    - open its settings in order to obtain its ID and insure by the way that it is up and running;
    - follow link like oauth.vk.com/authorize?client_id=8055328&display=page&redirect_uri=http://vk.com/callback&scope=photos,video,offline,albums,polls&response_type=token&v=5.131&state=123456 
       (just substitute your application ID from previous step into client_id parameter);
    - you will be prompted for access confirmation and after that you will be redirected to another page
       (like https://api.vk.com/blank.html...)
    - copy its access_token parameter and use it in WallGrabber (but remember: never EVER share it with someone else).
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
2. Navigate to final_task folder.
3. Enter the command below

```
docker-compose up

```

## Future scope

- Add more versatile errors processing;
- Create Utils class for common functions (getJSON etc);
- Add required fields control in Source abstract class __init__ method.