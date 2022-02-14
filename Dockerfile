FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get -y install gcc libffi-dev libgl1-mesa-glx libglib2.0-0

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD python bot.py
CMD ["python", "-u", "bot.py"]