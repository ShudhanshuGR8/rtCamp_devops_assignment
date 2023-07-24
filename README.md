# Dockerized WordPress Setup Script

![Docker](https://img.shields.io/badge/Docker-v20.10.7-blue?logo=docker)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v1.29.2-blue?logo=docker)
![Python](https://img.shields.io/badge/Python-v3.10-green?logo=python)

Welcome to my Dockerized WordPress Setup Script! With this script, you can easily set up a WordPress site using Docker and Docker Compose on various platforms, including Windows, Linux, and macOS.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Commands](#commands)
- [Results](#results)

## Overview
This Python script automates the installation of Docker and Docker Compose (if not already installed) and creates a Docker Compose configuration for running a WordPress site. Additionally, it adds an entry in your hosts file for easy access to the WordPress site in your browser.

## Prerequisites
Before running the script, please ensure you have the following installed on your system:

- Docker (v20.10.7 or higher)
- Docker Compose (v1.29.2 or higher)
- Python (v3.10 or higher)

## Getting Started
1. Clone this repository to your local machine or download the script file directly.

2. Open a terminal or command prompt and make sure to run it as administrator and navigate to the folder containing the script.
   - Run as Administrator is done because we need to add entry in the host files for our wordpress site. And for windows, you might get permission denied error while running the add_hosts_entry. Hence you need to run your terminal or command prompt as Administrator.

4. Run the following command to check if Docker and Docker Compose are installed:
```python
python script_name.py setup [site_name]
```
Replace `script_name.py` with the actual name of the script and `[site_name]` with your desired site name.

4. Follow the on-screen instructions to download and install Docker and Docker Compose if needed.

5. Once Docker and Docker Compose are installed, the script will automatically create a Docker Compose configuration for the WordPress site and start the containers.

6. After the setup is complete, you can access your WordPress site at `http://[site_name]` in your web browser.
   - The first time you will be prompted to choose your desired language and then enter details about your site-title, username and password. Do the neeedful and then click on Install wordpress.

8. Now you can access your WordPress site at `http://[site_name]` in your web browser.

## Commands
The script supports the following commands:

- `python script_name.py setup [site_name]`: Set up a new WordPress site with Docker.
- `python script_name.py enable`: Start the containers and enable the WordPress site.
- `python script_name.py disable`: Stop the containers and disable the WordPress site.
- `python script_name.py delete`: Delete the WordPress site and remove the Docker Compose configuration.

## Results
1. The first time you are redirected to the wordpress site page, you should be redirected to the below page:
- ![image](https://github.com/ShudhanshuGR8/rtCamp_devops_assignment/assets/75602183/dbaa00b6-4e1a-4b7c-955e-36fcdaf6d61d)
2. Then you will be redirected to the below page for filling your details and installing wordpress.
- ![image](https://github.com/ShudhanshuGR8/rtCamp_devops_assignment/assets/75602183/672cb5ab-584e-40be-88d0-e7a0de165f22)
3. Then it will prompt you to login to your wordpress account.
- ![image](https://github.com/ShudhanshuGR8/rtCamp_devops_assignment/assets/75602183/bbba13a4-0037-4b3e-8778-8d34f5df2ad2)
4. Then it will redirect you to the dashboard page.
- ![image](https://github.com/ShudhanshuGR8/rtCamp_devops_assignment/assets/75602183/960b6172-b143-4b57-bf40-9d2ccb56a8bb)
5. Now you just need to enter your the following url `http://[site_name]` and you will be able to view your wordpress file.
- ![image](https://github.com/ShudhanshuGR8/rtCamp_devops_assignment/assets/75602183/50564051-81f1-4831-b468-4052767b8338)



Feel free to contribute, report issues, or suggest improvements!

Happy coding! 🚀

