FROM python:3.10-slim

WORKDIR /bot

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY bot/ .

CMD ["python3", "bot.py"]