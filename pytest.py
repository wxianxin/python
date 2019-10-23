########################################################################################
# pytest
########################################################################################

# pytest's scope is special
# A test function can access variables outside it the scope


pytest test_mod.py::test_func
pytest test_mod.py::TestClass::test_method

pytest -v -s -r p,f,E -p no:warnings test_loan.py::test_el --ignore BEAST2/test/integration_test.py BEAST2/test/

    -v
    -s
    -r p,f,E
    -p no:warnings

    --tb=line

# py.test -s shows stdout of successful tests
########################################################################################
# test fixture
# to provide a fixed baseline upon which tests can reliably and repeatedly execute
@pytest.fixture
def genearte_seires():
    s = pd.Series()
    return s


def test_loan(s):
    assert s == s



# capture Exception:
    with pytest.raises(AttributeError) as e:
        loan.__getattr__(arbitrary_str)
    assert "BEAST2: Loan class cannot find the desired attribute" in str(e.value)


# conftest.py
# put pytest.fixture here and share the fixture across module/session


########################################################################################
# pytest-cov
########################################################################################
pytest --cov \
    --cov-fail-under=80 \
    --cov-report=term-missing \
    --json=.report.json \
    --cov-config=.coveragerc \
    tests/test_testing.py

