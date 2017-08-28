# MoinMoin Tables to CSV (and back)

MoinMoin is a wiki software that can also display tables. We have some of our
data only in those tables, which are formatted for humans. It is not directly
machine readable which is what is changed by these two scripts.

The `moinmoin_to_csv.py` script can convert text files which contain a MoinMoin
table into a CSV file. With `csv_to_moinmoin.py` one can convert these back.
The option `--header` will mark the first row in bold. The option ``--link``
will link the cells of the first column (excluding header if applicable) within
the wiki.

# License

MIT/Expat.
