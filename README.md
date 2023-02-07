# dbt_dry_run

dbt_dry_run is A meltano utility extension for dbt_dry_run that wraps the `dbt-dry-run` command.

It is based on a [plugin](https://github.com/autotraderuk/dbt-dry-run) made by the awesome team at AutotraderUK - please support the original creators.

## Plugin specifics
1) As the dry-run functionality is only offered by Bigquery (at the moment), this plugin is **exclusively** for `dbt-bigquery` use.
2) This plugin **requires** that you run `dbt-bigquery compile` before executing; it relies on a fresh compilation. We will be working on an update to make this step automated in the future.


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
