# goldreg-R76

The detector registry of the **Run 76** analysis (SuperCDMS-type NaI array, Side-2 readout; the series `07221203_2025`).

It holds the facts about the detectors that the analysis needs and that [goldpan](https://github.com/villano-lab/goldpan) must not contain: a detector's number, type, readout and where each named channel is wired in a given file format. It is **data, not code**: goldpan and [goldsluice](https://github.com/villano-lab/goldsluice) read it (`goldpan.registry`, specification in its docstring) and nothing in them depends on it.

| File | What it holds |
|---|---|
| `run76.toml` | the detectors (`NAI-S2`) with their channel map for idx files |
| `readouts.toml` | the readouts, with the evidence for each number (`DCRC_RUN76`; the `Z7` record stays here until `goldreg-Z7` exists) |

Every entry has a `status` (`confirmed` or `inferred`) and `evidence` that says where it comes from. Write `confirmed` only for what a file or a document says; never write a guess as `confirmed`. A name is defined once.

## Using it

Give the folder to goldpan in one of two ways:

- in a dataset definition: `[dataset] registry = ["../goldreg-R76"]` (relative to the definition file);
- or set the environment variable `GOLDPAN_REGISTRY` to the folder.

```python
from goldpan import registry

reg = registry.load("~/goldreg-R76")
config = reg.readout_config("DCRC_RUN76")        # a goldpan.config.PulseConfig
```

Anything a definition file writes itself wins over the registry.

## Changing it

Work as in [`CONTRIBUTING.md`](CONTRIBUTING.md): a branch from `develop` and a pull request. Edit the TOML by hand, or let a program add a record: `goldpan.registry.add_record(folder, "detectors", name, table)` checks it as the reader does and appends it without touching the rest of the file. Then run

```
python -m pytest
```

For a MIDAS file, `goldpan.adapters.midas.detectors(path)` returns what the file's ODB says about each detector, and `goldpan.registry.compare` checks a record against it.

A change to a number that results depend on (a pretrigger window, a sample period) is announced in [`CHANGELOG.md`](CHANGELOG.md): outputs made with the old value differ and should be made again.

## History

Until 2026-11-05 this was the folder `registry/` of [NSDF-Data](https://github.com/villano-lab/NSDF-Data); its history is kept here. The design is in goldpan issue 150 and in the NSDF-Data task list (item 70): one registry per analysis, `goldreg-R76` and `goldreg-Z7`; a detector is shared by copying its record with `copied_from = "goldreg-R76@<commit>"` next to its `evidence`.
