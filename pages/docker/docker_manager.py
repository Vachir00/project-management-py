import docker

client = docker.from_env()


def list_containers():
    """Lista todos los contenedores activos."""
    containers = client.containers.list()
    return containers


def list_images():
    """Lista todas las imágenes de Docker."""
    images = client.images.list()
    return images


def list_volumes():
    """Lista todos los volúmenes de Docker."""
    volumes = client.volumes.list()
    return volumes
