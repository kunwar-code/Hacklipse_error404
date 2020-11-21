from columnar import columnar
from click import style
from Read import Recommendation

def Table(Data):

    headers = ['Title','Authors','Summary']

    data = list(Data.values())[1:11]

    table = columnar(data, headers, no_borders=False)
    print(table)

Table(Recommendation())
    