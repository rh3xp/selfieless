FROM alpine:3.7
RUN apk add --update --no-cache py3-pip
WORKDIR /acts
COPY . /acts
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
ENV TEAM_ID=CC_218_226_239_225
CMD ["python3", "acts.py"]
