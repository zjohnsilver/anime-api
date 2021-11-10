CONTAINER_NAME=anime-api

docker/start:
	docker-compose up -d --build

docker/stop:
	docker-compose down

docker/logs:
	docker logs -f $(CONTAINER_NAME)

docker/exec:
	docker exec -it $(CONTAINER_NAME) sh