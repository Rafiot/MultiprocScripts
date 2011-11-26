
if __name__ == "__main__":

    from multiprocscripts.multiproc_dir import MultiprocDir
    m = MultiprocDir(max_spawn = 5, sleep_time = 2)
    m.spawn_scripts("test_multiproc_dir.py", "data/multiproc_dir/")

