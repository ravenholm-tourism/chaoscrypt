from src import main
import pytest

# @pytest.mark.skip()
def test_cli_args():
  x0 = 232323e-6
  b = 3.8
  text = 'hi'
  argv = f'{x0} {b} {text}'.split()
  response = main.main(argv)
  assert response == '2077, 5'