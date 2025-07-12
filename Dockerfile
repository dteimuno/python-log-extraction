FROM python:3

WORKDIR /usr/src/app

COPY log-parsing.py .
COPY openssh.log .

# Run the script on container start
CMD ["python", "log-parsing.py"]
