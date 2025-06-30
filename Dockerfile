ARG ACCOUNT_ID
FROM ${ACCOUNT_ID}.dkr.ecr.ap-northeast-2.amazonaws.com/baseimage:latest

COPY . /app
CMD ["python", "app.py"]
