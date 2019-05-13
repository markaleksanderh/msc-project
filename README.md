### MSc Project


Check for running containers
`docker ps`

To kill
`docker kill <CONTAINER ID>`

Remove all
`docker system prune -a`

Build 
`docker build -t msc-project:latest . `


Run
`docker run -d -p 5000:5000 msc-project:latest`