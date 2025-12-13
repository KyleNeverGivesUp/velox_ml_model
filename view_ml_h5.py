import h5py

if __name__ == '__main__':

    h5_file_path = "job_any_64.h5"

    with h5py.File(h5_file_path, "r") as f:
        print("model paras list:")
        for key in f.keys():
            data = f[key][()]
            print(f" {key}: shape = {data.shape}")
            print(data[:1])  # print first 5 rows
            # print(data[:5])  # print first 5 rows
            print("-" * 40) 1234