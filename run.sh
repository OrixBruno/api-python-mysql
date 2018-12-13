docker build -t api-python . \
&& docker run -it --rm -d -p 5000:5000 --name my-api-python api-python \
&& docker logs -f my-api-python