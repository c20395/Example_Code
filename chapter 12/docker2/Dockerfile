# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /docker

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# exposing default port for streamlit
EXPOSE 8501
# command to run on container start
CMD [ "streamlit", "run", "main2.py" ]
