"""The registry of this repository is valid: goldpan reads it, every record says where it comes from, and the few facts that other
code relies on are stated. It needs the released goldpan (`pip install goldpan pytest`) and nothing else."""
from pathlib import Path

import pytest

registry = pytest.importorskip("goldpan.registry")

FOLDER = Path(__file__).resolve().parents[1]


def reg():
    return registry.load(FOLDER, use_environment=False)


def test_the_folder_is_a_valid_registry_and_every_entry_says_where_it_comes_from():
    r = reg()
    assert r.detectors() and r.readouts()
    for rec in list(r.detectors().values()) + list(r.readouts().values()):
        assert rec.status in registry.STATUSES and rec.evidence.strip()
    for rec in r.detectors().values():
        if rec.readout is not None:
            r.readout_config(rec.readout)                                    # the readout it names exists


def test_nai_s2_is_the_run_76_detector_with_the_six_side_2_phonon_channels():
    rec = reg().detector("NAI-S2")
    idx = rec.read_defaults("idx")
    assert sorted(idx["channels"]) == ["Side2pA", "Side2pB", "Side2pC", "Side2pD", "Side2pE", "Side2pF"]
    assert set(idx["roles"]) == set(idx["channels"]) and set(idx["roles"].values()) == {"phonon"}
    assert rec.status in registry.STATUSES and "07221203_2025" in rec.series and rec.number == 1


def test_the_run_76_readout_has_the_sample_period_and_states_its_measurement():
    rec = reg().readouts()["DCRC_RUN76"]
    assert rec.config.sample_period_s == 0.8e-6 and rec.config.glitch_samples == 10
    assert "480 to 520" in rec.evidence                                      # the measurement the pretrigger window rests on
    assert 0 < rec.config.pretrigger_samples < 1000
