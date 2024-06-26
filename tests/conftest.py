import os

import pytest
from atomea.schemas.workflow.amber import Amber22Schema

from simlify import enable_logging
from simlify.simulation.contexts import SimlifyConfig

TEST_DIR = os.path.dirname(__file__)


@pytest.fixture
def test_dir():
    return os.path.abspath(TEST_DIR)


@pytest.fixture(scope="session", autouse=True)
def turn_on_logging():
    enable_logging(10)


@pytest.fixture
def dir_structures():
    return os.path.join(TEST_DIR, "files/structures")


@pytest.fixture
def path_1jc0():
    return os.path.join(TEST_DIR, "files/structures/1JC0.pdb")


@pytest.fixture
def path_1jc0_prepped():
    return os.path.join(TEST_DIR, "files/structures/1JC0-prepped.pdb")


@pytest.fixture
def path_cro_fcrmod():
    return os.path.join(
        TEST_DIR, "files/ff/amber-ff-chromo-params/frcmod.xFPchromophores.2022"
    )


@pytest.fixture
def path_cro_lib():
    return os.path.join(
        TEST_DIR, "files/ff/amber-ff-chromo-params/xFPchromophores.lib.2022"
    )


@pytest.fixture
def amber_sim_standard_config():
    simlify_config = SimlifyConfig()
    simlify_config.engine = Amber22Schema()
    simlify_config.label = "01_min"
    simlify_config.rendering.dir_work = os.path.join(TEST_DIR, "tmp")
    simlify_config.engine.cli.compute_platform = "pmemd.MPI"
    simlify_config.engine.ff.protein = "ff19SB"
    simlify_config.engine.ff.water = "opc3"
    simlify_config.slurm.ntasks_per_node = 8
    simlify_config.engine.inputs.update(
        {
            "irest": 1,
            "ntx": 5,
            "ig": -1,
            "dt": 0.002,
            "nstlim": 500000,
            "nscm": 500,
            "ntr": 1,
            "restraint_wt": 0.5,
            "restraintmask": "!(:WAT) & (@C,CA,N,O,O5',P,O3',C3',C4',C5')",
            "ntb": 2,
            "ntf": 2,
            "ntc": 2,
            "cut": 10.0,
            "ntt": 3,
            "temp0": 300.0,
            "gamma_ln": 5.0,
            "ntp": 1,
            "barostat": 2,
            "pres0": 1.01325,
            "mcbarint": 100,
            "comp": 44.6,
            "taup": 1.0,
            "ntxo": 2,
            "ntwr": 5000,
            "ntpr": 500,
            "ntwx": 5000,
            "ioutfm": 1,
            "iwrap": 1,
        }
    )
    return simlify_config
