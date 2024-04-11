import pytest
@pytest.fixture()
def setup_teardown():
    print("Setup")
    yield
    print("Teardown")
class KrishnaBuiltInMarker:

    name='Sri Krishna'
    @pytest.mark.skip(reason="Intentional Skip")
    def krishna_func1(self):
        print("inside Krishna Function 1")
        assert "Krishna" in "Sri Krishna"
    @pytest.mark.skipif(name.__eq__("Sri Krishna"),reason='Conditional Skip')
    def krishna_func2(self):
        print("inside Krishna Function 2")
        assert "Krishna" not in self.name

    @pytest.mark.xfail
    @pytest.mark.usefixtures('setup_teardown')
    def krishna_func3(self):
        print("inside Krishna Function 3")
        assert True

    @pytest.mark.xfail
    def krishna_func4(self):
        print("inside Krishna Function 4")
        assert False
    @pytest.mark.parametrize('Name,Deviji',[('Sri Krishna','Sri Rukmini'),('Sri Krishna','Sri Satyavama')])
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def krishna_func5(self,Name,Deviji):
        print("inside Krishna Function 5")
        assert 4 == 3+1
        print(f"Name:-{Name} , Deviji:-{Deviji}")
        pytest.yield_fixture()