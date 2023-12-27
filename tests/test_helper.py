from ievals.cli.ieval import get_evaluator


def test_get_evaluator():
    enc_cls = get_evaluator('Qwen/Qwen-7B-Chat') 
    assert 'HF_Chat' in str(enc_cls)
    enc_cls = get_evaluator('Qwen/Qwen-7B') 
    assert 'Qwen' in str(enc_cls)

