# Sistema de Gestão SOPUKA

Sistema de gestão **fullstack** desenvolvido para fins académicos, utilizando **Django REST Framework no backend** e **Vue.js no frontend**, com operações **CRUD completas**, dashboard interativo e notificações visuais.

O sistema permite gerir **Clientes, Serviços, Projetos e Equipas**, consumindo dados reais a partir de uma API REST.

---

## 📌 Tecnologias Utilizadas

### Backend

* Python 3
* Django
* Django REST Framework
* SQLite (base de dados)
* Django CORS Headers

### Frontend

* Vue.js 3 (Vite)
* Vue Router
* Axios
* Bootstrap 5
* Bootstrap Icons

---

## 🎯 Funcionalidades Principais

* CRUD completo (Criar, Listar, Atualizar e Eliminar)
* Dashboard com indicadores estatísticos
* Consumo real de API REST
* Notificações visuais (Toast) para ações do utilizador
* Interface responsiva e profissional
* Separação clara entre frontend e backend

---

## 🧩 Entidades do Sistema

* **Clientes**
* **Serviços**
* **Projetos**
* **Equipas**

---

## 🔗 Endpoints da API (Backend – SOPUKA)

A API segue o padrão **RESTful**, implementada com **Django REST Framework**.
Cada entidade possui um endpoint próprio com **CRUD completo**, suportando os métodos **GET, POST, PUT, PATCH e DELETE**.

### 📌 Clientes

| Método | Endpoint            | Descrição                    |
| ------ | ------------------- | ---------------------------- |
| GET    | /api/clientes/      | Listar todos os clientes     |
| GET    | /api/clientes/{id}/ | Obter cliente por ID         |
| POST   | /api/clientes/      | Criar novo cliente           |
| PUT    | /api/clientes/{id}/ | Atualizar cliente (completo) |
| PATCH  | /api/clientes/{id}/ | Atualizar cliente (parcial)  |
| DELETE | /api/clientes/{id}/ | Eliminar cliente             |

### 📌 Serviços

| Método | Endpoint            | Descrição                      |
| ------ | ------------------- | ------------------------------ |
| GET    | /api/servicos/      | Listar serviços                |
| GET    | /api/servicos/{id}/ | Obter serviço por ID           |
| POST   | /api/servicos/      | Criar serviço                  |
| PUT    | /api/servicos/{id}/ | Atualizar serviço              |
| PATCH  | /api/servicos/{id}/ | Atualizar serviço parcialmente |
| DELETE | /api/servicos/{id}/ | Eliminar serviço               |

### 📌 Projetos

| Método | Endpoint            | Descrição                      |
| ------ | ------------------- | ------------------------------ |
| GET    | /api/projetos/      | Listar projetos                |
| GET    | /api/projetos/{id}/ | Obter projeto por ID           |
| POST   | /api/projetos/      | Criar projeto                  |
| PUT    | /api/projetos/{id}/ | Atualizar projeto              |
| PATCH  | /api/projetos/{id}/ | Atualizar projeto parcialmente |
| DELETE | /api/projetos/{id}/ | Eliminar projeto               |

### 📌 Equipas

| Método | Endpoint           | Descrição                     |
| ------ | ------------------ | ----------------------------- |
| GET    | /api/equipas/      | Listar equipas                |
| GET    | /api/equipas/{id}/ | Obter equipa por ID           |
| POST   | /api/equipas/      | Criar equipa                  |
| PUT    | /api/equipas/{id}/ | Atualizar equipa              |
| PATCH  | /api/equipas/{id}/ | Atualizar equipa parcialmente |
| DELETE | /api/equipas/{id}/ | Eliminar equipa               |

---

## 🖥️ Dashboard

O dashboard apresenta informações resumidas do sistema, incluindo:

* Total de clientes
* Total de projetos
* Total de serviços
* Total de equipas

Os dados são carregados dinamicamente a partir da API REST.

---

## 🔔 Notificações

O sistema possui **notificações visuais (toast)** que informam ao utilizador quando:

* Um registo é criado
* Um registo é atualizado
* Um registo é eliminado
* Ocorre um erro

Isso melhora significativamente a experiência do utilizador.

---

## ⚙️ Como Executar o Projeto

### Backend (Django)

```bash
cd backend
python -m venv venv
venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Servidor disponível em:

```
http://127.0.0.1:8000/api/
```

---

### Frontend (Vue.js)

```bash
cd frontend
npm install
npm run dev
```

Aplicação disponível em:

```
http://localhost:5173
```

---

## 🧠 Conceitos Aplicados

* Arquitetura REST
* Separação de responsabilidades (Backend / Frontend)
* Componentização no Vue.js
* Reutilização de componentes (CRUD genérico)
* Boas práticas de UX/UI
* Consumo de API com Axios

---

## 🎓 Objetivo Académico

Este projeto foi desenvolvido como **trabalho académico**, com foco em:

* Aplicação prática de conceitos de desenvolvimento web
* Integração frontend + backend
* Preparação para projetos reais

---

## 📄 Licença

Este projeto é de uso académico e educativo.

---

## 👤 Autor

**Elias Sopupa**
Estudante de Tecnologia da Informação
Projeto – Django REST + Vue.js

---

> *“Sistema desenvolvido para demonstrar competências em desenvolvimento fullstack moderno.”*
