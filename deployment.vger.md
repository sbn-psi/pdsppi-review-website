Server: vger:3434 --> 8000

push to git branch (deployment)

ssh into vger

cd to project

git pull branch (deployment)

< copy env files from dev machine? >

docker-compose -f docker-compose.vger.yml up -d --build

ssh into web container
	./manage.py migrate
	./manage.py createsuperuser
	exit

log into /admin with super user

** follow README.md from here