# `pytest-dbt-conventions`

_A pytest plugin for linting a dbt project's conventions_

```
pip install pytest pytest-dbt-conventions
```

For a demo project using this linter, please see the `conventions.py` file of the [`poffertjes_shop`](https://github.com/tjwaterman99/poffertjes_shop) project.

## Quickstart

This plugin allows you to lint the conventions of your dbt project using pytest. Linting conventions helps ensure your project follows best practices, however you choose to define them.

To use the plugin, you first need to _compile_ your dbt project.

```
dbt compile
```

Next, create a file called `conventions.py` in the root of your dbt project. Here's an example `conventions.py` file, with a single rule that requires all models in your dbt project to have a description.

```py
# conventions.py

def test_models_have_descriptions(model):
    assert model.description is not None

```

To run the linter, use `pytest`.

```
pytest -v conventions.py
```

You'll see output similar to the following.

```
================================================ test session starts ================================================
platform linux -- Python 3.9.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /root/.cache/pypoetry/virtualenvs/poffertjes-shop-UnYrmav3-py3.9/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/poffertjes_shop
plugins: dbt-conventions-0.1.0a2
collected 5 items                                                                                                   

conventions.py::test_models_have_description[model.poffertjes_shop.base_shoppes] PASSED                       [ 20%]
conventions.py::test_models_have_description[model.poffertjes_shop.base_orders] PASSED                        [ 40%]
conventions.py::test_models_have_description[model.poffertjes_shop.base_products] PASSED                      [ 60%]
conventions.py::test_models_have_description[model.poffertjes_shop.base_customers] PASSED                     [ 80%]
conventions.py::test_models_have_description[model.poffertjes_shop.base_order_items] PASSED                   [100%]

================================================= 5 passed in 0.02s =================================================
```

## Using fixtures

This plugin provides several [_fixtures_](https://docs.pytest.org/en/6.2.x/fixture.html#what-fixtures-are) you can use in your `conventions.py` file. 

A fixture is the object that pytest provides to each of your test functions. 

For example, in the function below, the test function is called `test_sources_have_snapshots`, and the fixture is the argument `source` that gets passed to that test function.

```py
def test_sources_have_snapshots(source):
    assert len(source.snapshots) > 0
```

The `pytest-dbt-conventions` plugin provides several fixtures that you can use. For a full list of available fixtures, please see the [reference]() section below.

It's also possible to create your own fixtures. Please see the section [creating fixtures]() for more details.

## Allowing exceptions

Sometimes you expect certain models to fail the linter, so you want the linter to skip testing those models. This often happens when you're implementing a new linting rule for an existing project, and haven't yet fixed all the issues it discovers.

To skip a test for a specific model, you can use [`pytest.xfail()`](https://docs.pytest.org/en/latest/how-to/skipping.html#xfail-mark-test-functions-as-expected-to-fail).


```py
# conventions.py

import pytest

exception_list = ['orders', 'order_items']

def test_models_have_descriptions(model):
    if model.name in exception_list:
        pytest.xfail(f"Allowing failure in {model.name}")

    assert model.description is not None

```


## Creating Custom Fixtures

You can create custom fixtures using pytest and the [`artefacts` api](https://tjwaterman99.github.io/artefacts/api.html#) library. Custom fixtures help keep your conventions DRY.

```py
import pytest
import artefacts.api


models = artefacts.api.models()
base_models = [m for m in models if m.name.startswith('base_')]


@pytest.fixture(params=base_models, ids=[m.name for m in base_models])
def base_model(request):
    yield request.param
    
    
def test_base_models_are_in_correct_directory(base_model):
    assert base_model.path.starts_with('models/base')
```

For more examples of how to create custom fixtures, please see the [`plugin.py`](https://github.com/tjwaterman99/pytest-dbt-conventions/blob/main/pytest_dbt_conventions/plugin.py) module of this package.

## Reference

The available fixtures provided by this plugin are listed below, along with a simple usage example and a link to their reference documentation.

### `model`

An object that represents the models in your project.

```py
def test_model_resource_type(model):
    assert model.resource_type == 'model'
```

Reference - https://tjwaterman99.github.io/artefacts/reference.html?highlight=manifestnode#artefacts.core.ManifestNode

### `test`

An object that represents the tests in your project.

```py
def test_test_resource_type(test):
    assert test.resource_type == 'test'
```

Reference - https://tjwaterman99.github.io/artefacts/reference.html#artefacts.core.ManifestNode

### `seed`

An object that represents the seeds in your project.

```py
def test_seed_resource_type(seed):
    assert seed.resource_type == 'seed'
```

Reference - https://tjwaterman99.github.io/artefacts/reference.html#artefacts.core.ManifestNode

### `source`

An object that represents the sources in your project.

```py
def test_source_resource_type(source):
    assert source.resource_type == 'source'
```

Reference - https://tjwaterman99.github.io/artefacts/reference.html?highlight=manifestsourcenode#artefacts.core.ManifestSourceNode

### `exposure`

An object that represents the exposures in your project.

```py
def test_exposure_resource_type(exposure):
    assert exposure.resource_type == 'exposure'
```

Reference - https://tjwaterman99.github.io/artefacts/reference.html#artefacts.core.ManifestExposureNode

### `metric`

An object that represents the metrics in your project.

```py
def test_metric_resource_type(metric):
    assert metric.resource_type == 'metric'
```

Reference - https://tjwaterman99.github.io/artefacts/reference.html#artefacts.core.ManifestMetricNode

### `macro`

An object that represents the macros in your project.

```py
def test_macro_resource_type(macro):
    assert macro.resource_type == 'macro'
```

Reference - https://tjwaterman99.github.io/artefacts/reference.html#artefacts.core.ManifestMacroNode

### `selector`

An object that represents the selectors in your project.

```py
def test_selector_resource_type(selector):
    assert selector.resource_type == 'selector'
```

The selector is a simple Python dictionary type, ie `dict()`.


### `manifest`

An object that represents the entire manifest artifact generated by `dbt compile`.

```py
def test_manifest_has_nodes(manifest):
    assert len(manifest.nodes) > 0
```

Reference: https://tjwaterman99.github.io/artefacts/reference.html?highlight=manifest#artefacts.core.Manifest
