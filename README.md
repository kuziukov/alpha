# Alpha

Launch REDIS and MONGODB via docker-compose
```sh
docker run -d --name redis-test -p 6379:6379  -v /path/to/redisconf/redis.conf:/redis.conf redis redis-server /redis.conf

docker start redis-test
docker stop redis-test

docker-compose stop
docker-compose -f docker-compose.yml up --build
```
