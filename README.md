# Networking Project 

This is a real tie irc simulation, made for networking project with the help of my team. check out the working [here](https://pure-headland-4185.herokuapp.com). It is based on a simple skeleton provided by heroku for Django, Python.


## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
1. git clone https://github.com/ashwani-pandey/My-Networking-Projects.git
2. cd My-Networking-Projects
3. Follow steps on - https://devcenter.heroku.com/articles/getting-started-with-python#introduction

```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku open
```
