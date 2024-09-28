import docker


def start_database_container():
    client = docker.from_env()
    container_name = "test-db"

    try:
        existing_container = client.containers.get(container_name)
        print(f"Container {container_name} exists. Stopping and removing...")
        existing_container.stop()
        existing_container.remove()
        print(f"Containter {container_name} stopped and removed")
    except docker.errors.NotFound:
        print(f"Container {container_name} does not exist.")

    # Define container configuration
    container_config = {
        "name": container_name,
        "image": "postgres:16.1-alpine3.19",
        "detach": True,
        "ports": {"5432": "5434"},
        "environment": {
            "POSTGRES_USER": "postgres",
            "POSTGRES_PASSWORD": "postgres",
        },
    }

    container = client.containers.run(**container_config)
