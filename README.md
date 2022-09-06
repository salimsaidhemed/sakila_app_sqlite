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
- [**deployment.yaml**](./deployment.yaml) - Defines a Kubernetes deployment. A Deployment provides declarative updates for [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) and [ReplicaSets](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/).
- [**docker-compose.yml**](./docker-compose.yml) - Defines services, networks, and volumes for this Docker application.
- [**dockerfile**](./dockerfile) - Contains Commands used to assemble the Application Image. 
    - Ensures the Work directory `/app` exists
    - Copies the `requirements.txt` file to the container and installs all specified required `pip` modules
    - Runs the `app.py` File to start the application
- **models** - A Directory containing classes Subclassing the `Flask-SQLAlchemy` ORM Model and is used to define Database models that will map to tables in the database.
- [**requirments.txt**](./requirements.txt) - A file listing all the dependencies (and dependecies of dependencies) for this project
- **services** - Consist of a number of utility Classes and functions that can be used by other parts of the App.
- [**service.yaml**](./service.yaml) - A Kubernetes configuration file used to define how an application running in [Pods]https://kubernetes.io/docs/concepts/workloads/pods/) is exposed.
- **static** - Static Files (CSS,js,images etc). Though in Production a CDN is preferred.
- **templates** - jinja templates that are rendered to display the Application content
- **templates/fragments** - Commonly used HTML code (like navbars,footers,headers) that can be included in other templates.
- [**templates/base.html**](./templates/base.html) - The base template, all other templates import from this.
- [**vagrantfile**](./vagrantfile) - Describe VM architecture,spins up a VM and deploys the the Application to the VM which can be used for testing the app during development.

## Running the App 

### Using Docker Compose

Included with the app is a docker image definition (dockerfile) and a `docker-compose.yml` file to orchetsrate the container and deploy the application in a docker server. To run a Dockerized version of the Application:

1. Ensure port 80 is free (or you can change the `HOST_PORT` variable in the `.env` file to whichever port you like)

2. Ensure you have Docker and docker compose installed. See [Install Docker Engine](https://docs.docker.com/engine/install/)  and [Docker Compose v2](https://github.com/docker/compose)

3. Clone this repo.

4. Run the Command below from the root of this repo to deploy the container and App.

```docker-compose up -d```

this will install required libraries in the container and expose the app on port 80 by default.

