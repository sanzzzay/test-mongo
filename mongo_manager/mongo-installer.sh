# Pull MongoDB image:
docker pull mongo
# Run MongoDB container:
docker run --name mongodb -d -p 27017:27017 mongo
# Check running containers:
docker ps