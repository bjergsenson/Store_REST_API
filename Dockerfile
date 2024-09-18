FROM python:3.10
EXPOSE 5000
WORKDIR /Store_REST_API
RUN pip install flask
COPY . . 
CMD ["flask", "run", "--host", "0.0.0.0"]