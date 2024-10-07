docker network create --internal tplb
docker build . -t im-nginx-lb 
mkdir shared{1..2}
echo "<h1>Hello 1</h1>" > shared1/index.html
echo "<h1>Hello 2</h1>" > shared2/index.html
docker run --rm --name nginx1 -d --network=tplb -p 127.0.0.1:80:81 --mount type=bind,source=shared1/,target=/usr/share/nginx/html nginx:latest
docker run --rm --nale nginx2 -d --network=tplb -p 127.0.0.1:80:81 --mount type=bind,source=shared2/,target=/usr/share/nginx/html nginx:latest
docker run --rm -d --network=tplb -p 127.0.0.1:80:83 im-nginx-lb
