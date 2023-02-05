# dbt_dry_run

dbt_dry_run is A meltano utility extension for dbt_dry_run that wraps the `dbt-dry-run` command.

## Installing this extension for local development

1. Install the project dependencies with `poetry install`:

```shell
cd path/to/your/project
poetry install
```

2. Verify that you can invoke the extension:

```shell
poetry run dbt_dry_run_extension --help
poetry run dbt_dry_run_extension describe --format=yaml
poetry run dbt_dry_run_invoker --help # if you have are wrapping another tool
```

## Template updates

This project was generated with [copier](https://copier.readthedocs.io/en/stable/) from the [Meltano EDK template](https://github.com/meltano/edk).
Answers to the questions asked during the generation process are stored in the `.copier_answers.yml` file.

Removing this file can potentially cause unwanted changes to the project if the supplied answers differ from the original when using `copier update`.
