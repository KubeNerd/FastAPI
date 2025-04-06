FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH" \
    PYTHONPATH="/application"

WORKDIR /application

# Instala dependências do sistema
RUN apt-get update && apt-get install -y build-essential \
  && apt-get autoremove -y && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copia o requirements.txt
COPY ./requirements.txt .

# Instala as dependências com pip
RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY ./application .

EXPOSE 8080

CMD ["python", "main.py"]
