import pytest
import os
from artefacts import Manifest, Sources, RunResults, Catalog


def test_config(artefacts_config):
    target_dir = os.path.join(artefacts_config.get('dbt_project_dir'), 'target')
    manifest_filepath = os.path.join(target_dir, 'manifest.json')
    assert os.path.exists(manifest_filepath)


def test_manifest(manifest):
    assert type(manifest) == Manifest.model
    assert len(manifest.nodes) > 0


def test_catalog(catalog):
    assert type(catalog) == Catalog.model


def test_sources(sources):
    assert type(sources) == Sources.model


def test_run_results(run_results):
    assert type(run_results) == RunResults.model


def test_model(model):
    assert model.resource_type == 'model'


def test_test(test):
    assert test.resource_type == 'test'


def test_seed(seed):
    assert seed.resource_type == 'seed'


def test_source(source):
    assert source.resource_type == 'source'


def test_exposure(exposure):
    assert exposure.resource_type == 'exposure'


def test_metric(metric):
    assert metric.resource_type == 'metric'


def test_macro(macro):
    assert macro.resource_type == 'macro'


def test_selector(selector):
    assert type(selector) == dict


def test_operation(operation):
    assert operation.resource_type == 'operation'


def test_snapshot(snapshot):
    assert snapshot.resource_type == 'snapshot'
