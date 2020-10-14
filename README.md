# ECE444-F2020-Lab3
# Lab 4-5
Name: Jason Shang  
Note: This repo contains material from https://github.com/miguelgrinberg/flasky  

Instructions for Docker:
The Dockerfile is included in the same folder as the rest of the files required (hello.py, requirements.txt).
To build, run: "docker build -t app_name:latest . "
(choose the name and tag of your choosing).
To run, use: "docker run -it --name app_name --rm -p 5000:5000 app_name"
and change name and options based on what is desired.
After running, the site should now be accessible.
(Note: on some Windows devices, may need to use http://127.0.0.1:5000/ to access due to OS differences)

Screenshots can be seen below:
Example of running the Docker command: <br />
![Screenshot 1](https://github.com/NautilusGitHub/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/lab4_img1.png)
Screenshot of resulting webpage: <br />
![Screenshot 2](https://github.com/NautilusGitHub/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/lab4_img2.png)
Screenshot of Docker Image: <br />
![Screenshot 3](https://github.com/NautilusGitHub/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/lab4_img3.png)

Differences between Containers and Virtual Machines (VMs):
Virtual machines essentially run a secondary operating system on the host machine, and have a lot of overhead required in order to support it all, making it more cumbersome if all you want to do is run another application. Docker containers, on the other hand, are more portable and lightweight, and simply runs a process that has all its requirements encapsulated to isolate it from the rest of the machine.
