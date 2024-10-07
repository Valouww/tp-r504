docker network create tplb
docker build . -t im-nginx-lb 
mkdir shared{1..2}
echo "<h1>Hello 1</h1>" > shared1/index.html
echo "<h1>Hello 2</h1>" > shared2/index.html
docker run --rm --name nginx1 -d --network=tplb -p 81:80 --mount type=bind,source=/home/valdav/tp-r504/TP-LB/tp-A/shared1/,target=/usr/share/nginx/html nginx:latest
docker run --rm --name nginx2 -d --network=tplb -p 82:80 --mount type=bind,source=/home/valdav/tp-r504/TP-LB/tp-A/shared2/,target=/usr/share/nginx/html nginx:latest
docker run --rm -d --network=tplb -p 83:80 im-nginx-lb
