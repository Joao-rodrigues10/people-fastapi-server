
### 📄 README.md

````markdown
# MongoDB Local com Docker Compose

Este projeto fornece um ambiente MongoDB local usando Docker Compose, ideal para desenvolvimento em Windows.

---

## 🐳 Pré-requisitos

Antes de começar, você precisa ter:

- [Docker Desktop para Windows](https://www.docker.com/products/docker-desktop/) instalado e rodando.
- Git Bash ou terminal com suporte a comandos Unix (recomendado para Windows).

---

## 🚀 Rodando o MongoDB localmente

1. **Clone ou baixe este repositório**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
````

2. **Inicie o container**

```bash
docker-compose up -d
```

Isso irá:

* Baixar a imagem do MongoDB (caso ainda não tenha)
* Criar um container com:

  * Porta local `27017`
  * Usuário: `root`
  * Senha: `example`

3. **Verifique se está rodando**

```bash
docker ps
```

Você deverá ver algo como:

```
CONTAINER ID   IMAGE       COMMAND                  PORTS                    NAMES
abc123456789   mongo:6.0   "docker-entrypoint.s…"   0.0.0.0:27017->27017/tcp mongodb
```

---

## 🔗 Conexão

Conecte-se ao MongoDB usando a string:

```
mongodb://root:example@localhost:27017
```

* Banco: `people_db` (exemplo usado no código)
* Ferramenta recomendada: [MongoDB Compass](https://www.mongodb.com/products/compass)

---

## 🛑 Parar e remover os containers

```bash
docker-compose down
```

Para também apagar os dados salvos (volume):

```bash
docker-compose down -v
```

---

## 📁 Estrutura esperada do arquivo `docker-compose.yml`

```yaml
version: '3.8'

services:
  mongodb:
    image: mongo:6.0
    container_name: mongodb
    restart: unless-stopped
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example

volumes:
  mongodb_data:
```