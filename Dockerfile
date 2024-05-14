FROM python:3.11
WORKDIR /cartpole-evaluation
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8002
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8002", "--reload"]