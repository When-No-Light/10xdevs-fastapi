# Fast api test
## Overview
Example project with using FastApi and Quasar frameworks. 

## Fast start
1. Generate pants environment  files and TypeScript openapi client:
```console
make set_up
```
2. Run backend 
```console
make run_backend
```
3. In another terminal run frontend
```console
make run_frontend
```

## Additional information
This template has predefined pipeline for testing, validation and deploying app to VM.

## CI/CD 
#### Variables:
 - VM_HOST_KEY - VM (virtual machine) public key
 - VM_HOST - VM ip or domain address
 - VM_USER - VM user name
 - VM_PRIVATE_KEY - VM user private key



#### Docker 
Installing this application on a virtual machine consists of launching a container with an Nginx proxy that accepts requests on port 80 and then redirects them over the Docker network to a container running another Nginx server containing the generated web application files, and container with running FastApi application that listens on port 5000. Frontend and backend applications can only be accessed (from outside) through a Nginx proxy server.

To redirect requests to a specific entry point, address are processed by the Nginx proxy server. VIRTUAL_HOST (subdomain.domain or domain) must be set in each container that we want to get requested with Nginx proxy.

#### How to open web pages from browser (The section may have outdated data!)
Make sure that you have predefined domain addresses in `/etc/hosts` (10.0.0.40 fastapi.example and 10.0.0.40 fastapi.example)

Web app: http://fastapi.example
FastAPI: http://api.fastapi.example


## Fast api best practices

https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file
