FROM ubuntu:18.04


RUN apt-get update && apt-get install -y build-essential \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    vim \
    xvfb \
    firefox


RUN apt-get clean


# Make working directory
RUN mkdir /var/tmp/bu_cicd_example_selenium_test


# Declare the working directory inside container
WORKDIR /var/tmp/bu_cicd_example_selenium_test


# Copy the project files into the container
COPY . /var/tmp/bu_cicd_example_selenium_test


# Get the geckodriver binary for Firefox and decompress the tar
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz
RUN tar -xvzf /var/tmp/bu_cicd_example_selenium_test/geckodriver-v0.28.0-linux64.tar.gz


# Move the geckodriver binary into the $PATH and delete the tar file.
RUN mv /var/tmp/bu_cicd_example_selenium_test/geckodriver /usr/local/bin/
RUN rm -rf /var/tmp/bu_cicd_example_selenium_test/geckodriver-v0.28.0-linux64.tar.gz


# Install Python requirements
RUN pip3 install -r /var/tmp/bu_cicd_example_selenium_test/requirements.txt


# Make the selenium_test.py file executable
RUN chmod +x /var/tmp/bu_cicd_example_selenium_test/selenium_test.py


# Run the Selenium app with the headless option and output to file. Text appended
# to the file during execution indicates errors; an empty file is a success.
CMD  /var/tmp/bu_cicd_example_selenium_test/selenium_test.py -x > error.txt


# -----------------------------------------------------------------------------

# Build the Dockerfile from within the project's directory:
# docker build -t ubuntu_selenium_test:latest .


# Run container for life of processes
# (will terminate quickly if not running a process or sleeping):
# docker run --detach -it ubuntu_selenium_test


# Enter a running container
# docker exec -it <container id> /bin/bash


#  View or remove current images:
# docker image ls | rm


# View running containers:
# docker container ls


# Stop/Remove a running container:
# docker container stop <container ID>
# docker container rm <container ID>


# Clean up a unused and dangling images or stopped containers
# docker system prune
# docker container prune
