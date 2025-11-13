The main purpose of the docker is to package and containerize the applications, ship them and run them anywhere any times as many times as it required. 





Containers vs Virtual Machines











Docker images \& Containers

---------------------------



Images are like package or Template plan (just like VM template).

It's used to create one or more containers.





Containers are running instance of images. They are isolated with on environments. 









Docker is all about the container not images

* The images are "building blocks or blueprint or template for the container" It contains the "Our Code + Environment".
* Whereas the container are "The running software of the images"
* Initially we need to build the images then we can run the containers.
* Container is the running application







Docker Commands



docker run filename





Common Commands:

  run         Create and run a new container from an image

  exec        Execute a command in a running container

  ps          List containers

  build       Build an image from a Dockerfile

  pull        Download an image from a registry

  push        Upload an image to a registry

  images      List images

  login       Log in to a registry

  logout      Log out from a registry

  search      Search Docker Hub for images

  version     Show the Docker version information

  info        Display system-wide information

  cp          Copy files/folders between a container and the local filesystem

  inspect     Return low-level information on Docker objects

  kill        Kill one or more running containers







  rename      Rename a container

  restart     Restart one or more containers

  rm          Remove one or more containers

  rmi         Remove one or more images

  save        Save one or more images to a tar archive (streamed to STDOUT by default)

  start       Start one or more stopped containers

  attach      Attach local standard input, output, and error streams to a running container









How to run a Node app file in Docker



1\. One need to create Docker file in the node app



2\. First you need to go into the file directory then install node in docker using " Docker run node" or "sudo apt install node"

   Then you need to run "npm install" This will install all the required file/librares of the node and other configuration files.

   After that you need to run docker command "docker run -p 3000:80 image ID". In this the "-p" is the publicity to run the app

   "3000 is the port number where you need to run the app and map it with the port in the Docker file.

   Now you can visit the local host along with port number you can see the result of the node app.

 





-i, --interactive                    Keep STDIN open even if not attached

-p, --publish list                   Publish a container's port(s) to the host

-P, --publish-all                    Publish all exposed ports to random ports

    --pull string                    Pull image before running ("always",

                                       "missing", "never") (default "missing")

-q, --quiet                          Suppress the pull output





Running a port app

---



If you need to run a port app using any lang the cmd is "docker run -p 8000:80 image ID"

If we want to change the name of the container we can use the cmd name "--name" or docker run -p 8000:80 --name Ganesh ImageID"





Push and Pull of Images

---



If we want to push an images into the docker hub

 

1\. Login to the dokcer hub



2\. Create a name for Image, then Login to Docker, RUN docker run with dockername/imagename



4\. To push images (Public Images) into docker login, to access the images anyone can access it without login



Docker is all about Images and Containers



IMages are the templates/blueprints for Containers, multiple Containers can be created based on one image.

f



Images are either downloaded(docker pull or created with a Dockerfile and docker build.



COPY . .

The first dot is for the entire folder

The second dot is for the entire directory



For Creating a Dockerfile to run any app

---



FROM node (or any other tech your using)



WORKDIR /app (The working dir is app so mention it is app)



COPY package name (like package.json, hello.py)



RUN npm install (for node)



COPY . . /app



EXPOSE 80 (This can be based on the port numbers)



CMD \["node", "server.js"]  (In this based on the tech your using can inculde, "node, python, java or anyother" and mention "filename like server.js"





Understanding Volumes in Docker

---



Volume are folders on your host machine hard drive which are mounted ("made available", mapped) into containers





          Host(your Computer)



/same.path <---------- /app/user-data





Adding Volume to a Container



VOLUME \[ "/app/feedback" ]



In this the app is inside of the container which should be mapped with some folder outside of the container







Removing Anonymous Volumes

---



We saw, that anonymous volumes are removed automatically, when a container is removed.



This happens when you start / run a container with the --rm option.



If you start a container without that option, the anonymous volume would NOT be removed, even if you remove the container (with docker rm ...).



Still, if you then re-create and re-run the container (i.e. you run docker run ... again), a new anonymous volume will be created.



So even though the anonymous volume wasn't removed automatically, it'll also not be helpful



because a different anonymous volume is attached the next time the container starts (i.e. you removed the old container and run a new one).



Now you just start piling up a bunch of unused anonymous volumes - you can clear them via docker volume rm VOL\_NAME or docker volume prune.

