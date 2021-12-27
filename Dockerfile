FROM python:3.9

WORKDIR /api

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80","--reload"]
