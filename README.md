# Sakila Sample App - SQLite Version

This is a Sample App that was created to take advantage of the Sakila Sample Database. I use this a proof of concept App to implement and learn concepts such as:

- Deployments
- Test Driven Deployments
- Monitoring (Prometheus/Grafana)
- Log Analysis (ELK Stack)
- Containers (Docker,Kubernetes,podman)
- Virtual Machines (Vagrant)
- CI/CD (Jenkins)
- Reverse Proxy and Ingress Controller

The App is written in python using the Flask framework and uses an embedded sqlite version of the Sakila database

## Architecture

The high level architecture of the application is as seen below:

```
.
├── app.py
├── data
│   └── sakila_master.db
├── deployment.yaml
├── docker-compose.yml
├── dockerfile
├── LICENSE
├── models
│   ├── actor.py
│   ├── film.py
│   └── language.py
├── README.md
├── requirements.txt
├── services
│   └── database.py
├── service.yaml
├── static
│   └── main.css
├── templates
│   ├── actors.html
│   ├── base.html
│   ├── film_actors.html
│   ├── films.html
│   ├── fragments
│   └── index.html
└── vagrantfile
```
- [**app.py**](./app.py) - This is the main application launcher file. It sets up Flask and also includes a function to run the application.
- **data** - A directory which Contains the [embedded database](https://github.com/bradleygrant/sakila-sqlite3), the application queries this and manipulates the sample data stored.
- [**deployment.yaml**](./deployment.yaml) - 

## Running the App 

### Using Docker Compose

Included with the app is a docker image definition (dockerfile) and a `docker-compose.yml` file to orchetsrate the container and deploy the application in a docker server. To run a Dockerized version of the Application:

1. Ensure port 80 is free (or you can change the `HOST_PORT` variable in the `.env` file to whichever port you like)

2. Ensure you have Docker and docker compose installed. See [Install Docker Engine](https://docs.docker.com/engine/install/)  and [Docker Compose v2](https://github.com/docker/compose)

3. Clone this repo.

4. Run the Command below from the root of this repo to deploy the container and App.

```docker-compose up -d```

this will install required libraries in the container and expose the app on port 80 by default.

