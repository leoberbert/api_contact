# API RestFul com Python, Flask e MongoDB

API criada com o intuito de demonstrar o cadastro e consulta de contatos, utilizando o Flask + MongoDB.

### Pré-Requisitos:

Docker (https://www.docker.com/)
docker-compose (https://docs.docker.com/compose/install/)

### Passo a Passo da instalação:

```
git clone https://github.com/leoberbert/api_contact.git

cd api_contact
```

### Iniciar o Docker Compose:

```
docker-compose up -d
```

### Utilização

Para realizar o cadastro de um contato, deverá ser utilizando a URL abaixo com método POST com o seguinte conteúdo json:

END POINT: http://172.17.198.133:5000/add_contact

```
{
        "name" : "Joao Grilo",
        "contact" : "11970801010"
}
```
Para realizar a consulta do contato cadastrado, deverá ser utilizando a URL abaixo com método GET com o seguinte conteúdo json:

END POINT: http://172.17.198.133:5000/get_contact

```
{
        "contact" : 11970801010
}
```
OBS: Substitua o endereço IP acima pelo endereço IP da máquina onde o docker está sendo executado. Recomendo a utilização do POSTMAN(https://www.postman.com/downloads/) para realização dos testes.
