### MSc Project

Run
`docker-compose up`

Check if package installed
`docker exec <CONTAINER ID> pip list`

For some reason, Flask-Graphl, Graphene, Py2neo packages aren't installing so before running compose add packages.

Use `docker exec` with server container id and run `pip install` with `graphene`, `py2neo` and `flask-graphql`.





---

GraphQL

Query:
```
query {
  projects {
    name
    description
  }
}
```


---

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