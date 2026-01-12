<div>

<h1>Sistema de Gestão SOPUKA – Backend (Django REST API)</h1>

<p>
Sistema de gestão <strong>backend</strong> desenvolvido para fins académicos, utilizando
<strong>Django REST Framework</strong>, responsável por fornecer uma
<strong>API RESTful</strong> consumida por um frontend desenvolvido em Vue.js.
</p>

<p>
A API gere dados de <strong>Clientes</strong>, <strong>Serviços</strong>,
<strong>Equipas</strong> e <strong>Projetos</strong>, com operações CRUD completas.
</p>

<hr/>

<h2>📌 Tema Escolhido</h2>

<p>
Sistema de Gestão Empresarial para controlo de clientes, serviços, equipas e projetos,
baseado em arquitetura REST.
</p>

<hr/>

<h2>⚙️ Tecnologias Utilizadas</h2>

<ul>
  <li>Python 3</li>
  <li>Django</li>
  <li>Django REST Framework</li>
  <li>SQLite (Base de dados)</li>
  <li>Django CORS Headers</li>
  <li>Gunicorn</li>
  <li>Git & GitHub</li>
</ul>

<hr/>

<h2>🎯 Funcionalidades Principais</h2>

<ul>
  <li>CRUD completo (Criar, Listar, Atualizar e Eliminar)</li>
  <li>API RESTful</li>
  <li>Relacionamentos entre entidades (FK e M2M)</li>
  <li>Integração com frontend Vue.js</li>
  <li>Suporte a métodos GET, POST, PUT e DELETE</li>
</ul>

<hr/>

<h2>🧩 Entidades do Sistema</h2>

<ul>
  <li>Clientes</li>
  <li>Serviços</li>
  <li>Equipas</li>
  <li>Projetos</li>
</ul>

<hr/>

<h2>🗂️ Diagrama das Entidades</h2>

<pre>
CLIENTE
- id
- nome
- email
- telefone
- localizacao

SERVICO
- id
- nome
- tipo
- descricao
- preco_base

EQUIPA
- id
- nome
- funcao
- especialidade
- contacto

PROJETO
- id
- cliente (FK)
- servicos (M2M)
- equipas (M2M)
- data_inicio
- data_fim
- estado
- local_execucao
</pre>

<hr/>

<h2>🔗 Endpoints da API</h2>

<h3>Clientes</h3>

<ul>
  <li>GET /api/clientes/ – Listar clientes</li>
  <li>POST /api/clientes/ – Criar cliente</li>
  <li>PUT /api/clientes/{id}/ – Atualizar cliente</li>
  <li>DELETE /api/clientes/{id}/ – Eliminar cliente</li>
</ul>

<p>
As restantes entidades (<strong>Serviços</strong>, <strong>Equipas</strong> e
<strong>Projetos</strong>) seguem o mesmo padrão RESTful.
</p>

<hr/>

<h2>⚙️ Instruções de Execução</h2>

<pre>
git clone https://github.com/SEU_USUARIO/backend-django-gestao.git
cd backend-django-gestao

python -m venv venv
venv\Scripts\activate   (Windows)

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
</pre>

<p>API disponível em:</p>

<pre>
http://127.0.0.1:8000/api/
</pre>

<hr/>

<h2>🎓 Objetivo Académico</h2>

<p>
Projeto desenvolvido para fins académicos, com foco na aplicação prática de:
</p>

<ul>
  <li>APIs REST</li>
  <li>Arquitetura Backend</li>
  <li>Integração Frontend / Backend</li>
</ul>

<hr/>

<h2>👤 Autor</h2>

<p>
<strong>Elias Sopupa</strong><br/>
Projeto Académico – Django REST Framework
</p>

</div>
