# Prova do SO - Raquel Martiniano Félix Pires

## Introdução:
Nessa atividade, mostra como é a execução do docker junto com Django, podendo baixar tudo em uma só vez, inclusive com linux, assim acessando um sistema web que o desenvolvedor pode criar e fazer em um local só, ficando tudo mais fácil.

## Relato de atividades:
1. Primeiro entre a pasta app com esse comando
![Entrando pasta app](/imagens/Captura%20de%20tela%202026-03-23%20081418.png)

2. Depois que criou o dockerfile e modificado, terá que usar esse comando para criar uma imagem com esse build
![usando o dockerfile para buildar](/imagens/Captura%20de%20tela%202026-03-23%20081448.png)

3. Agora pode usar o docker run para ele funcionar junto com docker local aberto!
![usando o dockerfile para run](/imagens/Captura%20de%20tela%202026-03-23%20081616.png)

4. Precisa agora usar os três comandos, o primeiro será django-admin startproject myproject . para criar o projeto Django, depois python3 manage.py startapp webapp para fazer o Django ser aplicado e funcionar, e python3 manage.py migrate para criar o arquivo do banco de dados, lembrando que preisa modificar alguns arquivos como webapp no INSTALLED_APPS no myproject/settings.py e configurar ALLOWED_HOSTS, colocando '*'
![comandos](/imagens/Captura%20de%20tela%202026-03-23%20085849.png)


5. Precisa usar esse comando para criar sua conta admin para poder mexer o site, precisa colocar nome do usuario, email é opcional, senha e confirmar novamente a senha, com esse comando  python3 manage.py createsuperuser     
![conta admin](/imagens/Captura%20de%20tela%202026-03-23%20085923.png)

6. Depois disso tudo, chamamos o servidor para o site funcionar! Com esse comando python3 manage.py runserver 0.0.0.0:8000
![servidor](/imagens/Captura%20de%20tela%202026-03-23%20081719.png)

7. No fim, receberá o resultado das páginas como esse comum do usuário, pelo link do localhost:8000
![servidor](/imagens/Captura%20de%20tela%202026-03-23%20081532.png)

OBS: Não terei como colocar a foto do admin aberto por ter tido problema com senha, já que geralmente pede o nome do usuário e senha que criou antes.

## Considerações finais: 
As dificuldades que tive foi mais o problema de senha que provavelmente eu não ativei o "Num Lock" e mesmo assim o comando recebeu, mas no sevridor de admin, não aceita a senha.

Além disso, aprendi mais como usar o arquivo md para colocar a imagem e a noção abrangiu mais o uso do Django com o docker, conseguindo visualizar o servidor conforme editei dentro do Django.

 






