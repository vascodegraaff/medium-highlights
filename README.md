## Medium Highlights

## Description

Django project to crawl links of top articles from the medium archive using beautiful soup.

## Demo

https://medium-highlights.herokuapp.com/

![demo screenshot](https://i.imgur.com/nE6mysX.png)


If you install the mediumship chrome extension, you can bypass the paywall

https://github.com/swapagarwal/mediumship



## How I choose the categories

![Medium Category Graph](https://i.imgur.com/7RIzLvV.png)


## How to install

make a new directory and create a virtual environment to install all the requirements.

run these commands in your terminal

```
$ mkdir medium-highlights
```

Create a virtual envrionment

```
$ virtualenv env
```

activate the virtual environment

```
$ source env/bin/activate
```

now we need to install all the required libraries from the requirements.txt file. We can do this by running the command below. (env) shows that the virtual enviroment is activated and the libraries you install wont directly be installed into your system but instead just to this folder

```
(env) $ pip install -r requirements.txt
```

Then you should be able to run the app locally with the command

```
(env) $ python manage.py runserver
```

## Issues

One problem I came across was that most articles have many tags assosiated with in and when I scraped medium's archieve I would get many entries of the same article, the simple solution I came up with was just to remove the duplicate entries eventhough they may have many tags. Right now this works perfectly fine and I'm not too bothered about trying to add multiple tags on each article.
