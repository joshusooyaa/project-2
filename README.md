Author: Josh Sawyer
Email: jsawyer@uoregon.edu


app.py
This is a simple server that responds to requests from the client side.

The directory "pages" holds the files that the server will transmit to the client side. In the
case that a request is made for a file that doesn't exist in the directory, a 404 error is
transmitted along with the 404.html file. In the case a request is made with the string '..' or '~' 
then a 403 error is transmitted along with a 403.html file.


Dockerfile:
Docker is used to create a container with the contents of web/ 

To build the image:
docker build -t image_name .

To run the image and create the container:
docker run -d -p local_port:container_port image_name

To stop the container from running:
docker ps --> locate the name of the running container (image_name in repository column)
docker stop container_name
