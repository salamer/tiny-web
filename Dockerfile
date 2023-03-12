FROM kaithregistry.azurecr.io/serving-basic:v18
ENV PYTHONUNBUFFERED True
ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV APP_HOME /app
WORKDIR $APP_HOME
RUN python $APP_HOME/boot.py
COPY *.py ./
EXPOSE 8888 8887 8889 8080
RUN apt-get update && \
    apt-get -y install \
    git
RUN git clone https://github.com/salamer/tiny-web
RUN pip install pillow
RUN ["chmod", "+x", "/app/tiny-web/run.sh"]
ENTRYPOINT ["/bin/bash" ,"/app/tiny-web/run.sh"]