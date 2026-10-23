import os
import platform
import time
import numpy as np

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

STUDENT_ID = "230103319"


def main():
    print(f"Student ID: {STUDENT_ID}")
    print(f"OS: {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"CPU Model / Platform: {platform.processor() or 'Not specified'}")

    logical_cores = os.cpu_count()
    print(f"Logical Cores: {logical_cores}")

    seed = int(STUDENT_ID)

    start_time = time.perf_counter()

    rng = np.random.default_rng(seed)
    arr = rng.random(20_000_000, dtype=np.float64)

    total_sum = np.sum(arr)
    std_dev = np.std(arr)

    # Stop wall-clock timer
    end_time = time.perf_counter()
    duration_ms = (end_time - start_time) * 1000.0

    print(f"Array Size: {arr.size}")
    print(f"Sum: {total_sum:.6f}")
    print(f"Standard Deviation: {std_dev:.6f}")
    print(f"Execution Time: {duration_ms:.2f} ms")


if __name__ == "__main__":
    main()