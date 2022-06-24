#Deriving the latest base image
FROM browserless/chrome

LABEL Maintainer="Elgilany Hassan"

WORKDIR /home

#COPY gellany_tools.py ./
#COPY requirements.txt ./

RUN apt-get update
RUN apt-get install git
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip install --upgrade pip 

RUN git clone https://github.com/gellanyhassan0/gellany_table.git ./

RUN pip install -r ./requirements.txt
RUN wget https://raw.githubusercontent.com/gellanyhassan0/gellany_selenium_chromedriver/main/gellany_selenium_chromedriver.sh 
RUN chmod +x ./gellany_selenium_chromedriver.sh
RUN ./gellany_selenium_chromedriver.sh
#CMD [ "python3", "./manage.py", runserver", "0.0.0.0:8000"]

CMD python3 -c "import signal; signal.pause()"
