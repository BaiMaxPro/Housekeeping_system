# /bin/bash

docker build ./backend -t chenseanxy/housekeeping-backend
docker push chenseanxy/housekeeping-backend
docker build ./frontend -t chenseanxy/housekeeping-frontend
docker push chenseanxy/housekeeping-frontend
