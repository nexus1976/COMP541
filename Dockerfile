FROM python:3.11.2-slim
EXPOSE 80
EXPOSE 8000
COPY . .
RUN apt-get update && apt-get install -y gcc python3-dev
RUN pip install -r /deployedmodel/requirements.txt
CMD ["python", "-m", "uvicorn", "deployedmodel.main:app", "--host", "0.0.0.0", "--port", "8000", "--forwarded-allow-ips", "*"]
