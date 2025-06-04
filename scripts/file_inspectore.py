# file_inspector.py
import os
import time
import datetime

start = time.time()
cutoff_days = 30
min_size_mb = 1
path = "."

def bytes_to_mb(bytes_size):
    return round(bytes_size / (1024 * 1024), 2)

total_files = 0
large_files = []
old_files = []

cutoff_time = time.time() - (cutoff_days * 86400)

for root, _, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        try:
            total_files += 1
            size = os.path.getsize(full_path)
            if size > 1024 * 1024:
                large_files.append((full_path, bytes_to_mb(size)))
            mtime = os.path.getmtime(full_path)
            if mtime < cutoff_time:
                old_files.append((full_path, datetime.datetime.fromtimestamp(mtime)))
        except Exception:
            continue

print(f"Total files: {total_files}")
print(f"Large files (>1MB): {len(large_files)}")
print(f"Old files (> {cutoff_days} days): {len(old_files)}")

end = time.time()
print(f"Execution time: {end - start:.4f} seconds")
