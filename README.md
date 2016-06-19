# Eventex

Sistemas de eventos

[![Build Status](https://travis-ci.org/jvsl/wttd.svg?branch=master)](https://travis-ci.org/jvsl/wttd)
[![Code Health](https://landscape.io/github/jvsl/wttd/master/landscape.svg?style=plastic)](https://landscape.io/github/jvsl/wttd/master)

## como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone https://github.com/jvsl/wttd.git
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?
1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure um serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py
heroku config:set DEBUG=False
# Configure o email
git push heroku master --force
```

