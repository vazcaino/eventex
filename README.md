# Eventex Lvz

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/vazcaino/eventex.svg?branch=master)](https://travis-ci.org/vazcaino/eventex)

[![Maintainability](https://api.codeclimate.com/v1/badges/24fd12151d59f4f95430/maintainability)](https://codeclimate.com/github/vazcaino/eventex/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/24fd12151d59f4f95430/test_coverage)](https://codeclimate.com/github/vazcaino/eventex/test_coverage)

## Como desenvolver:

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:vazcaino/eventex.git wttd_lvz
cd wttd_lvz
python -m venv .wttd_lvz
source .wttd_lvz/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY
4. Defina DEBUG=False
5. Configure o serviço de e-mail
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configurar e-mail
git push eventex master --force
```



