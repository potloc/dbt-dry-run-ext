"""Passthrough shim for dbt_dry_run extension."""
import sys

import structlog
from meltano.edk.logging import pass_through_logging_config
from dbt_dry_run_ext.extension import dbt_dry_run


def pass_through_cli() -> None:
    """Pass through CLI entry point."""
    pass_through_logging_config()
    ext = dbt_dry_run()
    ext.pass_through_invoker(
        structlog.getLogger("dbt_dry_run_invoker"),
        *sys.argv[1:] if len(sys.argv) > 1 else []
    )
