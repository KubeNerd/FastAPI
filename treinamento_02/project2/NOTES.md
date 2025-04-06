## Migrations
```sh
    docker-compose run --user 1000 app sh -c 'alembic init migrations'
```

```sh
    docker-compose run --rm app sh -c 'alembic revision --autogenerate -m "add categories table"'
    docker-compose run --rm app sh -c 'alembic revision  -m "upgrade head"'

```


## Permissão de editar arquivos
```sh
    sudo chown myuser:myuser /home/myuser/KubeNerd/FastAPI/treinamento_02/project2/application/alembic.ini
```

## Pytest
```sh
   docker-compose run app sh -c "pytest -k test_add_category_uc"
```