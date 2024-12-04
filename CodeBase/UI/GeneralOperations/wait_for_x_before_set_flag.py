import time


def wait_for_x_before_set_flag(duration, flag_to_set):
    start_time = time.time()
    while not flag_to_set.is_set() and (time.time() - start_time) < duration:
        elapsed = time.time() - start_time
        #print(f"Timer: {elapsed:.1f} seconds")
        time.sleep(1)
    if not flag_to_set.is_set():
        print("Timer completed.")
        flag_to_set.set()
    else:
        print("Timer stopped early.")