FROM python:3.11.0-slim

WORKDIR /app

RUN pip install "poetry==1.3.1"



COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-root

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



COPY flower_workshop .

EXPOSE 8000
ENTRYPOINT ["bash","entrypoint.sh"]
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]



