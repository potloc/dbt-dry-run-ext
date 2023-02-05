"""Meltano dbt_dry_run extension."""
from __future__ import annotations

import os
import pkgutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import structlog
from meltano.edk import models
from meltano.edk.extension import ExtensionBase
from meltano.edk.process import Invoker, log_subprocess_error

log = structlog.get_logger()


class dbt_dry_run(ExtensionBase):
    """Extension implementing the ExtensionBase interface."""

    def __init__(self) -> None:
        """Initialize the extension."""
        self.dbt_dry_run_bin = "dbt-dry-run"  # verify this is the correct name
        self.dbt_dry_run_invoker = Invoker(self.dbt_dry_run_bin)
        self.dbt_project_dir = Path(os.getenv("DBT_PROJECT_DIR", "transform"))
        self.dbt_profiles_dir = Path(
            os.getenv("DBT_PROFILES_DIR", self.dbt_project_dir / "profiles")
        )

    def invoke(self, command_name: str | None, *command_args: Any) -> None:
        """Invoke the underlying cli, that is being wrapped by this extension.

        Args:
            command_name: The name of the command to invoke.
            command_args: The arguments to pass to the command.
        """
        try:
            if self.dbt_project_dir is not None:
                command_args = command_args + ("--project-dir=" + str(self.dbt_project_dir),)
                log.info(f"Using project-dir at `{self.dbt_project_dir}`...")
            if self.dbt_profiles_dir != "":
                command_args = command_args + ("--profiles-dir=" + str(self.dbt_profiles_dir),)
                log.info(f"Using profile.yml at `{self.dbt_profiles_dir}`...")
            self.dbt_dry_run_invoker.run_and_log(command_name, *command_args)
        except subprocess.CalledProcessError as err:
            log_subprocess_error(
                f"dbt_dry_run {command_name}", err, "dbt_dry_run invocation failed"
            )
            sys.exit(err.returncode)

    def describe(self) -> models.Describe:
        """Describe the extension.

        Returns:
            The extension description
        """
        # TODO: could we auto-generate all or portions of this from typer instead?
        return models.Describe(
            commands=[
                models.ExtensionCommand(
                    name="dbt_dry_run_extension", description="extension commands"
                ),
                models.InvokerCommand(
                    name="dbt_dry_run_invoker", description="pass through invoker"
                ),
            ]
        )
