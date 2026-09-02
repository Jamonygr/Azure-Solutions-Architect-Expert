from __future__ import annotations

import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from validate_repository import command_allowed, extract_commands


class LaneParsingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = yaml.safe_load((ROOT / "curriculum/commands.yml").read_text(encoding="utf-8"))

    def test_extracts_cli_behind_assignment(self) -> None:
        commands = extract_commands("$group = az group show --name $ResourceGroup --output json | ConvertFrom-Json")
        self.assertEqual(len(commands), 1)
        self.assertTrue(commands[0].startswith("az group show"))

    def test_extracts_az_and_graph_cmdlets(self) -> None:
        commands = extract_commands("$resource = Get-AzResource -ResourceId $Id\nGet-MgUser -UserId $UserId")
        self.assertEqual(commands, ["Get-AzResource", "Get-MgUser"])

    def test_does_not_treat_module_name_as_cli(self) -> None:
        self.assertEqual(extract_commands("Get-Module Az.Accounts,Az.Resources"), [])

    def test_registry_accepts_lane_command(self) -> None:
        self.assertTrue(command_allowed("az group show --name example", "azure-cli", self.registry))
        self.assertTrue(command_allowed("Get-AzResource", "azure-powershell", self.registry))
        self.assertTrue(command_allowed("Get-MgUser", "azure-powershell", self.registry))

    def test_registry_rejects_unregistered_surface(self) -> None:
        self.assertFalse(command_allowed("az imaginary create", "azure-cli", self.registry))
        self.assertFalse(command_allowed("Invoke-UnknownCloud", "azure-powershell", self.registry))


if __name__ == "__main__":
    unittest.main()
