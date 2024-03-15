def load_wl(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

ycsb_load = load_wl('ycsb.load')
key_set = set()
for l in ycsb_load:
    key = l.split(' ')[1]
    key_set.add(key)

trans_list = ['ycsba', 'ycsbb', 'ycsbc', 'ycsbd']

for wl in trans_list:
    trans = load_wl(f'{wl}.trans')
    for l in trans:
        key = l.split(' ')[1]
        assert(key in key_set or wl == 'ycsbd')