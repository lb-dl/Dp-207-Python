from .file_parser import *
import pytest
import mock
import builtins


@pytest.fixture
def mock_data_file(tmpdir):
    test_file = tmpdir.mkdir("test_path").join("file.txt")
    test_file.write('Elementary task. File parser task 4')
    return test_file


def test_count_lines(mock_data_file):
    test_count_str = CountString(mock_data_file, 'task')
    test_res = test_count_str.get_number_of_given_str()
    assert test_res == '2 strings were found in the file'


def test_replace_lines(mock_data_file):
    ReplaceString(mock_data_file, 'task', 'python task').replace_str()
    assert mock_data_file.read() == 'Elementary python task. File parser python task 4'


def test_user_input_2_params():
    with mock.patch.object(builtins, 'input', lambda _: 'file.txt, task'):
        assert get_params() == ['file.txt', 'task']


def test_user_input_3_params():
    with mock.patch.object(builtins, 'input', lambda _: 'file.txt, task, python task'):
        assert get_params() == ['file.txt', 'task', 'python task']


def test_user_answer_yes():
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert __eq__(is_exit(), True)
