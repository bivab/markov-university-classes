import sqlite3
import sys
import codecs

def verify(conn):
    result = conn.execute("SELECT value FROM info WHERE key = 'schema_version'")
    version = int(result.fetchone()[0])
    assert version == 9


def write_file(filename, data):
    with codecs.open(filename, 'w', 'utf8') as f:
        f.writelines(data)


def dump_units(conn):
    result = conn.execute("SELECT title FROM units")
    return (u"{0}\n".format(row[0]) for row in result)


def dump_abstract_units(conn):
    result = conn.execute("SELECT title FROM abstract_units")
    return (u"{0}\n".format(row[0]) for row in result)


def main(path):
    print(path)

    conn = sqlite3.connect(path)
    verify(conn)

    write_file('units.txt', dump_units(conn))
    write_file('abstract_units.txt', dump_abstract_units(conn))


if __name__ == '__main__':
    assert len(sys.argv) > 1
    main(sys.argv[1])
