import csv
# import pandas


class CustomException(Exception):
    pass


class CsvVariant:

    def __init__(self, fileName):
        self.csvFp = open(fileName, "w+")

    def CreateCsv(self, DS="str"):

        if DS == "str":
            csvWriter = csv.writer(self.csvFp, delimiter=",")
            for i in range(0, 100):
                rowNum = str(i+1)
                csvWriter.writerow([rowNum+"colA", rowNum+"colB",
                                   rowNum+"colC", rowNum+"colD"])

        elif DS == "dict":
            csv_dictWriter = csv.DictWriter(self.csvFp, fieldnames=["A", "B", "C", "D"])
            for i in range(0, 100):
                rowNum = str(i+1)
                dataAsDict = {"A": rowNum+"colA", "B": rowNum+"colB",
                             "C": rowNum+"colC", "D": rowNum+"colD"}
                csv_dictWriter.writerow(dataAsDict)

    def ReadCsv(self):
        pass

    def InsertHeaderLine(self):
        pass

    def RemoveHeaderLine(self):
        pass

    def GetValFromCol(self, colName):
        pass


class PandasVariant:

    def __init__(self, fileName):
        self.pandasFp = open(fileName, "w+")

    def CreateCsv(self):
        pass

    def ReadCsv(self):
        pass

    def InsertHeaderLine(self):
        pass

    def RemoveHeaderLine(self):
        pass

    def GetValFromCol(self, colName):
        pass


if __name__ == "__main__":
    tmp = CsvVariant("sampleByCsv_dict.csv")
    tmp.CreateCsv("dict")
