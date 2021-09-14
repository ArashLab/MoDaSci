from enum import Enum

class DataTypes(Enum):
    HailTable = 1
    HailMatrixTable = 2
    PandasDataFrame = 3
    PandasSeries = 4
    SparkDataFrame = 5
    SparkRdd = 6
    PythonDict = 7
    PythonList = 8
    SqlTable = 9