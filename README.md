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

## Overview
This Python script automates the installation of Docker and Docker Compose (if not already installed) and creates a Docker Compose configuration for running a WordPress site. Additionally, it adds an entry in your hosts file for easy access to the WordPress site in your browser.

## Prerequisites
Before running the script, please ensure you have the following installed on your system:

- Docker (v20.10.7 or higher)
- Docker Compose (v1.29.2 or higher)
- Python (v3.10 or higher)

## Getting Started
1. Clone this repository to your local machine or download the script file directly.

2. Open a terminal or command prompt and navigate to the folder containing the script.

3. Run the following command to check if Docker and Docker Compose are installed:
```python
python script_name.py setup [site_name]
```
Replace `script_name.py` with the actual name of the script and `[site_name]` with your desired site name.

4. Follow the on-screen instructions to download and install Docker and Docker Compose if needed.

5. Once Docker and Docker Compose are installed, the script will automatically create a Docker Compose configuration for the WordPress site and start the containers.

6. After the setup is complete, you can access your WordPress site at `http://[site_name]` in your web browser.

## Commands
The script supports the following commands:

- `python script_name.py setup [site_name]`: Set up a new WordPress site with Docker.
- `python script_name.py enable`: Start the containers and enable the WordPress site.
- `python script_name.py disable`: Stop the containers and disable the WordPress site.
- `python script_name.py delete`: Delete the WordPress site and remove the Docker Compose configuration.


Feel free to contribute, report issues, or suggest improvements!

Happy coding! 🚀

