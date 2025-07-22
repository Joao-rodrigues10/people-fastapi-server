
---
```markdown
# 📘 FastAPI - Explicando

Este projeto é uma API simples desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) para fins educacionais. A API permite criar e consultar pessoas, persistindo os dados localmente em um arquivo JSON.

## 🚀 Funcionalidades

- 📄 Adicionar uma nova pessoa
- 🔍 Buscar uma pessoa por ID

## PRECISA IMPLEMENTAR
- 🗑️ Deletar uma pessoa
- ✏️ Atualizar os dados de uma pessoa
- 📜 Listar todas as pessoas

````

## 📦 Requisitos

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic

Você pode instalar as dependências com:

```bash
pip install -r requirements.txt
````

## ▶️ Como Executar

Execute o servidor com:

```bash
python main.py
```

A API estará acessível em: [http://localhost:80](http://localhost:80)

## 📬 Endpoints

### `GET /people/{user_id}`

Busca uma pessoa pelo ID.

**Exemplo de resposta:**

```json
{
  "id": "c1a37b59-f1f3-4f25-84b9-b08a6ce0bb63",
  "name": "João",
  "last_name": "Silva",
  "age": 30,
  "birthdate": "1993-05-14"
}
```

### `POST /people`

Adiciona uma nova pessoa.

**Exemplo de requisição:**

```json
{
  "name": "Maria",
  "last_name": "Oliveira",
  "age": 28,
  "birthdate": "1995-03-22"
}
```

**Exemplo de resposta:**

```json
{
  "id": "f44d9f1e-1f6e-47c9-9020-109bc4e5cf4d",
  "name": "Maria",
  "last_name": "Oliveira",
  "age": 28,
  "birthdate": "1995-03-22"
}
```

## 🧠 Sobre o Projeto

Esse projeto simula um CRUD básico com armazenamento em arquivo local (`database.json`). Ideal para ensinar conceitos como:

* Organização em camadas (router, schema, main)
* Pydantic para validação de dados
* Uso de UUID para criação de identificadores únicos
* Criação de rotas com FastAPI