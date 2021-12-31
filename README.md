# Django Channels Real Time Chat Application

## About Project

<p>
  Olá, este é um projeto de estudo sobre websockets com Django Channels, é um chat app bem simples que pode ser usado para conversar com usuários dentro de uma sala criada por você ou outros usuários, esse projeto é interessante para compreender como websockets funcionam e como ele pode ser usado com Django para resolver problemas como a sincronização ou processos assincronos de dados que precisam ser mostrados para o usuário em tempo real, como mensagens de conversas, notificações e processos em segundo plano o que abre muitas possibilidades a serem exploradas.
</p>

### How Start The Project?

Primeiro de tudo vamos clonar este repositório
````
git clone https://github.com/Monke001/chat_app.git
cd chat_app
````
Agora instalamos as dependencias dentro do requimeremts.txt, mas primeiro ativamos nossa venv
````
python3 -m venv venv
cd venv/Scripts/activate
pip install -r requirements.txt
````
Então rodamos o projeto, recomendo trocar o superuser do projeto para ter acesso a page admin e também rodar os comandos makemigrations e migrate
````
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
````

### Features

<p>
  Algumas das features principais do projeto feitas foram:
</p>

- Salas de chat em tempo real, possibilitando a saida e mostrando uma mensagem de quando o usuário entra ou sai da sala.
- Salas privadas, o usuário pode ter conversas privadas com outros usuários, assim como aceitar a solicitação de contato ou mesmo enviar uma solicitação.
- Comentários em tempo real, podendo excluir o comentário feito e também responder outros comentários.
- Sistema de likes em posts e contagem de visualização.

### The Future

<p>
  Apesar de ser um projeto de estudo eu penso em deixar ele melhor adicionando mais features como um sistema de notificações, area administrativa das salas de chat para o criador adicionar admin a outros usuários, bloquear usuários, até mesmo criar salas privadas a serem acessadas com código gerado automaticamente ou que permitam apenas adicionar amigos, há muitas features interessantes que podem e talvez serão adicionadas no futuro, até porque o projeto cumpre a função de estudo inicial sobre Django Channels, mas é muito divertido adicionar essas features então até breve provavelmente.
</p>

### This project was deployed!

<p>
  Eu realizei o deploy desse projeto no Heroku, ele não foi muito intuitivo de fazer quanto fazer um deploy normal sem usar Django Channels, mas consegui fazendo algumas pesquisas rápidas no google, você pode conferir o live project neste link <bold><a href="https://monke-chatapp.herokuapp.com/" target="_blank">Chat App</a></bold>. Lista de usuários padrão:
</p>

- usuário: user01, senha: teste1010
- usuário: user02, senha: teste1010
- usuário: user03, senha: teste1010
- usuário: user04, senha: teste1010
- usuário: user05, senha: teste1010

<hr />

#### Obrigado por estar aqui, eu nunca vou parar, vou ficar um pouco melhor a cada dia trazendo projetos cada vez mais interessantes.

<p align="center">
  <img src="https://jonchaisson.files.wordpress.com/2021/10/anime-writing.gif" width=70% />
</p>
