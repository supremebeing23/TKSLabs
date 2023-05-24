#LAB06 cADVISOR
```
 sudo docker run \
   --volume=/:/rootfs:ro \
   --volume=/var/run:/var/run:ro \
   --volume=/sys:/sys:ro \
   --volume=/var/lib/docker/:/var/lib/docker:ro \
   --volume=/dev/disk/:/dev/disk:ro \
   --publish=8080:8080 \
   --detach=true \
   --name=cadvisor \
   --privileged \
   --device=/dev/kmsg \
   gcr.io/cadvisor/cadvisor:v0.36.0
Unable to find image 'gcr.io/cadvisor/cadvisor:v0.36.0' locally
v0.36.0: Pulling from cadvisor/cadvisor
9d48c3bd43c5: Pull complete
f7d6cbe0ad90: Pull complete
ec9db44a3ab4: Pull complete
Digest: sha256:5ee8e2734bb79a0cf8a1f87e10458527105273006b033e617f0ba848088c9cfc
Status: Downloaded newer image for gcr.io/cadvisor/cadvisor:v0.36.0
10d27c20af69c38d247d1663e64ddf404b421c0c93129e9c544d01b1c2836f0a
```



