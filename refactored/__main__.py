from refactored.main import process_csv, read_file, write_data

if __name__ == '__main__':
    data = process_csv(input_data=read_file())
    # print(data)
    write_data(data=data)
