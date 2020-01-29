cd ..
dt=`date '+%Y%m%d_%H%M%S'`
docker build -f docker/Dockerfile -t music_focus:$dt .
docker tag music_focus:$dt music_focus:latest
