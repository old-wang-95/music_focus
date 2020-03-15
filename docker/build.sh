cd ..
dt=`date '+%Y%m%d_%H%M%S'`
commit_id=`git log -1 | head -1 | awk '{print substr($2,1,8)}'`
img_name=music_focus:${dt}_${commit_id}
docker build -f docker/Dockerfile -t $img_name .
docker tag $img_name music_focus:latest
