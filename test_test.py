# import pytest
# import requests
#
#
# class Test:
#     # x_data = [1, 2, 3]
#     #
#     # @pytest.mark.parametrize("x", x_data, ids=lambda val: f'testing {val}')
#     # def test_ceva(self, x):
#     #     assert x < 4
#
#     @pytest.fixture()
#     def test_generate_data(self):
#         return range(5)
#
#     @pytest.mark.parametrize("y", [5, 6, 7], ids=lambda val: f'testing {val}')
#     @pytest.mark.parametrize("x", [1, 2, 3], ids=lambda val: f'testing {val}', )
#     def test_ceva2(self, x, y, request):
#         print([val for val in request.getfixturevalue('test_generate_data')])
#         assert x < y
