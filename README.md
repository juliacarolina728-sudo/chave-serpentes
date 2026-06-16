# 🐍 Chave Serpentes

O **Chave Serpentes** é uma aplicação web desenvolvida em Flask integrada a um banco de dados PostgreSQL. O objetivo principal do sistema é gerenciar dados e consultas taxonômicas ou de identificação de serpentes de forma rápida e segura.

Este projeto foi totalmente dockerizado, permitindo que toda a infraestrutura (aplicação web e banco de dados) seja inicializada de forma automatizada com um único comando.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.10 / Flask
* **Servidor de Produção:** Gunicorn
* **Banco de Dados:** PostgreSQL 15
* **Orquestração de Contêineres:** Docker & Docker Compose

---

## 🚀 Como Rodar o Projeto (Guia do Usuário)

Como o projeto está configurado com Docker, você não precisa instalar o Python ou o PostgreSQL manualmente na sua máquina. Basta ter o Docker instalado.

### 📋 Pré-requisitos
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e rodando.

### 🔧 Passo a Passo para Execução

1. **Clone o repositório:**
```bash
   git clone [https://github.com/juliacarolina728-sudo/chave-serpentes.git]
   cd chave-serpentes
```
2. Suba os contêineres com o Docker Compose:
No terminal da raiz do projeto, execute o comando abaixo para construir as imagens e iniciar os serviços:

```
docker compose up --build
```


