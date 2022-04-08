FROM python:3.8

WORKDIR .

COPY main.py .

RUN pip install requests beautifulsoup4

CMD ["python","main.py"]