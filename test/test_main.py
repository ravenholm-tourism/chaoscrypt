from src import main
import pytest

# @pytest.mark.skip()
def test_cli_args():
  x0 = 232323e-6
  b = 3.8
  text = 'hi'
  xmit = '--xmit .9'
  argv = f'{x0} {b} {text} {xmit}'.split()
  response = main.main(argv)
  nums = [int(_) for _ in response.split(',')]
  assert nums[0] >= 2077 and nums[1] >= 5

# @pytest.mark.skip()
def test_cli_args_noxmit():
  x0 = 232323e-6
  b = 3.8
  text = 'hi'
  argv = f'{x0} {b} {text}'.split()
  response = main.main(argv)
  nums = [int(_) for _ in response.split(',')]
  assert nums == [2077, 5]