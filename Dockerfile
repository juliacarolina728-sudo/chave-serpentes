FROM python:3.10-slim

WORKDIR /app

# Instala as dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto dos arquivos do projeto
COPY . .

# Comando para rodar o servidor de produção
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]