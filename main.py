import sys
import os
import subprocess
import platform

# Function to check if Docker is installed on the system
def check_docker_installed():
    # Detect the system platform (Windows, Linux, macOS)
    system_platform = platform.system().lower()

    if system_platform == "windows":
        try:
            # Check for Docker on Windows using 'where' command
            subprocess.run(["where", "docker"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("Docker is already installed.")
        except subprocess.CalledProcessError:
            # If Docker is not found, download the installer for Windows
            print("Docker is not installed. Downloading and installing Docker for Windows...")
            url = "https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe"
            subprocess.run(["curl", "-fsSL", "-o", "docker_installer.exe", url])
            print("Please run the downloaded installer (docker_installer.exe) to install Docker.")
            return
    else:
        try:
            # Check for Docker on Linux and macOS using 'which' command
            subprocess.run(["which", "docker"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("Docker is already installed.")
        except subprocess.CalledProcessError:
            # If Docker is not found, download and install Docker for Linux or macOS
            print("Docker is not installed. Downloading and installing Docker...")
            subprocess.run(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"])
            subprocess.run(["sudo", "sh", "get-docker.sh"])
            os.remove("get-docker.sh")
            print("Docker is now installed.")

# Function to check if Docker Compose is installed on the system
def check_docker_compose_installed():
    # Detect the system platform (Windows, Linux, macOS)
    system_platform = platform.system().lower()

    if system_platform == "windows":
        try:
            # Check for Docker Compose on Windows using 'where' command
            subprocess.run(["where", "docker-compose"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("Docker Compose is already installed.")
        except subprocess.CalledProcessError:
            # If Docker Compose is not found, download the executable for Windows
            print("Docker Compose is not installed. Downloading and installing Docker Compose for Windows...")
            url = "https://github.com/docker/compose/releases/latest/download/docker-compose-Windows-x86_64.exe"
            subprocess.run(["curl", "-fsSL", "-o", "docker-compose.exe", url])
            print("Docker Compose is now installed.")
            print("Please make sure to add the directory containing 'docker-compose.exe' to your system's PATH.")
            return
    else:
        try:
            # Check for Docker Compose on Linux and macOS using 'which' command
            subprocess.run(["which", "docker-compose"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("Docker Compose is already installed.")
        except subprocess.CalledProcessError:
            # If Docker Compose is not found, download and install Docker Compose for Linux or macOS
            print("Docker Compose is not installed. Downloading and installing Docker Compose...")
            url = f"https://github.com/docker/compose/releases/latest/download/docker-compose-{system_platform}-{platform.machine()}"
            subprocess.run(["curl", "-fsSL", "-o", "docker-compose", url])
            os.chmod("docker-compose", 0o755)
            os.environ["PATH"] += os.pathsep + os.getcwd()
            print("Docker Compose is now installed.")

# Function to create a WordPress site using Docker Compose
def create_wordpress_site(site_name):
    if site_name is None:
        print("Error: Site name is missing.")
        return
    print(f"Creating WordPress site '{site_name}': ")
    docker_compose_content = f"""
version: '3'
services:
  wordpress:
    image: wordpress:latest
    restart: always
    ports:
      - 80:80
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - ./wp-content:/var/www/html/wp-content
  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
      MYSQL_ROOT_PASSWORD: root_password
    volumes:
      - db_data:/var/lib/mysql
volumes:
  db_data:
    """
    
    # Write the Docker Compose configuration to a file
    with open("docker-compose.yml", "w") as docker_compose_file:
        docker_compose_file.write(docker_compose_content)
    
    # Start the WordPress site using Docker Compose
    subprocess.run(["docker-compose", "up", "-d"], check=True)

# Function to add an entry in the hosts file for the WordPress site
def add_entry(site_name):
    system_platform = platform.system().lower()

    if system_platform == "windows":
        # On Windows, the 'hosts' file is located at C:\Windows\System32\drivers\etc\hosts
        hosts_file_path = os.path.join(os.environ["SystemRoot"], "System32", "drivers", "etc", "hosts")
    else:
        # On Linux and macOS, the 'hosts' file is at /etc/hosts
        hosts_file_path = "/etc/hosts"

    # Append the site entry to the hosts file
    with open(hosts_file_path, "a") as hosts_file:
        hosts_file.write(f"127.0.0.1 {site_name}\n")

    print(f"Added entry for {site_name} in the hosts file.")

# Function to open the WordPress site in the default web browser
def open_in_browser(site_name):
    system_platform = platform.system().lower()

    if system_platform == "windows":
        # On Windows, use the 'start' command to open the URL in the default web browser
        subprocess.run(["start", f"http://{site_name}"], shell=True)
    elif system_platform == "linux" or system_platform == "darwin":
        # On Linux or macOS, use 'xdg-open' to open the URL in the default web browser
        subprocess.run(["xdg-open", f"http://{site_name}"])
    else:
        print(f"Sorry, automatic browser opening is not supported on {system_platform}. Please manually open http://{site_name} in your web browser.")

# Function to enable or disable the WordPress site by starting or stopping the containers
def enable_disable_site(action):
    if not os.path.exists("docker-compose.yml"):
        print("Error: docker-compose.yml not found. Please run 'python script_name.py setup [site_name]' first.")
        return

    if action == "enable":
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        print("Site enabled.")
    elif action == "disable":
        subprocess.run(["docker-compose", "down"], check=True)
        print("Site disabled.")
    else:
        print("Invalid action. Use 'enable' or 'disable'.")

# Function to delete the WordPress site by stopping and removing the containers and the configuration file
def delete_site():
    if not os.path.exists("docker-compose.yml"):
        print("Error: docker-compose.yml not found. Please run 'python script_name.py setup [site_name]' first.")
        return

    subprocess.run(["docker-compose", "down", "--volumes"], check=True)
    os.remove("docker-compose.yml")
    print("Site deleted.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py [command] [site_name]")
        sys.exit(1)

    command = sys.argv[1]
    site_name = sys.argv[2] if len(sys.argv) >= 3 else None

    if command == "setup":
        # Setup the WordPress site
        check_docker_installed()
        check_docker_compose_installed()
        create_wordpress_site(site_name)
        add_entry(site_name)
        open_in_browser(site_name)
    elif command == "enable":
        # Enable the WordPress site
        enable_disable_site("enable")
    elif command == "disable":
        # Disable the WordPress site
        enable_disable_site("disable")
    elif command == "delete":
        # Delete the WordPress site
        delete_site()
    else:
        print("Invalid command.")
