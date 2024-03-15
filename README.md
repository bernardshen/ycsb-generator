# ycsb-generator


## Requirements
```bash
sudo apt install default-jre -y
```

## How to use?
1. `./setup.sh`. This will download and decompress YCSB.
2. Modify workload specifications in `workload_spec` directory.
    - `recordcount` specifies the total number of records.
    - `operationcount` specifies the number of operations.
    - For other fields, refer to `workload_template` for more information.
3. Generate workload with `python gen_all_workloads.py`. This will generate five files under the `workloads` directory, which are `[ycsb.load, ycsba.trans, ycsbb.trans, ycsbc.trans, ycsbd.trans]`.
4. In `workloads` directory. Execute `python3 check.py` to make sure all keys accessed in trans are contained in load, except for ycsbd.