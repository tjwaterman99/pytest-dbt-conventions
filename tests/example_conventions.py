import os


def test_conf(artefacts_conf):
    assert artefacts_conf._dbt_project_dir == os.environ['DBT_PROJECT_DIR']


def test_manifest(manifest):
    assert manifest.name() == 'manifest'
    assert len(manifest.nodes) > 0


def test_catalog(catalog):
    assert catalog.name() == 'catalog'


def test_sources(sources):
    assert sources.name() == 'sources'


def test_run_results(run_results):
    assert run_results.name() == 'run_results'


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



