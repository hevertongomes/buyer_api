## API BUYER

## Iniciando

O buyer api foi criado usando a lib flas-restful

### Pré-requisitos

* Docker e Docker-Compose.

### Clonar o Projeto

No seu terminal linux, em um diretório de sua preferência para projetos, digite:

```

git clone https://github.com/hevertongomes/buyer_api.git

```
No diretório do projeto no mesmo nível de pasta de **docker-compose.yml** você precisa criar uma arquivo na raiz do projeto um arquivo chamdo .env pode ser feito usando seu editor. Ele se deve passar o tipo de ambiente onde vai rodar o projeto que pode ser três: development, production,testing. Dentro desse arquivo colocar seguinte código:

```
ENVIRONMENT_PROJECT=development (Pode ser outras das três opções)
```

Após esse processo executar o comando abaixo no mesmo diretório para rodar o projeto

```
docker-compose up
```
