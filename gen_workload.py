# Used to generate single workload with a .load and a .trans from a workload_spec.
import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ycsb_dir = 'YCSB/'
workload_dir = 'workload_spec/'
output_dir= 'workloads/'

if __name__ == "__main__":
    if (len(sys.argv) != 2) :
        print(bcolors.WARNING + 'Usage:')
        print('python3 gen_workload.py workload_name' + bcolors.ENDC)
        exit(0)

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    workload = sys.argv[1]
    
    print(bcolors.OKGREEN + 'workload = ' + workload)
    
    out_ycsb_raw_load  = output_dir + workload + '_raw_load'
    out_ycsb_raw_trans = output_dir + workload + '_raw_trans'
    out_ycsb_load  = output_dir + workload + '.load'
    out_ycsb_trans = output_dir + workload + '.trans'
    
    cmd_ycsb_load  = 'python2 ' + ycsb_dir + 'bin/ycsb load basic -P ' + workload_dir + workload + ' > ' + out_ycsb_raw_load
    cmd_ycsb_trans = 'python2 ' + ycsb_dir + 'bin/ycsb run basic -P '  + workload_dir + workload + ' > ' + out_ycsb_raw_trans
    
    os.system(cmd_ycsb_load)
    os.system(cmd_ycsb_trans)

    # compress output
    f_load = open(out_ycsb_raw_load, 'r')
    f_load_out = open(out_ycsb_load, 'w')
    out_lines = []
    for line in f_load:
        if line[0] != 'I':
            continue
        cols = line.split()
        if cols[0] != 'INSERT':
            continue
        out_lines.append(cols[0] + ' ' + cols[2][4:] + '\n')
    print('loaded: ', len(out_lines))
    f_load.close()
    f_load_out.writelines(out_lines)
    f_load_out.close()

    f_trans = open(out_ycsb_raw_trans, 'r')
    f_trans_out = open(out_ycsb_trans, 'w')
    out_lines = []
    for line in f_trans:
        if line[0] not in ['I', 'R', 'U']:
            continue
        cols = line.split()
        if cols[0] not in ['INSERT', 'READ', 'UPDATE']:
            continue
        out_lines.append(cols[0] + ' ' + cols[2][4:] + '\n')
    print('trans: ', len(out_lines))
    f_trans.close()
    f_trans_out.writelines(out_lines)
    f_trans_out.close()
    
    cmd = 'rm -f ' + out_ycsb_raw_load
    os.system(cmd)
    cmd = 'rm -f ' + out_ycsb_raw_trans
    os.system(cmd)