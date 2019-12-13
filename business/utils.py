#!/usr/bin/python
import pandas as pd
import os
import json


class Utils:

    def __init__(this):
        pass

    @staticmethod
    def genFileName(filePath, fileName):
        fielPath = filePath.strip().rstrip("\\")
        if not os.path.exists(fielPath):
            os.mkdir(fielPath)
        return fielPath+"\\"+fileName

    @staticmethod
    def genSplitStr(fileName):
        result = []
        with open(fileName, 'r') as file_to_read:
            lines = file_to_read.read()
            StrArray = lines.split('\n')
            for eachstr in StrArray:
                if eachstr != "":
                    result.append("'"+eachstr.lstrip()+"'")
            finalStr = ",".join(result)
            return finalStr

    @staticmethod
    def dict2Excel(this, filePath, fileName,  sheetsDict):
        fullPath = this.genFileName(filePath, fileName)
        writer = pd.ExcelWriter(fullPath)
        for key in sheetsDict.keys():
            sheet = sheetsDict[key]
            df = pd.DataFrame(sheet[1], None, sheet[0])
            df.to_excel(writer, sheet_name=key)
        writer.save()
        writer.close()

    @staticmethod
    def getConnStr(filePath, Database):
        tempJson = json.load(open(filePath, 'r'))
        return tempJson[Database]["CONNECT_STR"]
