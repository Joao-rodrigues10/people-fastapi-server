---

```markdown
# 📘 FastAPI + MongoDB (Arquitetura Hexagonal)

Este projeto é uma API simples desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) utilizando **MongoDB como banco de dados** e arquitetura **hexagonal (ports & adapters)**.  
A API permite criar, buscar e futuramente atualizar/deletar pessoas. Ideal para fins educacionais e testes locais.

---

## 🧱 Arquitetura

O projeto segue a **arquitetura hexagonal (ou Clean Architecture)**:

```

\[Router] ─▶ \[UseCase] ─▶ \[Domain Service] ─▶ \[Repository]

````

- `app/router`: entrada HTTP com FastAPI  
- `app/usecase`: lógica de orquestração  
- `domain/service`: regras de negócio  
- `infra/repository`: acesso ao MongoDB (camada adaptadora)  

---

## 🚀 Funcionalidades

- ✅ Criar uma nova pessoa (`create`) – **implementado**
- ✅ Buscar uma pessoa por ID (`get`) – **implementado**
- ⏳ Atualizar uma pessoa (`update`) – **a implementar**
- ⏳ Deletar uma pessoa (`delete`) – **a implementar**
- ⏳ Listar todas as pessoas (`list`) – **a implementar**

---

## 📦 Requisitos

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- [pymongo](https://pymongo.readthedocs.io/en/stable/) (driver MongoDB)
- MongoDB local via Docker

Instale as dependências com:

```bash
pip install -r requirements.txt
````

---

## 🐳 Banco de Dados

Rodamos o MongoDB localmente usando **Docker Compose**.
Exemplo de `docker-compose.yml` incluído no projeto:

```yaml
version: '3.8'

services:
  mongodb:
    image: mongo:6.0
    container_name: mongodb
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
    volumes:
      - mongodb_data:/data/db

volumes:
  mongodb_data:
```

Start com:

```bash
docker-compose up -d
```

Conexão esperada:

```
mongodb://root:example@localhost:27017
```

Banco padrão: `people_db`
Coleção: `people`

---

## ▶️ Como Executar

Rode o app com:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📬 Endpoints

### `POST /people`

Adiciona uma nova pessoa.

**Requisição:**

```json
{
  "name": "Maria",
  "last_name": "Oliveira",
  "age": 28,
  "birthdate": "1995-03-22"
}
```

**Resposta:**

```json
{
  "id": "f44d9f1e-1f6e-47c9-9020-109bc4e5cf4d",
  "name": "Maria",
  "last_name": "Oliveira",
  "age": 28,
  "birthdate": "1995-03-22"
}
```

---

### `GET /people/{user_id}`

Busca uma pessoa pelo ID.

**Resposta:**

```json
{
  "id": "c1a37b59-f1f3-4f25-84b9-b08a6ce0bb63",
  "name": "João",
  "last_name": "Silva",
  "age": 30,
  "birthdate": "1993-05-14"
}
```

---

## ✅ Progresso de Implementação

| Método     | Status         | Integração Mongo | Local |
| ---------- | -------------- | ---------------- | ----- |
| `create`   | ✅ Implementado | ✅                | ❌     |
| `get`      | ✅ Implementado | ✅                | ❌     |
| `update`   | ⏳ Em breve     | ❌                | ❌     |
| `delete`   | ⏳ Em breve     | ❌                | ❌     |
| `list_all` | ⏳ Em breve     | ❌                | ❌     |

---

## 💡 Aprendizados

Esse projeto ensina:

* 📐 Arquitetura hexagonal real com separação de camadas
* 📂 Organização escalável (routers, usecases, domain, infra)
* 🧪 Injeção de dependência e testes por camadas
* 💾 Integração com MongoDB via PyMongo
* 🧰 Uso de UUID como identificador único
* 
---
