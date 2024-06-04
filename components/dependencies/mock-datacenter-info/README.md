# Building and Pushing Docker Image using Podman

1. Ensure that you have Podman installed on your machine. If not, you can install it using the following command:

```bash
brew install podman
```

```
cd components/dependencies/mock-datacenter-info/imagebuild/
```

2. Build the Docker image using the following command:  
    
```bash
podman build -t mock-datacenter-info:v1 .
```

Test podman Run using Custom IP_OCTET3
```bash
podman run -e IP_OCTET3=58 localhost/mock-datacenter-info:v1
```

Test podman using custom IP_OCTET3 and machine name
```bash 
podman run -e IP_OCTET3=58 -e MACHINE_BASE_NAME=mock-datacenter-info-1 localhost/mock-datacenter-info:v1
```

Remove all exited containers 
```bash
for id in $(podman ps -a --filter "status=exited" --format "{{.ID}}"); do
    podman rm $id
done
```

Push Container image to quay.io
```bash
podman login -u <username> -p <password> quay.io
podman tag mock-datacenter-info:v1 quay.io/<username>/mock-datacenter-info:v1
podman push quay.io/<username>/mock-datacenter-info:v1
```
