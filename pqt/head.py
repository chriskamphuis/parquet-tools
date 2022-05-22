import argparse
import duckdb


class Head:

    def __init__(self, **kwargs):
        self.file = kwargs.get('file')
        self.lines = kwargs.get('lines')
        self.print_head()

    def print_head(self):
        cursor = duckdb.connect().cursor()
        cursor.execute(
            f"""
                SELECT * FROM "{self.file}" LIMIT ?
            """, [self.lines]
        )
        for entry in cursor.fetchall():
            print(entry)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file',
        help='The filename of the parquet file to show the first lines off.'
    )
    parser.add_argument(
        '-n',
        '--lines',
        default=10,
        type=int,
        help='Number of entries to show'
    )
    Head(**vars(parser.parse_args()))


if __name__ == '__main__':
    main()
