FROM python

WORKDIR .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get --assume-yes install build-essential gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirments.txt ./

RUN pip install -r requirments.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]