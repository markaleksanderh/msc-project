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

Mutation:
```
mutation {
  create_project(name: "test") {
    project {
      name: name
    }
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

Rebuild
`docker-compose build` or `docker-compose up --build`

Run
`docker run -d -p 5000:5000 msc-project:latest`