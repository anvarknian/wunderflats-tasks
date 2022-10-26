import google.cloud.bigquery as bq


# Defining a function which to read the file
def read_file(path: str = 'myfile.csv', mode: str = 'r', encoding: str = 'utf-8') -> str:
    with open(path, mode, encoding=encoding) as file:
        return file.read()


def process_csv(input_data: str):
    data = [l.split(",") for l in input_data.split('\n')]
    data = [{data[0][k]: v for k, v in enumerate(l)} for l in data[1:]]
    return data


if __name__ == '__main__':
    i = read_file()
    d = process_csv(input_data=i)
    c = bq.Client()
    t = c.get_table("myproject.mydataset.mytable")
    e = c.insert_rows(t, d)
