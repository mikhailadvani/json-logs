FROM python:alpine

ADD run.py .

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "-u", "run.py"]
