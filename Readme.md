docker build -t andarroyave.com:1.0.0 .
docker rm andarroyave --force
docker run -d -p 3000:3000 -p 8000:8000 --name andarroyave andarroyave.com:1.0.0