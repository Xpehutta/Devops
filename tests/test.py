from src.main import main

def test():
    main_list = main(file_name='contacts_part.xz', directory='/test', return_fl = True)
    compare_list = []
    with open('/test/compare_result.txt') as f:
        for line in f.readlines():
            _l = line.split('\t')
            compare_list.append([_l[0], int(_l[1]), int(_l[2].strip())])
    
    for _ in range(10):
        assert main_list[_] == compare_list[_]
