# 🐍 Chave Serpentes

O **Chave Serpentes** é uma aplicação web desenvolvida em Flask, integrada a um banco de dados PostgreSQL, focada na gestão de dados taxonômicos e identificação de serpentes de forma rápida, segura e educativa. O projeto visa auxiliar na identificação de espécies nativas do estado de São Paulo, promovendo a conscientização sobre a fauna local e a prevenção de acidentes.

---

## 🛠️ Tecnologias Utilizadas
- **Backend:** Python 3.10 / Flask
- **Banco de Dados:** PostgreSQL 15
- **Servidor:** Gunicorn (Produção)
- **Infraestrutura:** Docker & Docker Compose
- **Deploy:** Railway

---

## 🧠 Lógica de Identificação
A aplicação utiliza um algoritmo baseado em **chaves dicotômicas**. O sistema conduz o usuário através de perguntas lógicas sobre características morfológicas, habitat e comportamento da serpente, filtrando as informações no banco de dados até chegar à espécie correta.

---

## 📂 Estrutura do Projeto
A organização do código foi planejada para garantir escalabilidade e fácil manutenção:

- `/app`: Código principal da aplicação Flask.
- `/static` & `/templates`: Assets e arquivos de front-end.
- `Dockerfile`: Configuração do ambiente de execução.
- `docker-compose.yml`: Orquestração entre a aplicação e o banco de dados.



[Image of basic database schema architecture]


---

## 📊 Modelo de Dados
Os dados estão estruturados no PostgreSQL com as seguintes entidades principais:
- **Species**: Armazena o nome científico, características morfológicas, habitat e links de imagens.
- **DichotomousKey**: Armazena as ramificações lógicas das perguntas de identificação.

---

## 🚀 Como Rodar o Projeto

Como o projeto está totalmente containerizado, você não precisa instalar o Python ou o PostgreSQL manualmente.

### Pré-requisitos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado.

### Passo a Passo
1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/juliacarolina728-sudo/chave-serpentes.git
   
   cd chave-serpentes
Subir os serviços:
No terminal da raiz do projeto, execute:
```
docker compose up --build
```
O projeto está disponível online via Railway:  
 https://chave-serpentes-production.up.railway.app
 
 ### Demonstração
 <img width="692" height="388" alt="teste site" src="https://github.com/user-attachments/assets/16e6a89d-da91-4ed9-a6e5-ec268c06f0cd" />

 
 👤 Autor
 
Desenvolvido por Julia Carolina.

